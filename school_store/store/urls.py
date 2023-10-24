from . import views
from django.urls import path
app_name='store_app'
urlpatterns = [

    path('',views.stores,name='stores'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('logout',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('sub/',views.submitt,name='submitt'),

]