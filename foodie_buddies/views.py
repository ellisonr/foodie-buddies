from django.shortcuts import render, redirect
from .forms import RestaurantForm, MenuItemForm, CommentForm, RestaurantUpdateForm, MenuItemUpdateForm, CommentUpdateForm
from .models import Restaurant, MenuItem, Comment
# Create your views here.


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'foodie_buddies/restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    return render(request, 'foodie_buddies/restaurant_detail.html', {'restaurant': restaurant})


def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'foodie_buddies/restaurant_form.html', {'form': form})


def restaurant_update(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    if request.method == 'POST':
        form = RestaurantUpdateForm(request.POST, instance=restaurant)
        if form.is_valid:
            restaurant = form.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantUpdateForm(instance=restaurant)
        return render(request, 'foodie_buddies/restaurant_update_form.html', {'form': form})


def restaurant_delete(request, pk):
    if request.method == 'POST':
        Restaurant.objects.get(id = pk).delete()
    return redirect('restaurant_list')


def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'foodie_buddies/menu_item_list.html', {'menu_items': menu_items})


def menu_item_detail(request, pk):
    menu_item = MenuItem.objects.get(id=pk)
    return render(request, 'foodie_buddies/menu_item_detail.html', {'menu_item': menu_item})


def menu_item_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save()
            return redirect('menu_item_detail', pk=menu_item.pk)
    else:
        form = MenuItemForm()
    return render(request, 'foodie_buddies/menu_item_form.html', {'form': form})


def menu_item_update(request, pk):
    menu_item = MenuItem.objects.get(id=pk)
    if request.method == 'POST':
        form = MenuItemUpdateForm(request.POST, instance=menu_item)
        if form.is_valid:
            menu_item = form.save()
            return redirect('menu_item_detail', pk=menu_item.pk)
    else:
        form = MenuItemUpdateForm(instance=menu_item)
        return render(request, 'foodie_buddies/menu_item_update_form.html', {'form': form})

def menu_item_delete(request, pk):
    if request.method == 'POST':
        MenuItem.objects.get(id = pk).delete()
    return redirect('menu_item_list')


def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'foodie_buddies/comment_detail.html', {'comment': comment})


def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'foodie_buddies/comment_form.html', {'form': form})


def comment_update(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, instance=comment)
        if form.is_valid:
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentUpdateForm(instance=comment)
        return render(request, 'foodie_buddies/comment_update_form.html', {'form': form})


def comment_delete(request, pk):
    if request.method == 'POST':
        Comment.objects.get(id = pk).delete()
    return redirect('comment_list')
	 