from django.urls import path  # type: ignore
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
