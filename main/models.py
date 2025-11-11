from django.db import models
from django.urls import reverse


# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True)

    def __str__(self) -> None:
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menu_page', kwargs={'slug': self.slug})
