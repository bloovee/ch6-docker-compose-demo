from django.urls import path
from .views import book_list, book_create, book_update, book_delete

urlpatterns = [
   path('', book_list, name='book_list'),
   path('new/', book_create, name='book_create'),
   path('edit/<int:pk>/', book_update, name='book_update'),
   path('delete/<int:pk>/', book_delete, name='book_delete'),
]
