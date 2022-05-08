from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-added_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('added_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_view.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('added_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "recipe_view.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class RecipeLike(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_view', args=[slug]))


class AddRecipe(View):

    def get(self, request):
        context = {'form': RecipeForm()}
        return render(request, 'add_recipe.html', context)

    def post(self, request):

        print('Start of POST request')
        form = RecipeForm(request.POST)
        print(form)
        title = form.instance.recipe_name
        print(title)
        recipe_exists = Recipe.objects.filter(
            Q(recipe_name__iexact=title)
        ).exists()
        print(recipe_exists)
        if recipe_exists:
            print('Recipe Name already exists')
            messages.error(request, 'Recipe Name already exists, please choose another name')
            context = {'form': form}
            return render(request, 'add_recipe.html', context)
        if form.is_valid():
            print("form is valid")
            form.instance.author = self.request.user
            print("author assigned")
            form.save()
            print("form is saved")
            messages.success(request, "Your recipe is awaiting approval")
            return redirect('home')
        else:
            print('form not valid')
            form = RecipeForm()
