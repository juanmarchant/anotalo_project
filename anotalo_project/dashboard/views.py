# Class View and Methods
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Functions
from django.shortcuts import redirect

# Messages
from django.contrib import messages 

#Models
from django.contrib.auth.models import User
from .models import *


# Create your views here.
@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name= "dashboard/home.html"

    def get_context_data(self, **kwargs,):
        context = super(TemplateView, self).get_context_data(**kwargs)
        user = self.request.user
        context ={
            'all_task': user.tasks.all()[::-1],
            'avatar': user.profile.avatar,
            'background': user.profile.background,
        }
        return context


def select_option(content):
    color = ['default','#FFF7A1', '#F9E26E']
    if content == 'red':
        color[0] = 'red'
        color[1] = '#FF8585'
        color[2] = '#ED5B66'

    if content == 'green':
        color[0] = 'green'
        color[1] = '#B3FF7A'
        color[2] = '#9DF85B'

    if content == 'purple':
        color[0] = 'purple'
        color[1] = '#E777FA'
        color[2] = '#DB5DFC'
    
    if content == 'blue':
        color[0] = 'blue'
        color[1] = '#7BDEFE'
        color[2] = '#5ED7FD'

    if content == 'pink':
        color[0] = 'pink'
        color[1] = '#FB79CA'
        color[2] = '#FE5EBE'
    return color

def add_task(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        errors = Task.objects.task_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/dashboard/")       
        else:
            color = select_option(request.POST['option'])
            task = Task(user = user, content = request.POST['content'])
            final_task = TaskColor(task= task, color=color[0] ,glue_color= color[1], content_color= color[2])
            task.save()
            final_task.save()
            messages.success(request, "You have successfully added a task")
            return redirect("/dashboard/")       

def edit_task(request, task_id):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        edit_task = user.tasks.get(id=task_id)
        color = select_option(request.POST['option'])
        
        if request.POST['content'] == edit_task.content and edit_task.colors.color == color[0]:
            messages.error(request, 'The task could not be edite because the edited is the same ')
            return redirect("/dashboard/") 

        elif len(request.POST['content']) > 130:
            messages.error(request, 'You can only make task with 130 characters')
            return redirect("/dashboard/")

        elif request.POST['content'] == '' and request.POST['option'] == 'Select color':
            messages.error(request, "You didn't change anything")
            return redirect("/dashboard/")

        elif request.POST['content'] or request.POST['option']:
            if request.POST['content'] != "":
                edit_task.content = request.POST['content']    
            if request.POST['option'] != 'Select color':
                edit_task.colors.color = color[0]
                edit_task.colors.glue_color = color[1]
                edit_task.colors.content_color = color[2]
            edit_task.save()
            edit_task.colors.save()            
            messages.success(request, 'The task was edited successfully')
            return redirect("/dashboard/")

def delete_task(request, task_id):
    if request.method == "POST":
        user = User.objects.get(id = request.user.id)
        delete_task = user.tasks.get(id=task_id)
        delete_task.delete()
        return redirect("/dashboard/")       