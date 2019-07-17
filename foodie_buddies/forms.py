from django import forms
from .models import Restaurant, MenuItem, Comment


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'cuisine', 'street_address',
                  'city', 'state', 'country',)

class RestaurantUpdateForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'cuisine', 'street_address',
                  'city', 'state', 'country',)

class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = ('name', 'price', 'description', 'image_url', 'restaurant',)

class MenuItemUpdateForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = ('name', 'price', 'description', 'image_url', 'restaurant',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'body', 'menu_item',)

class CommentUpdateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'body', 'menu_item',)