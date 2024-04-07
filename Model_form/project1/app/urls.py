from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_data, name='add_url'),
    path('show/',views.show_data, name='show_url'),
    path('update/<int:pk>/',views.update_data, name='update_url'),
    path('delete/<int:pk>/',views.delete_data, name='delete_url'),
]