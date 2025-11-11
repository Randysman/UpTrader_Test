from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="main_page"),
    path("about/", views.about_view, name="about_page"),
    path("terms/", views.terms, name="terms_of_service_page"),
    path("services/", views.services_view, name="services_page"),
    path("services/<slug:service_slug>/", views.service, name="service_detail_page"),
]
