from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.land, name='landing_page'),
    path('landingPage',views.landing, name='landing_page'),
    path('user', views.user_page, name='user_page'),
    path('admin', views.admin_page, name='admin_page'),
    path('redirectToUser',views.redirectToUser,name='redirectToUser'),
    path('redirectToAdmin',views.redirectToAdmin,name='redirectToAdmin'),
    path('redirectToLogin',views.redirectToLogin, name='RedirectToLogin'),
    path('Login',views.Login,name='UserLogin'),
    path('Register',views.Register,name='UserRegister'),
    path('NgoLink',views.NgoLink ,name='NgoLink'),
    path('SubmitNgoForm',views.SubmitNgoForm, name='SubmitNgoForm'),
    path('LoadEcommerce',views.LoadEcommerce,name='LoadEcommerce'),
    path('MachineLearn',views.MachineLearn,name='MachineLearn'),
    path('redirectToMl',views.redirectToMl,name='redirectToMl'),
    path('redirectToServices',views.redirectToServices, name='redirectToServices')

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 