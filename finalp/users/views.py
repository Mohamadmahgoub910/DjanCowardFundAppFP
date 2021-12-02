from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
# messages
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
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
def loginUser(request):
    # one form for login if he is authenticated
    page = 'login'
    # make some strict on the user
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == "POST":
        # print(request.POST)
        # get the username and password  from form
        username = request.POST['username']
        password = request.POST['password']
        # and store them in a context
        # context = {'username': username, 'password': password}
        # if username == "Mahgoub" and password == "12345":
        # return redirect('projects')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(
                request, 'username does not exist or password error')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # create a session
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Invalid user or Password !")
    return render(request, 'users/login_register.html')


# handle logout
def logoutUser(request):
    # destroy session
    logout(request)
    messages.error(request, "logged out ")
    return redirect('login')


# Register
# def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            # return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user = authenticate(username=user.username,
                                password=user.password1)

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
# make account profile
def accountProfile(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)


# edit Profile
@login_required(login_url='login')
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
