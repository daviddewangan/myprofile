from django.urls import path
from college.views import ProjectListAndFormView
from college import views

urlpatterns = [
   path('',ProjectListAndFormView.as_view(), name='main'),
]
