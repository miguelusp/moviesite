from django.contrib import admin

from .models import Movie, Review, List, Provider,Category



admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(List)
admin.site.register(Provider) 
admin.site.register(Category)


