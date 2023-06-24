from django.shortcuts import render, redirect
import django.views.generic as views

from fruitipedia_app.core.utils import get_user_profile
from fruitipedia_app.fruit.models import FruitModel


# Create your views here.
# def index(request):
#     profile = get_user_profile()
#
#     context = {
#         'user_profile': profile,
#     }
#
#     return render(request, 'common/index.html', context)
#
#
# def dashboard_view(request):
#     profile = get_user_profile()
#     fruits = FruitModel.objects.all()
#     context = {
#         'user_profile': profile,
#         'fruits': fruits,
#     }
#     return render(request, 'common/dashboard.html', context)
#

class HomePageView(views.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        return context


class DashboardView(views.ListView):
    template_name = 'common/dashboard.html'
    model = FruitModel

    def get_context_data(self, *, object_list=None, **kwargs):
        fruits = FruitModel.objects.all()
        context = super().get_context_data(**kwargs)
        context['user_profile'] = get_user_profile()
        context['fruits'] = fruits
        return context

    def get(self, request, *args, **kwargs):
        if get_user_profile() is None:
            return redirect('home page')

        return super().get(request, *args, **kwargs)
