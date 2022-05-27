from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms import HiddenInput


class CommentForm(forms.ModelForm):
    """Comment Form """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """Recipe Form"""
    class Meta:
        model = Recipe
        fields = (
            'recipe_name',
            'description',
            'ingredients',
            'method',
            'recipe_image',
        )
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }


class ApproveForm(forms.ModelForm):
    """Form to Approve Recipes"""
    class Meta:
        model = Recipe
        fields = (
            'slug',
            'status',
        )
        widgets = {
            'slug': HiddenInput(),
        }
