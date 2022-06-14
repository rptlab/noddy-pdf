from django.urls import path
from . import views as noddy_views

urlpatterns = [
    path('pdf/', noddy_views.view_pdf),
]
