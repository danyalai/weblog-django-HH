from django.contrib import admin

from .models import Post


@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified')
    # ordering = ('status',)

# admin.site.register(Post, Postadmin)
