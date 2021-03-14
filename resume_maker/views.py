from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from .utils import render_to_pdf
from django.template.loader import render_to_string

person = Person.objects.last()

try:
    personId = Person.objects.last().id
except AttributeError:
    personId = 1

forms = {
              "person":PersonForm,
              "edu": EducationForm,
              "exp": ExperienceForm,
              "skills": SkillsForm,
              "projects": ProjectsForm,
              "lang": LanguageForm,
              "ach": AchievementsForm,
              "hobby": HobbiesForm
}

# Create your views here.
def render_page(request):
    person = Person.objects.last()
    education = Education.objects.filter(person = person)
    exp = Experience.objects.filter(person=person)
    skill = SkillSet.objects.filter(person=person)
    prjct = Projects.objects.filter(person=person)
    ach = Achievements.objects.filter(person=person)

    context = {
        "person": person,
        "education": education,
        "exp": exp,
        "skill": skill,
        "prjct": prjct,
        "lang": Languages,
        "ach": ach,
        "hobb": Hobbies,
    }

    return render(request,"site.html",context)


def personal_det(request):
    return render(request,"getinput.html", { "person":PersonForm})

first = True
def get_input(request):
    global first
    person = Person.objects.last()
    #person = Person.objects.get()
    print(person)
    print(request.method)
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd.get('first_name')
            middle_name = cd.get('middle_name')
            last_name = cd.get('last_name')
            email = cd.get('email')
            mobile_no = cd.get('mobile_no')
            age = cd.get('age')
            dob = cd.get('dob')
            address = cd.get('address')
            github = cd.get('github')
            linkedin = cd.get('linkedin')
            website = cd.get('website')

            data = Person(first_name = first_name, middle_name = middle_name, last_name = last_name, email = email, mobile_no = mobile_no, age = age, dob = dob, address = address, github= github, linkedin = linkedin, website= website)
            temp = Person.objects.filter(first_name = first_name, middle_name = middle_name, last_name = last_name, email = email, mobile_no = mobile_no, age = age, dob = dob, address = address, github= github, linkedin = linkedin, website= website)

            if temp.exists():
                temp.update(first_name = first_name, middle_name = middle_name, last_name = last_name, email = email, mobile_no = mobile_no, age = age, dob = dob, address = address, github= github, linkedin = linkedin, website= website)
            else:
                form.save()

            #form = PersonForm()
            first = False
            return render(request,"getinput.html",{"form":form,"person":form.cleaned_data,"show":first})
    else:
        form = PersonForm()
    return render(request, "getinput.html",{"form":form,"show":first,"person":person})

def edu(request,id = None):
    person = Person.objects.last()
    show = True
    edu= Education.objects.filter(person = person)
        #form = EducationForm(instance = )
    if request.method == "POST":
        if id:
            delete = Education.objects.get(id = id)
            delete.delete()
        else:
            form = EducationForm(request.POST or None)
            if form.is_valid():
                cd = form.cleaned_data
                qualification = cd.get('qualification')
                institution = cd.get('institution')
                board = cd.get('board')
                start_yr = cd.get('start_yr')
                end_yr = cd.get('end_yr')
                cgpa = cd.get('cgpa')
                percent = cd.get('percent')

                data = Education(qualification = qualification, institution = institution, board = board, start_yr = start_yr, end_yr = end_yr, cgpa = cgpa, percent = percent,person = person)

                temp = Education.objects.filter(qualification = qualification, institution = institution, board = board, start_yr = start_yr, end_yr = end_yr, cgpa = cgpa, percent = percent,person = person)

                if temp.exists():
                    temp.update(qualification = qualification, institution = institution, board = board, start_yr = start_yr, end_yr = end_yr, cgpa = cgpa, percent = percent,person = person)
                else:
                    data.save()
        form = EducationForm()
        show = True
        return render(request,"Education.html",{"edu":form,"data":edu,"show":show})
    else:
        form = EducationForm()
    return render(request,"Education.html",{"edu":form,"data":edu,"show":show})

def wor(request):
    person = Person.objects.last()
    print(person)
    show = True
    exp = Experience.objects.filter(person = person)
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            type = cd.get('type')
            company = cd.get('company')
            role = cd.get('role')
            join_dt = cd.get('join_dt')
            left_dt = cd.get('left_dt')
            details = cd.get('details')

            data = Experience(type = type,company = company,role = role, join_dt = join_dt, left_dt = left_dt, details = details, person = person)
            temp = Experience.objects.filter(type = type,company = company,role = role, join_dt = join_dt, left_dt = left_dt, details = details, person = person)
            # try:
            if temp.exists():
                temp.update(type = type,company = company,role = role, join_dt = join_dt, left_dt = left_dt, details = details, person = person)
            else:
                data.save()

            show = True

            form = ExperienceForm()
            print(exp)

            return render(request,"work.html",{"exp":form,"data":exp,"show":show})
    else:
        form = ExperienceForm()
    return render(request,"work.html",{"exp" : form,"show":show,"data":exp})

def skill(request):
    show = True
    person = Person.objects.last()
    skills = SkillSet.objects.filter(person = person)
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            skill = cd.get('skill')
            exp = cd.get('experience')
            show = True
            data = SkillSet(skill = skill,experience = exp,person = person)
            temp = SkillSet.objects.filter(skill = skill,experience = exp,person = person)
            if temp.exists():
                temp.update(skill = skill,experience = exp,person = person)
            else:
                data.save()

            form = SkillsForm()

            return render(request,"skillset.html",{"skill":form,"data":skills,"show":show})
    else:
        form = SkillsForm()
    return render(request,"skillset.html", { "skill": form,"show":show,"data":skills})

def pro(request):
    show =True
    person = Person.objects.last()
    prjcts = Projects.objects.filter(person = person)
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            project = cd.get('project')
            start_dt = cd.get('start_dt')
            end_dt = cd.get('end_dt')
            running = cd.get('running')
            project_link = cd.get('project_link')

            data = Projects(project = project, start_dt = start_dt, end_dt = end_dt,running = running, project_link = project_link, person = person)

            temp = Projects.objects.filter(project = project, start_dt = start_dt, end_dt = end_dt,running = running, project_link = project_link, person = person)
            if temp.exists():
                temp.update(project = project, start_dt = start_dt, end_dt = end_dt,running = running, project_link = project_link, person = person)
            else:
                data.save()

            form = ProjectsForm()

            show = True

            return render(request,"project.html",{"prjct":form,"data":prjcts,"show":show})
    else:
        form = ProjectsForm()
    return render(request,"project.html", {"prjct": form,"show":show,"data":prjcts})

def lang(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"languages.html",{"lang":form,"data":form.cleaned_data})
    else:
        form = LanguageForm()
    return render(request,"languages.html", { "lang": form })

def ext(request):
    show = True
    person = Person.objects.last()
    ach = Achievements.objects.filter(person = person)
    if request.method == "POST":
        form = AchievementsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            achievement= cd.get('achievement')

            data = Achievements(achievement = achievement,person = person)
            temp = Achievements.objects.filter(achievement = achievement,person = person)
            if temp.exists():
                temp.update(achievement = achievement,person = person)
            else:
                data.save()
            show = True

            form = AchievementsForm()

            return render(request,"extra.html",{"ach":form,"data":ach, "show":show})
    else:
        form = AchievementsForm()
    return render(request,"extra.html", { "ach" : form, "show":show,"data":ach})

def get_pdf(request):
    pass

    """content = Person.objects.last()

    pdf = render_to_pdf("site.html")

    return HttpResponse(pdf, content_type = "application/pdf")

    return render_to_pdf(
            "site.html",
            {
                "pagesize":"A4",
                "data": content,
            })"""

    """html_string = render_to_string('site.html')
    
    html = HTML(string = html_string)

    html.write_pdf(target = 'resume.pdf')"""



