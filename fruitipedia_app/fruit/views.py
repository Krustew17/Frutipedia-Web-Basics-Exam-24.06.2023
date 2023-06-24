from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from fruitipedia_app.core.utils import get_user_profile
from fruitipedia_app.fruit.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruitipedia_app.fruit.models import FruitModel
import django.views.generic as views


# Create your views here.
# def create_fruit_view(request):
#     profile = get_user_profile()
#     if request.method == 'GET':
#         form = CreateFruitForm()
#     else:
#         form = CreateFruitForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     context = {
#         'user_profile': profile,
#         'form': form,
#     }
#     return render(request, 'fruit/create-fruit.html', context)
#
#
# def edit_fruit_view(request, pk):
#     profile = get_user_profile()
#     fruit = FruitModel.objects.filter(pk=pk).get()
#     if request.method == 'GET':
#         form = EditFruitForm(instance=fruit)
#     else:
#         form = EditFruitForm(request.POST, instance=fruit)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     context = {
#         'user_profile': profile,
#         'form': form,
#         'fruit': fruit,
#     }
#     return render(request, 'fruit/edit-fruit.html', context)
#
#
# def details_fruit_view(request, pk):
#     profile = get_user_profile()
#     fruit = FruitModel.objects.filter(pk=pk).get()
#     context = {
#         'user_profile': profile,
#         'fruit': fruit,
#     }
#     return render(request, 'fruit/details-fruit.html', context)
#
#
# def delete_fruit_view(request, pk):
#     profile = get_user_profile()
#     fruit = FruitModel.objects.filter(pk=pk).get()
#     if request.method == 'GET':
#         form = DeleteFruitForm(instance=fruit)
#     else:
#         form = DeleteFruitForm(request.POST, instance=fruit)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     context = {
#         'form': form,
#         'user_profile': profile,
#         'fruit': fruit,
#     }
#     return render(request, 'fruit/delete-fruit.html', context)
#

class CreateFruitView(views.CreateView):
    model = FruitModel
    form_class = CreateFruitForm
    template_name = 'fruit/create-fruit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard')


class DetailFruitView(views.DetailView):
    model = FruitModel
    template_name = 'fruit/details-fruit.html'
    context_object_name = 'fruit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context


class EditFruitView(views.UpdateView):
    model = FruitModel
    template_name = 'fruit/edit-fruit.html'
    form_class = EditFruitForm
    context_object_name = 'fruit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context

    def get_success_url(self):
        return reverse_lazy('fruit details', kwargs={'pk': self.object.pk})


class DeleteFruitView(views.DeleteView):
    model = FruitModel
    template_name = 'fruit/delete-fruit.html'
    form_class = DeleteFruitForm
    context_object_name = 'fruit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard')
