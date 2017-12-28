from django.contrib import admin
from .models import Students_info
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['name','university','major','english_score','math_score','political_score','major_score','total_score','rank']
admin.site.register(Students_info,PostAdmin)