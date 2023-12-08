import contextlib

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from fruitpedia.fruits.forms import CategoryModeForm, FruitModelForm

from fruitpedia.fruits.models import Fruit


# Create your views here.

# Starting Page
def index(request):
    return render(request, template_name='common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all().order_by('name')
    context = {
        'fruits': fruits,
    }
    return render(request, 'common/dashboard.html', context, )


def create_fruits(request):
    return render(request, template_name='fruits/create-fruit.html')


def detail_fruit(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)
    context = {'fruit': fruit}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)

    if request.method == 'POST':
        form = FruitModelForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()

        return redirect('create-category')

    else:
        form = FruitModelForm(instance=fruit)

    context = {'form': form,
               'fruit': fruit}
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)
    print(request)
    if request.method == 'POST':
        fruit.delete()

        return redirect('dashboard')

    context = {'fruit': fruit}
    return render(request, 'fruits/delete-fruit.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryModeForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('')

    else:
        form = CategoryModeForm(request.GET)

    form = CategoryModeForm()
    context = {'form': form}
    return render(request, 'categories/create-category.html', context)


class FruitFormView(FormView):
    form_class = FruitModelForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('create-category')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
