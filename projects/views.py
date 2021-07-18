from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
projectList=[
    {
        'id':'1',
        'title':"ecommerce Website",
        'description':'fully funtional ecommerce'
    },
    {
        'id':'2',
        'title':"Portfolio Website",
        'description':'this is project where I built my portfolio'
    },
    {
        'id':'3',
        'title':"Social Network",
        'description':'Awesom e open source project i am still working on'
    },
]

def projects(request):
    projects = Project.objects.all()
    context={'projects':projects}

    return render(request,'projects/projects.html',context) 

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request,'projects/single-project.html',{'project':projectObj,})

