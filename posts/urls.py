from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.urls import path
# from posts.views import robots_txt


urlpatterns = [
    path('', views.index, name='index'),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata')
]

""" 
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    ...
    (r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)

    path('robots.txt',views.robots, name='robots', content_type="text/plain"),
 """