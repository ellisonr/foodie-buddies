from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Restaurant, MenuItem, Comment
# from .forms import RestaurantForm, MenuItemForm, Comment Form

def restaurant_list(request):
	restaurants = Restaurant.objects.all()
	return render(request, 'foodie_buddies/restaurant_list.html', {'restaurants': restaurants})