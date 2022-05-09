from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path(
        'recipes/<slug:slug>/', views.RecipeView.as_view(), name='recipe_view'
    ),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('recipes/add', views.AddRecipe.as_view(), name="add_recipe"),
    path(
        'recipes/my_recipes', views.UserRecipes.as_view(), name='user_recipes'
    )
]
