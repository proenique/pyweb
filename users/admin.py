from django.contrib import admin

from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('avatar_tag','skill', 'phone')
    list_filter = ('user',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    list_per_page=50
    ordering = ('user',)
    prepopulated_fields = {'slug': ['user'],}

    class Media:
        js=("https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js",'js/script.js',)






class PostAdmin(admin.ModelAdmin):
    list_display=['image_tag','title','url','cat']
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50

    class Media:
        js=("https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js",'js/script.js',)

