from django import forms
from django.forms import ModelForm,modelformset_factory,DateField
from django.conf import settings
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            'dob': DateInput(),
        }



class EducationForm(ModelForm):
    class Meta:
        model = Education
        #fields = "__all__"
        exclude = ('person',)
        widgets = {
            'start_yr': DateInput(),'end_yr': DateInput(),
        }
        labels = {
            'start_yr':'Start Year',
            'end_yr':'End Year',
            'cgpa':'CGPA',
            'percent':'Percentage'
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('person',)
        widgets = {
            'join_dt': DateInput(),
            'left_dt': DateInput(),
            'details': forms.Textarea(attrs={'placeholder': 'Max 250 words'})
        }
        labels = {
            'join_dt':'Join Date',
            'left_dt':'Left Date',
            'current':'Currently Working Here',
        }


class SkillsForm(ModelForm):
    class Meta:
        model = SkillSet
        exclude = ('person',)

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        exclude = ('person',)
        widgets = {
            'start_dt':DateInput(),
            'end_dt': DateInput(),
        }
        labels = {
            'start_dt':'Start Date',
            'end_dt':'End Date',
            'running':'Recently Working on this project'
        }

class LanguageForm(ModelForm):
    class Meta:
        model = Languages
        exclude = ('person',)


class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        exclude = ('person',)
        widgets = {
            'achievement': forms.Textarea(attrs={'placeholder': 'Max 250 words'})
        }


class HobbiesForm(ModelForm):
    class Meta:
        model = Hobbies
        exclude = ('person',)