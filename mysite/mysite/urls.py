from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from mysite import views
from .views import GeneratePdf

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.home, name='home'),
    path('generatePaper', views.generatePaper,name='generatePaper'),
    path('loginapp/', include('loginapp.urls')),
    path('delete',views.delete, name='delete'),
    path('deleteQuestion',views.deleteQuestion, name='deleteQuestion'),
    path('deleteSuccess',views.deleteSuccess, name='deleteSuccess'),
    path('pdf/paper.html', GeneratePdf.as_view()),
    path('intermediate.html',views.intermediate, name='intermediate'),
    path('intermediate2.html',views.intermediate2, name='intermediate2'),
    path('loginpage', views.loginpage, name="lpage"),
    path('login',views.view_login, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('index', views.index, name='index'),
]