from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("<slug:slug>/", views.menu_page, name='menu_page'),
]
