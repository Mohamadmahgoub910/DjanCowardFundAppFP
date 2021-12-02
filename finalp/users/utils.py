from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    # print(f'search query {search_query} ')

    # search by skill
    # skills = Skill.objects.filter(name__iexact=search_query)
    skills = Skill.objects.filter(name__icontains=search_query)

    # search by name and short intro
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(head_line__icontains=search_query) |
        Q(skill__in=skills))

    return profiles
