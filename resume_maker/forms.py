from django import forms

from django.forms import ModelForm, modelformset_factory, DateField
from django.conf import settings
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            'dob': DateInput(),

        }
        labels = {
            'dob': 'Date of Birth', }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        # fields = "__all__"
        exclude = ('person',)
        widgets = {
            'start_yr': DateInput(), 'end_yr': DateInput(),
        }
        # if =='Pursuing':
        #     show='End Year'
        # else:
        #     show='Expected End Year'
        labels = {
            'start_yr': 'Start Year',
            'end_yr': 'End Year',
            'cgpa': 'CGPA',
            'percent': 'Percentage'
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('person',)
        # if Experience.current == True:
        #     w='Present'
        widgets = {
            'current': forms.CheckboxInput(attrs={'name': 'current',
                                                  'type': 'checkbox',
                                                  'class': "checkboxinput form-check-input",
                                                  'id': 'id_curr',
                                                  'onchange': 'chapre(this)'

                                                  }),

            'join_dt': DateInput(),
            # 'left_dt': DateInput(),
            'left_dt': forms.DateInput(attrs={
                'name': 'left_dt',
                'type': 'date',
                'class': "dateinput form-control checkpro",
                'id': 'id_left',

            }),

            'details': forms.Textarea(attrs={'placeholder': 'Max 250 words\nKeep it to 3-4 points'})
        }
        labels = {
            'join_dt': 'Join Date',
            'left_dt': 'Left Date',
            'current': 'Currently Working Here',
        }

        # class ExampleForm(forms.Form):
        #     def __init__(self, *args, **kwargs):
        #         super().__init__(*args, **kwargs)
        #         self.helper = FormHelper(self)
        #         self.helper.layout = Layout(
        #             Field('current',id ='id_curr', css_class="form-contro-l"),
        #             Field('left_dt',id="id_left",css_class='sayam')
        #         )


class SkillsForm(ModelForm):
    class Meta:
        model = SkillSet
        exclude = ('person',)


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        exclude = ('person',)
        widgets = {
            'start_dt': DateInput(),
            # 'end_dt': DateInput(),
            'end_dt': forms.DateInput(attrs={
                'name': 'left_dt',
                'type': 'date',
                'class': "dateinput form-control checkpro",
                'id': 'id_left',
            }),
            'running': forms.CheckboxInput(attrs={'name': 'running',
                                                  'type': 'checkbox',
                                                  'class': "checkboxinput form-check-input",
                                                  'id': 'id_curr',
                                                  'onchange': 'chapre(this)'

                                                  }),

        }
        labels = {
            'start_dt': 'Start Date',
            'end_dt': 'End Date',
            'running': 'Currently Working on this project'
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
            'achievement': forms.Textarea(attrs={'placeholder': 'Max 250 words\nKeep it to 3-4 points'})
        }


class HobbiesForm(ModelForm):
    class Meta:
        model = Hobbies
        exclude = ('person',)
