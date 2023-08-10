from django.contrib import admin
from .models import PostModel

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')

admin.site.register(PostModel, PostModelAdmin)