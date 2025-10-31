from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('read/',views.read,name='read'),
    path('update/<int:sid>/',views.update,name='update'),
    path('delete/<int:sid>/',views.delete_data,name='delete'),

]