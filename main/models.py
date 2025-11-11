from django.core.exceptions import ValidationError
from django.db import models
from django.urls import NoReverseMatch, reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    menu_name = models.CharField(max_length=100, db_index=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ["menu_name", "pk"]

    def __str__(self) -> str:
        return f"{self.menu_name} | {self.name}"

    def get_url(self) -> str:
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return "#"
        return self.url

    def clean(self) -> None:
        if self.url and self.named_url:
            raise ValidationError(
                "Нельзя одновременно указывать и прямой, и именованный URL."
            )
        if not self.url and not self.named_url:
            if self.parent:
                raise ValidationError(
                    "Необходимо указать либо прямой, либо именованный URL."
                )
