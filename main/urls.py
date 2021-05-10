from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home, name="home"),
    path('semester/<int:id>/', views.subjects, name ="subject"),
    path('subject/<int:id>/', views.chapters, name="chapter"),
    path('resource/<int:id>/', views.resources, name="resource"),
]
