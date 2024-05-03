from django.urls import path
from .views import index, contact

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', contact, name='contact'),
    path('', index, name='index'),
]
