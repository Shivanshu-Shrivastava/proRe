from django.urls import path
from . import views

urlpatterns = [
    path('site', views.render_page, name='res'),
    path('start', views.personal_det),
    path('getinput', views.get_input, name='input'),
    path('getinput/<int:id>/', views.getipdel),
    path('getinput/edit/<int:id>',views.getipedit),
    # path('getinput/<int:id>', views.getdel),
    # path('getinput/edit/<int:id>', views.getedit),
    path('education', views.edu, name='Education'),
    path('education/<int:id>',views.edudel),
    path('education/edit/<int:id>',views.eduedit),
    #path('education/<slug:edit>/<int:id>',views.edu),
    path('work', views.wor, name='work'),
    path('work/<int:id>',views.delwork),
    path('work/edit/<int:id>',views.editwork),
    path('skills',views.skill),
    path('skills/<int:id>',views.delskill),
    path('skills/edit/<int:id>',views.editskill),
    #path('position.html', views.pos, name='position'),
    path('project', views.pro, name='project'),
    path('project/<int:id>',views.delpro),
    path('project/edit/<int:id>',views.editpro),
    path('extra', views.ext, name='academic'),
    path('extra/<int:id>',views.delext),
    path('extra/edit/<int:id>',views.editext),
    #path('hw',views.HW.render_hw)
    #path('languages', views.lang),
    #path('pdf',views.get_pdf,name = "pdf"),

    # path('add/<slug:field>',views.add_field,name = "add_field")
]
