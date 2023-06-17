from django.urls import path

from digidesk.views import index, create

urlpatterns = [
  path('', index),
  path('create', create)
]