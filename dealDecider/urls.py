from django.urls import path
from . import views

app_name = 'dealDecider'
urlpatterns = [
  #path('', views.index, name='index'),
  path('', views.process_data, name='process_data'),
]