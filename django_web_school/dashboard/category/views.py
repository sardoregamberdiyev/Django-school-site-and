from django.shortcuts import render, redirect
from dashboard.category.forms import CategoryForm

from dashboard.category.services import ctg_list, ctg_one, ctg_delete, ctg_rec_delete
from school.models import Category


def list(requests):
    all = ctg_list(pk=2)
    ctx = {
        'all': all
    }
    return render(requests, 'dashboard/category/list.html', ctx)


def one(requests, pk):
    one = ctg_one(pk)
    ctx = {
        'one': one
    }
    return render(requests, 'dashboard/category/detail.html', ctx)


def add(requests):
    form = CategoryForm()
    if requests.POST:
        forms = CategoryForm(requests.POST)
        if forms.is_valid():
            forms.save()
        else:
            print(forms.errors)
    ctx = {
        'form': form
    }

    return render(requests, 'dashboard/category/forms.html', ctx)


def edit(requests, pk):
    root = Category.objects.get(pk=pk)
    form = CategoryForm(instance=root)
    if requests.POST:
        forms = CategoryForm(requests.POST, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('ctg_list')
        else:
            print(forms.errors)
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/category/forms.html', ctx)


def delete(requests, pk):
    ctg_rec_delete(pk)
    ctg_delete(pk)
    return redirect('ctg_list')
