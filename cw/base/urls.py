from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path('', views.index,name= "index"),
    path('home/', views.home,name= "home"),
    path('DC/', views.DC,name= "DC"),
    path('Faculty/', views.Faculty,name= "Faculty"),
    path('Campus/', views.Campus,name= "Campus"),
    path('Students/', views.Student,name= "Student"),
    path('Academic/', views.Academic,name= "Academic"),
    path('principledesk/', views.principledesk,name= "principledesk"),
    path('Contactus/', views.Contactus,name= "Contactus"),
    path('Grievance/', views.Grievance,name= "Grievance"),
    path('index/', views.index,name='index'),
    path('basic/', views.basic,name='basic'),
    path('hostel/', views.hostel,name='hostel'),
    path('library/', views.library,name='library'),
    path('lab/', views.lab,name='lab'),
    path('games/', views.games,name='games'),
    path('infrastructure/', views.infrastructure,name='infrastructure'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('gallery/',views.gallery,name='gallery'),
    
]