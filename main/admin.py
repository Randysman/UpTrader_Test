from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "title")
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "menu", "parent")
    prepopulated_fields = {"slug": ("title",)}