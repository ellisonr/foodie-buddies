from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:pk>', views.restaurant_detail, name='restaurant_detail'),
    path('menuitems/', views.menu_item_list, name='menu_item_list'),
    path('menuitems/<int:pk>', views.menu_item_detail, name='menu_item_detail'),
    path('restaurant/new', views.restaurant_create, name='restaurant_create'),
    path('menuitems/new', views.menu_item_create, name='menu_item_create'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail',)
]
