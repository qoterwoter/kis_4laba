from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('users',UserViewSet)
urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('landing', views.landing, name='landing'),
    # path('students/', views.StudentsView.as_view(), name='students'),
    # url(r'^students/$', views.students_list),
    # url(r'^students/(?P<id>[0-9]+)$', views.students_detail),
    # url(r'^staff/$',views.staff_list),
    # path('projects/', views.ProjectsView.as_view(), name='projects'),
    # path('users/', views.UserView.as_view(),name='users'),
    path ('',include(router.urls))
]