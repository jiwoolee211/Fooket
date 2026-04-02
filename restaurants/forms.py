from django import forms
from .models import Restaurant
from .models import Comment

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'category', 'location', 'description','image'] 



class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment 
        fields = ['comment'] 