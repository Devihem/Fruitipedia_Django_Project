from django.contrib import admin
from django.urls import path, include
from fruitpedia.fruits import views

urlpatterns = [
    path('', views.index, name=''),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/fruit/', views.FruitFormView.as_view(), name='create_fruit'),
    path('<int:fruit_pk>/',include([
        path('details/',views.detail_fruit, name='detail-fruit'),
        path('edit/',views.edit_fruit, name='edit-fruit'),
        path('delete/',views.delete_fruit, name='delete-fruit'),])),

]
