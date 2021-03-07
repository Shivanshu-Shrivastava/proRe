from django.urls import path
from . import views

urlpatterns = [
    path('site.html', views.render_page, name='res'),
    path('getinput.html', views.get_input, name='input'),
    path('Education.html', views.edu, name='Education'),
    path('work.html', views.wor, name='work'),
    path('position.html', views.pos, name='position'),
    path('project.html', views.pro, name='project'),
    path('academic.html', views.aca, name='academic'),
    path('extra.html', views.ext, name='extra'),
    path('additi.html', views.add, name='additi'),

    # path('add/<slug:field>',views.add_field,name = "add_field")
]