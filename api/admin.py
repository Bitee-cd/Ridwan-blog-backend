from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tags)
# admin.site.register(NewsLetter)

@admin.register(NewsLetter)
class NewsLetterAdmin(ImportExportModelAdmin):
    pass