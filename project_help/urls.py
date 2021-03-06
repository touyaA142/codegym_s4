"""project_help URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#from django.urls import path
#from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from help_app import views

#from help_app.views import IndexView

#index_view = TemplateView.as_view(template_name="registration/index.html")
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path("", login_required(views.parent_assign), name="index"),
    path('addwork/', views.addwork, name="addwork"),
    path('newwork/', views.newwork, name="new_work"),
    path('child_tasklist/', views.child_page, name="child_page"),
    path('', include("django.contrib.auth.urls")),

    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name="activate"),





    #path('', views.top, name='top'),
    #path('login', views.login, name='login'),
    #path('register', views.register, name='register'),

    # path('parent_top', views.parent_top, name='parent_top'),
    path('parent_tasklist/', views.parent_tasklist, name='parent_tasklist'),
    path('parent_assign', views.parent_assign, name='parent_assign'),
    path('parent_taskregister/<int:pk>/', views.parent_taskregister, name='parent_taskregister'),
    path('parent_usersmanage', views.parent_usersmanage, name='parent_usersmanage'),
    path('parent_usersedit/<int:pk>/', views.parent_usersedit, name='parent_usersedit'),
    path('parent_users_delete/<int:pk>/', views.parent_users_delete, name='parent_users_delete'),
    path('parent_userslist', views.parent_userslist, name='parent_userslist'),
    path('parent_complete', views.parent_complete, name='parent_complete'),
    path('parent_task_delete/<int:pk>/', views.parent_task_delete, name='parent_task_delete'),
    path('parent_approval/', views.parent_approval, name='parent_approval'),
    path('parent_approval_on/<int:pk>/', views.parent_approval_on, name='parent_approval_on'),

    # path('child_top', views.child_top, name='child_top'),
    path('child_tasklist/<idName>', views.child_page_tab, name='child_tasklist_tab'),
    path('child_tasklist', views.child_page, name='child_tasklist'),
    path('child_complete', views.child_complete, name='child_complete'),
    path('child_history/<idName>', views.child_history_tab, name='child_history_tab'),
    path('child_history', views.child_history, name='child_history'),
    path('certification', views.certification, name='certification'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('help_app.urls')),
]
"""