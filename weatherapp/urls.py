from django.urls import path
from weatherapp import views

urlpatterns = [
    path('',views.base,name="base")
]