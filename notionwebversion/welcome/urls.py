from django.urls import path
from . import views

urlpatterns = [
    path('', views.welocome_view, name='welcome'),
]