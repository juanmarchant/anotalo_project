from django.urls import path
from .views import SignUpView, ProfileUpdate

app_name= 'register'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
