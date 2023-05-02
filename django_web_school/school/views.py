from django.shortcuts import render
from .models import Recipe, Category

# Create your views here.
from .services import get_recipes_all, get_recipes_one


def index(requests):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/index.html', ctx)


def uzb(requests):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/uz.html', ctx)

