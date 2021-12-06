from django.shortcuts import render
from django.views.generic import *
from flows.models import Project
from django.views.generic.list import *
from django.core.paginator import Paginator

# Create your views here.
 

class IndexView(ListView):
    template_name = 'flows/index.html' 
    model = Project
    paginate_by = 3
    context_object_name = 'projects'




    

class ProjectDetailView(DetailView):
    template_name = 'flows/projectdetail.html'   
    model = Project
    context_object_name = 'project' 

    def get_context_data(self, **kwargs): 
        return super().get_context_data(**kwargs)
        return context 