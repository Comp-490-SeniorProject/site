from django.urls import path

from web.frontend import views

app_name = "frontend"
urlpatterns = [
    path("", views.index, name="index"),
]
