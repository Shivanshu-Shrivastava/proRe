from django.shortcuts import render
from .models import *


# Create your views here.


def get_input(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(Person.objects.all())
    if request.method == "POST":
        new_name = request.POST.get("name")
        new_email = request.POST.get("email")
        new_phone = request.POST.get("phone")
        new_github = request.POST.get("github")
        new_linked = request.POST.get("linkedin")
        new_dob = request.POST.get("dob")
        new_address = request.POST.get("address")
        Person.objects.create(full_name=new_name, email=new_email,
                              phone=new_phone, dateob=new_dob,
                              address=new_address, github=new_github
                              , linkedin=new_linked)

        objeedu = len(Person.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = Person.objects.get(id=total + e)
            list.append(realedu)

            total -= 1
        show = True
        disable=True
    else:
        new_name = None
        show = False
        new_email = None
        new_phone = None
        new_github = None
        new_linked = None
        new_dob = None
        new_address = None
        disable = False

    context = {
        "name": new_name,
        "email": new_email,
        "phone": new_phone,
        "github": new_github,
        "linked": new_linked,
        "dob": new_dob,
        "address": new_address,
        "show": show,
        "list":list,
        'disable':disable

    }

    # print('//////////')
    # print(request.POST)
    return render(request, "resume_maker/getinput.html", context)


def render_page(request):
    global e
    objepersonal = Person.objects.all()
    c = len(objepersonal)
    realper = Person.objects.get(id=c)
    # EducatMOdel
    objeedu = EducatModel.objects.all()
    e = len(objeedu)
    print('3###########', e)
    realedu = EducatModel.objects.get(id=e)
    # work COde
    objework = workModel.objects.all()
    w = len(objework)
    realwork = workModel.objects.get(id=w)
    # position
    objepos = posModel.objects.all()
    p = len(objepos)
    realpos = posModel.objects.get(id=p)
    # proition
    objepro = proModel.objects.all()
    pr = len(objepro)
    realpro = proModel.objects.get(id=pr)
    # academic
    objeaca = acaModel.objects.all()
    ac = len(objeaca)
    realaca = acaModel.objects.get(id=ac)
    # extra
    objextra = extraModel.objects.all()
    ob = len(objextra)
    realextra = extraModel.objects.get(id=ob)

    context = {
        "name": realper.full_name,
        "email": realper.email,
        "phone": realper.phone,
        "address": realper.address,
        'dob': realper.dateob,
        'github': realper.github,
        'linked': realper.linkedin,
        "degree": realedu.degree,
        'syear': realedu.start_yr,
        'eyear': realedu.end_yr,
        'institute': realedu.institute,
        'score': realedu.score,
        'profile': realwork.profile,
        'title': realwork.title,
        'description': realwork.description,
        'first': realpos.first,
        'last': realpos.last,
        'handle': realpos.handle,
        'project': realpro.project,
        'industrial': realpro.industrial,
        'projlink': realpro.projlink,
        'academic': realaca.academic,
        'extra': realextra.extra,

    }

    return render(request, "resume_maker/site.html", context)


def edu(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(EducatModel.objects.all())

    if request.method == "POST":
        checkloo = True

        new_degree = request.POST.get('degree')
        new_syear = request.POST.get('syear')
        new_eyear = request.POST.get('eyear')
        new_score = request.POST.get('score')
        new_institute = request.POST.get('institute')
        EducatModel.objects.create(degree=new_degree, start_yr=new_syear,
                                   end_yr=new_eyear, score=new_score,
                                   institute=new_institute)
        objeedu = len(EducatModel.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = EducatModel.objects.get(id=total + e)
            list.append(realedu)

            total -= 1

        show = True
        save = ' Next'



    else:
        save = 'Skip'

        checkloo = False
        new_degree = None
        new_syear = None
        new_eyear = None
        new_score = None
        new_institute = None
        show = False
        education = None

    print(list)
    context = {
        'checkloo': checkloo,
        'degree': new_degree,
        'score': new_score,
        'syear': new_syear,
        'eyear': new_eyear,
        'institute': new_institute,
        "show": show,
        'save': save,
        # 'education':education,
        'list': [l for l in list],

    }

    return render(request, "resume_maker/Education.html", context)


def wor(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(workModel.objects.all())
    if request.method == "POST":
        save = 'Next'
        new_profile = request.POST.get('profile')
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        workModel.objects.create(profile=new_profile, title=new_title,
                                 description=new_description)
        objeedu = len(workModel.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = workModel.objects.get(id=total + e)
            list.append(realedu)
            total -= 1

    else:
        save = 'Skip'
        new_profile = None
        new_title = None
        new_description = None
    # print('/////////')
    # print(new_profile)
    # print(request.POST)
    lasteedu = len(workModel.objects.all())
    last=workModel.objects.last()
    print('@@@@@',last,lasteedu)
    context = {
        'Save': save,
        'profile': new_profile,
        'title': new_profile,
        'descripton': new_description,
        'list': list
    }
    return render(request, "resume_maker/work.html", context)


def pos(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(posModel.objects.all())
    if request.method == "POST":
        save = 'Next'
        new_first = request.POST.get('first')
        new_last = request.POST.get('last')
        new_handle = request.POST.get('handle')
        posModel.objects.create(first=new_first, last=new_last,
                                handle=new_handle)
        objeedu = len(posModel.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = posModel.objects.get(id=total + e)
            list.append(realedu)
            total -= 1
    else:
        save = 'Skip'
        new_first = None
        new_last = None
        new_handle = None

    # print('#####')
    # print(save)
    context = {
        'pos_save': save,
        'first': new_first,
        'last': new_last,
        'handle': new_handle,
        'list': list
    }
    return render(request, "resume_maker/position.html", context)


def pro(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(proModel.objects.all())
    if request.method == "POST":
        save = 'Next'
        new_project = request.POST.get('project')
        new_industrial = request.POST.get('industrial')
        new_projlink = request.POST.get('projlink')
        proModel.objects.create(project=new_project, industrial=new_industrial,
                                projlink=new_projlink)
        objeedu = len(proModel.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = proModel.objects.get(id=total + e)
            list.append(realedu)
            total -= 1
    else:
        save = 'Skip'
        new_project = None
        new_industrial = None
        new_projlink = None

    context = {
        'pro_save': save,
        'project': new_project,
        'industrial': new_industrial,
        'projlink': new_projlink,
        'list': list
    }
    return render(request, "resume_maker/project.html", context)


def aca(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(acaModel.objects.all())
    if request.method == "POST":
        save = 'Next'
        new_academic = request.POST.get('academic')
        acaModel.objects.create(academic=new_academic)
        objeedu = len(acaModel.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = acaModel.objects.get(id=total + e)
            list.append(realedu)
            total -= 1

    else:
        save = 'Skip'
        new_academic = None

    context = {
        'aca_save': save,
        'academic': new_academic,
        'list': list
    }
    return render(request, "resume_maker/academic.html", context)


def ext(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(extraModel.objects.all())
    if request.method == "POST":
        save = 'Show my Resume'
        new_extra = request.POST.get('extra')
        extraModel.objects.create(extra=new_extra)
        objeedu = len(extraModel.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = extraModel.objects.get(id=total + e)
            list.append(realedu)
            total -= 1


    else:
        save = 'Skip and Show my Resume'
        new_extra = None
    # print('#####')
    # print(save)
    context = {
        'show_resume': save,
        'extra': new_extra,
        'list': list
    }
    return render(request, "resume_maker/extra.html", context)

def add(request):
    global e
    list = []
    # e=len(EducatModel.objects.all())
    # print('###############:####',e)
    if request.method == 'GET':
        e = len(additional.objects.all())
    if request.method == "POST":
        save = 'Show My Resume'
        new_additi = request.POST.get('additi')
        additional.objects.create(add=new_additi)
        objeedu = len(additional.objects.all())

        total = objeedu - e
        while total >= 1:
            realedu = additional.objects.get(id=total + e)
            list.append(realedu)
            total -= 1


    else:
        save = 'Skip and Show my Resume'
        new_additi = None
    # print('#####')
    # print(save)
    context = {
        'show_resume': save,
        'additi': new_additi,
        'list': list
    }
    return render(request, "resume_maker/additi.html", context)
