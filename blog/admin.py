from django.contrib import admin
from .models import Author, Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields=('body')
    list_display = ('title','date_created','date_updated','author')


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
