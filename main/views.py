from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import MenuItem


def index_view(request):
    return render(request, "main/page.html", {"title": "Главная страница"})


def about_view(request):
    return render(request, "main/page.html", {"title": "О нас"})


def services_view(request):
    return render(request, "main/page.html", {"title": "Услуги"})


def terms(request):
    return render(request, "main/page.html", {"title": "Условия пользования"})


def service(request, service_slug: str):
    title = f'Услуга: {service_slug.replace("-", " ").capitalize()}'
    return render(request, "main/page.html", {"title": title})
