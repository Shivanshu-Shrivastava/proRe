from django.contrib import admin
from .models import Person,Education,Experience,Projects,SkillSet,Languages,Achievements,Hobbies

# Register your models here.
admin.site.register(Person)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(SkillSet)
admin.site.register(Languages)
admin.site.register(Achievements)
admin.site.register(Hobbies)