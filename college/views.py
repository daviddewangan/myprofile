from django.shortcuts import render, redirect, get_object_or_404
from college.models import Project, Contact, Blog
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.core.mail import get_connection, send_mail, message
from college.forms import ContactForm, Contactform
from django.template.context_processors import request

from django.template.loader import get_template

from django.contrib.messages.context_processors import messages

# Create your views here.
class ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = Project
    template_name = 'college/main.html'
    context_object_name = 'list_projects' 
    queryset = Project.objects.all().order_by("-pub_date")
    object_list = None

    form_class = Contactform
    success_url = '/' 
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        form.save()
        
        return super(ProjectListAndFormView, self).form_valid(form)
    
    

        
    



