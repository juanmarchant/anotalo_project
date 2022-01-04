from django.urls import path
from .views import HomePageView, add_task
from dashboard import views

app_name= 'dashboard'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    # CRUD
    path('create/', views.add_task, name="create"),
    path('edit/<int:task_id>', views.edit_task, name="edit"),
    path('delete/<int:task_id>', views.delete_task, name="delete"),
]
