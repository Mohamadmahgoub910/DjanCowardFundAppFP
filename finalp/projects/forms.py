from django.db import models
from django.forms import ModelForm, widgets
from .models import Project,Donation
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


class DonateForm(forms.ModelForm):
    class Meta:
        model=Donation
        fields=['donation_id','id','donation_amount']
      
    def __init__(self, *args, **kwargs):
        super(DonateForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
