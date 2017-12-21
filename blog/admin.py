from django.contrib import admin

# Register your models here.
from blog.models import article, comments

admin.site.register(article)
admin.site.register(comments)