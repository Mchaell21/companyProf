from django.urls import path
from logAuth import views

urlpatterns = [
    path('login/', views.logPage, name='loginPage'),
    path('session_log/', views.sess_login, name='sesLog'),
    path('logout/', views.logout_page, name='logout'),
    path('homeadmin/', views.home, name='homePageAdmin'),
    path('contact list/', views.contactList, name='contactListPage'),
    path('contact/delete/<slug:slug>/', views.deleteContact, name='deleteContact'),
]