from django.contrib import admin
from django.urls import include, path
 
urlpatterns = [
    path('', include('staticpages.urls')),
    path('movies/', include('movies.urls')), # adicionar esta linha
    path('admin/', admin.site.urls),
]   