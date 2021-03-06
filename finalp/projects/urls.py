from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('singleproject/<str:pk>/', views.singleproject, name="project"),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
    path('adddonate/',views.createDonate,name="add_donate")
]
