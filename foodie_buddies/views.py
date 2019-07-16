from django.shortcuts import render, redirect
from .forms import RestaurantForm, MenuItemForm, CommentForm
from .models import Restaurant, MenuItem, Comment
# Create your views here.

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'foodie_buddies/restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    return render(request, 'foodie_buddies/restaurant_detail.html', {'restaurant': restaurant})


def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'foodie_buddies/menu_item_list.html', {'menu_items': menu_items})


def menu_item_detail(request, pk):
    menu_item = MenuItem.objects.get(id=pk)
    return render(request, 'foodie_buddies/menu_item_detail.html', {'menu_item': menu_item})

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'foodie_buddies/restaurant_form.html', {'form': form})
