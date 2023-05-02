from django import forms
from school.models import Recipe


class RecipeFrom(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

