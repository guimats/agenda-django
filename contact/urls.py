from django.urls import path  # type: ignore
from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),  # type: ignore
    path('', views.index, name='index'),  # type: ignore
]
