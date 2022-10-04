
from django.contrib import admin
from .models import Brand

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Brand'''

    list_display = ('user',)
    list_filter = ('user',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('user',)
    prepopulated_fields = {'slug': ['user'],}