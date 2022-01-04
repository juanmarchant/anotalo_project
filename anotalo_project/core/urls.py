from django.urls.conf import path
from .views import HomePageView

app_name= 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
