from django.contrib import admin
from .models import Movie  # Ensure this is the only import for Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'ref_no', 'rating', 'release_date', 'email')
    search_fields = ('title', 'email')
    list_filter = ('release_date',)

# Register the Movie model with the admin site
admin.site.register(Movie, MovieAdmin)
