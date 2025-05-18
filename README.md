# Ex02 Django ORM Web Application
## Date: 09.5.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie  # Ensure this is the only import for Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'ref_no', 'rating', 'release_date', 'email')
    search_fields = ('title', 'email')
    list_filter = ('release_date',)

# Register the Movie model with the admin site
admin.site.register(Movie, MovieAdmin)

models.py

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

```


## OUTPUT

![alt text](<Screenshot 2025-05-18 135850.png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
