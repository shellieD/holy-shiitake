from .models import Comment, Recipe
from django import forms


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
