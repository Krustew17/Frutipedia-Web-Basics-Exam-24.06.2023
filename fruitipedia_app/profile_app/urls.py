from django.urls import path

from .views import EditProfileView, DeleteProfileView, CreateProfileView, ProfileDetailsView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create profile'),
    path('details/', ProfileDetailsView.as_view(), name='profile details'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile'),
    path('edit/', EditProfileView.as_view(), name='edit profile'),
)
