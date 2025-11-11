from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import MenuItem


def menu_page(request: HttpRequest, slug: str) -> HttpResponse:
    item = get_object_or_404(MenuItem, slug=slug)
    return render(request, 'page.html', {'item': item})