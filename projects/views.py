from django.shortcuts import render
from django.http import HttpResponse

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
        'description':'Awesome open source project i am still working on'
    },
]

def projects(request):
    page="Projects"
    number = 10
    context={'page': page,'number':number,'projects':projectList}

    return render(request,'projects/projects.html',context) 

def project(request,pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i

    return render(request,'projects/single-project.html',{'project':projectObj})

