from django.contrib import admin
from django.urls import path, include
from mysite.core import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('desmail/',views.desmail,name='desmail'),
    path('devmail/',views.devmail,name='devmail'),
    path('dmail/',views.dmail,name='dmail'),
    path('thanks',views.thanks,name='thanks'),
    


]
