from django.contrib import admin
from .models import Project, Review, Tag, Category,Donation

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Donation)