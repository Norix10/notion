from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_page_view, name='work-page'),

]