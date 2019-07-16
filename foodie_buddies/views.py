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

def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'foodie_buddies/comment_detail.html', {'comment': comment})

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'foodie_buddies/restaurant_form.html', {'form': form})


def menu_item_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save()
            return redirect('menu_item_detail', pk=menu_item.pk)
    else:
        form = MenuItemForm()
    return render(request, 'foodie_buddies/menu_item_form.html', {'form': form})


def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'foodie_buddies/comment_form.html', {'form': form})
