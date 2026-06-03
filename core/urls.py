from django.contrib import admin
from django.urls import path
# Эскиси: from .views import home
# Жаңысы:
from courses.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), 
]