from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add', views.add_book),
    path('<int:id>', views.book)
]