from django.shortcuts import render, redirect
import django.views.generic as views
from django.urls import reverse_lazy

from fruitipedia_app.core.utils import get_user_profile
from fruitipedia_app.fruit.models import FruitModel
from fruitipedia_app.profile_app.forms import CreateProfileForm, EditProfileForm
from fruitipedia_app.profile_app.models import ProfileModel


# Create your views here.
# def create_profile_view(request):
#     if request.method == 'GET':
#         form = CreateProfileForm()
#     else:
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile/create-profile.html', context)
#
#
# def edit_profile_view(request):
#     profile = get_user_profile()
#     if request.method == 'GET':
#         form = EditProfileForm(instance=profile)
#     else:
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#
#     context = {
#         'user_profile': profile,
#         'form': form,
#     }
#     return render(request, 'profile/edit-profile.html', context)
#
#
# def delete_profile_view(request):
#     profile = get_user_profile()
#     if request.method == 'POST':
#         profile.delete()
#         FruitModel.objects.all().delete()
#         return redirect('home page')
#
#     context = {
#         'user_profile': profile,
#     }
#     return render(request, 'profile/delete-profile.html', context)
#
#
# def details_profile_view(request):
#     profile = get_user_profile()
#     amount_posts = FruitModel.objects.all().count()
#     context = {
#         'user_profile': profile,
#         'amount_posts': amount_posts,
#     }
#     return render(request, 'profile/details-profile.html', context)


class CreateProfileView(views.CreateView):
    model = ProfileModel
    form_class = CreateProfileForm
    template_name = 'profile/create-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_profile'] = get_user_profile()
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home page')


class EditProfileView(views.UpdateView):
    model = ProfileModel
    form_class = EditProfileForm
    template_name = 'profile/edit-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context

    def get_object(self, queryset=None):
        return ProfileModel.objects.first()

    def get_success_url(self):
        return reverse_lazy('profile details')


class ProfileDetailsView(views.DetailView):
    model = ProfileModel
    template_name = 'profile/details-profile.html'

    def get_context_data(self, **kwargs):
        amount_posts = FruitModel.objects.all().count()
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        context['amount_posts'] = amount_posts
        return context

    def get_object(self, queryset=None):
        return ProfileModel.objects.first()


class DeleteProfileView(views.DeleteView):
    model = ProfileModel
    template_name = 'profile/delete-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context

    def get_object(self, queryset=None):
        return ProfileModel.objects.first()

    def get_success_url(self):
        return reverse_lazy('home page')

    def form_valid(self, form):
        FruitModel.objects.all().delete()
        return super().form_valid(form)
