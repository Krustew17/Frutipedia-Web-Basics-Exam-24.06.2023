from django.urls import path, include
from .views import CreateFruitView, DetailFruitView, EditFruitView, DeleteFruitView


urlpatterns = (
    path('create/', CreateFruitView.as_view(), name='create fruit'),
    path('<int:pk>/', include([
        path('details/', DetailFruitView.as_view(), name='fruit details'),
        path('edit/', EditFruitView.as_view(), name='edit fruit'),
        path('delete', DeleteFruitView.as_view(), name='delete fruit'),
    ]))
)
