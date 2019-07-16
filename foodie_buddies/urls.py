from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list),
	 path('restaurants/', views.restaurant_list),
    path('restaurants/<int:pk>', views.restaurant_detail, name='restaurant_detail'),
]
