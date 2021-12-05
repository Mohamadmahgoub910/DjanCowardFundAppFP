from django.shortcuts import redirect, render
<<<<<<< HEAD
from .forms import ProjectForm,DonateForm
=======
from .forms import ProjectForm, ReviewForm
>>>>>>> 8c20278d454c11126b34269138d207f01e5f5c39
from .models import Project
# decorators loginrequire
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProjects
# some json data in a dict way :-
listProjects = [
    {
        'id': '1',
        'title': 'FullStack Python',
        'description': ' a final project contains many frameworks '
    },
    {
        'id': '2',
        'title': 'FullStack Dotnet',
        'description': ' a final project contains C# frameworks '
    },
    {
        'id': '3',
        'title': 'Mean stack ',
        'description': ' a final project contains Js frameworks '
    }
]


@login_required(login_url="login")
def projects(request):

    # page = 'project.html'
    # number = 3
    # context = {'page': page, 'number': number, 'projects': listProjects}
    # gets all projects
    projects = searchProjects(request)
    # projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project.html', context)


def singleproject(request, pk):
    # print i[id] , pk and make ru compare
    # token = None
    # print(listProjects)
    # for i in listProjects:
    #     if i['id'] == pk:
    #         token = i
    proObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = proObj
        review.owner = request.user.profile
        review.save()
        # update project vote count
        proObj.getVoteCount
        messages.success(request, 'ur review submitted')
    # get all details about each project
    # get all tags in the projects
    tags = proObj.tags.all()
    category = proObj.category.all()
    context = {'project': proObj, 'tags': tags,
               'category': category, 'form': form}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)

@login_required(login_url="login")
def createDonate(request):
    profile=request.user.profile
    formdonate=DonateForm()
    if request.method=='POST':
        formdonate=DonateForm(request.POST)
        if formdonate.is_valid():
           project = formdonate.save(commit=False)
           project.formdonate = profile
           return redirect('projects')
    context={'formdonate':formdonate}
    return render(request,'projects/donateform.html',context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    # Get id
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    # Get id
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, 'projects/project-form.html')
# https://us04web.zoom.us/j/4838177139?pwd=YUdRK0xSSGsrbzk0RWRuYXc2TE9xUT09
