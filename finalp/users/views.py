from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# messages
from django.contrib import messages
from .forms import SignUpForm, ProfileForm, SkillForm
from .utils import searchProfiles
# Create your views here.


def profiles(request):
    profiles = searchProfiles(request)
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user_profile.html', context)


# handle login
# make account profile
def accountProfile(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills,
               'projects': projects}
    return render(request, 'users/account.html', context)

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('edit-account')
    return render(request,'users/signup.html',{'form':form})



# edit Profile

def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)




# AddSkill
def createSkill(request):
    profile = request.user.profile
    form = SkillForm(instance=profile)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill success was created!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
# Edit skill
def editSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill success was updated!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url="login")
# delete skill
def deleteSkill(request, pk):
    profile = request.user.profile
    # Get id
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request, 'Skill successfully deleted !')
        return redirect('account')
    return render(request, 'projects/project-form.html')
