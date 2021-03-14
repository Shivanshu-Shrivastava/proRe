from django.urls import path
from . import views

urlpatterns = [
    path('site', views.render_page, name='res'),
    path('start', views.personal_det),
    path('getinput', views.get_input, name='input'),
    path('getinput/<int:id>/', views.get_input),
    path('education', views.edu, name='Education'),
    path('education/<int:id>',views.edu),
    path('work', views.wor, name='work'),
    path('skills',views.skill),
    #path('position.html', views.pos, name='position'),
    path('project', views.pro, name='project'),
    path('extra', views.ext, name='academic'),
    #path('languages', views.lang),
    #path('pdf',views.get_pdf,name = "pdf"),

    # path('add/<slug:field>',views.add_field,name = "add_field")
]
