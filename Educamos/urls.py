"""Educamos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from Educamos.settings import local
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from school import views as school_views
from user import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/$', user_views.login_frontend, name='login'),

    url(r'salon/(?P<pk>[0-9])/$', school_views.classroom_view, name='classroom'),
    url(r'materia/(?P<pk>[0-9])/$', school_views.subject_view, name='subject'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/login/'}, name='logout'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)