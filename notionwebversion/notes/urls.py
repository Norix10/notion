from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_page_view, name='work-page'),
    path('/note_create', views.create_note_view, name='note_create'),
]