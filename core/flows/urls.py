from django.urls import path, include
from .views import *

app_name = 'flows'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/' , ProjectDetailView.as_view(), name= 'project_detail'),
]