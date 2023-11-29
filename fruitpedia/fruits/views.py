from django.shortcuts import render

from fruitpedia.fruits.models import Fruit


# Create your views here.

# Starting Page
def index(request):
    return render(request, template_name='common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits,
    }
    return render(request, 'common/dashboard.html', context, )


def create_fruits(request):
    return render(request, template_name='fruits/create-fruit.html')


def detail_fruit(request, fruit_pk):
    return render(request, template_name='fruits/details-fruit.html')


def edit_fruit(request, fruit_pk):
    return render(request, template_name='fruits/edit-fruit.html')


def delete_fruit(request, fruit_pk):
    return render(request, template_name='fruits/delete-fruit.html')


def create_category(request):
    return render(request, template_name='categories/create-category.html')
