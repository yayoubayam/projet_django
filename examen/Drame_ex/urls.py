from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    # path('index2',views.index2, name="index2"),
    path('connexion/',views.connexion,name="connexion"),
    path('update/<int:pk>/',views.update, name="update"),
    path('delete/<int:pk>/',views.delete, name="delete"),
    path('register/', views.register, name='register'),
    path('creertache/',views.ajoutertache, name='creation'),
    path('ajouteruser/',views.utilisateur, name='inscription'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)