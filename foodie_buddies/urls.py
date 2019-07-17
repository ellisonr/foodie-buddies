from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:pk>', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/new', views.restaurant_create, name='restaurant_create'),
	 path('restaurants/<int:pk>/edit', views.restaurant_update, name = 'restaurant_update'),
    path('restaurants/<int:pk>/delete', views.restaurant_delete, name = 'restaurant_delete'),
	 path('menuitems/', views.menu_item_list, name='menu_item_list'),
    path('menuitems/<int:pk>', views.menu_item_detail, name='menu_item_detail'),
    path('menuitems/new', views.menu_item_create, name='menu_item_create'),
	 path('menuitems/<int:pk>/edit', views.menu_item_update, name = 'menu_item_update'),
    path('menuitems/<int:pk>/delete', views.menu_item_delete, name = 'menu_item_delete'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
	 path('comments/<int:pk>/edit', views.comment_update, name = 'comment_update'),
    path('comments/<int:pk>/delete', views.comment_delete, name = 'comment_delete'),
]
