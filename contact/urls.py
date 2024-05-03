from django.urls import path
from .views import index, contact, search, create, update

app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    #
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', contact, name='contact'),
    path('contact/create/', create, name='create'),
    path('contact/<int:contact_id>/update/', update, name='update'),
]
