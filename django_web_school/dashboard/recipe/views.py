from django.shortcuts import render, redirect

from school.models import Recipe
from .forms import RecipeFrom
from .services import get_recipe_list, get_recipe_one, delete


def rec_list(requests):
    lists = get_recipe_list()
    ctx = {
        'all': lists
    }
    return render(requests, 'dashboard/recipe/list.html', ctx)


def rec_detail(requests, pk):
    one = get_recipe_one(pk)
    print(one)
    ctx = {
        'one': one
    }
    return render(requests, 'dashboard/recipe/detail.html', ctx)


def add(requests):
    form = RecipeFrom()
    if requests.POST:
        forms = RecipeFrom(requests.POST, requests.FILES)
        if forms.is_valid():
            forms.save()
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/recipe/forms.html', ctx)


def edit(requests, pk):
    root = Recipe.objects.get(pk=pk)
    form = RecipeFrom(instance=root)
    if requests.POST:
        forms = RecipeFrom(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('rec_list')
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/recipe/forms.html', ctx)


def rec_delete(requests, pk):
    delete(pk)
    return redirect('rec_list')
