<<<<<<< HEAD
from django.db import models
from django.forms import ModelForm, widgets
from .models import Project,Donation
=======
from django.db.models import fields
from django.forms import ModelForm
from .models import Project, Review
>>>>>>> 8c20278d454c11126b34269138d207f01e5f5c39
from django import forms


# make it generic
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'description', 'featured_image',
                  'demo_link', 'source_link', 'tags', 'total_budget', 'end_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
    # self.fields['title'].widgets.attrs.update({'class':'input'})


<<<<<<< HEAD
class DonateForm(forms.ModelForm):
    class Meta:
        model=Donation
        fields=['donation_id','id','donation_amount']
      
    def __init__(self, *args, **kwargs):
        super(DonateForm, self).__init__(*args, **kwargs)
=======
# Review
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

>>>>>>> 8c20278d454c11126b34269138d207f01e5f5c39
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
