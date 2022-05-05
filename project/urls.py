
from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.setsession),
    path('get/', views.getsession),
    path('del/', views.delsession),
]
