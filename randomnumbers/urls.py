from django.urls import path

from . import views

urlpatterns = [
    # ex: /randomnumbers/
    path("", views.random_number_request),
    # ex: /randomnumbers/5/
    path("<int:id>/", views.random_number_status),
]