from django.contrib import admin
from .models import Post
# Register your models here.
#so that they show up on the admin page

admin.site.register(Post)
