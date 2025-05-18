from django.db import models
from django.contrib import admin

class Movie(models.Model):
    title = models.CharField(max_length=100)  # Increased max_length for movie titles
    ref_no = models.AutoField(primary_key=True)  # AutoField for unique reference number
    rating = models.FloatField()  # Changed from Percentage to rating for clarity
    release_date = models.DateField()  # Changed DoB to release_date for movies
    email = models.EmailField()  # Assuming this is for the user who added the movie

    def __str__(self):
        return self.title  # String representation for the admin interface

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'ref_no', 'rating', 'release_date', 'email')  # Updated field names


