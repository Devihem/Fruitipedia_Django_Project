from django import forms
from fruitpedia.fruits.models import Category, Fruit


class CategoryModeForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
