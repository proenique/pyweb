from django.contrib import admin
from .models import Service, Plan, Product
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    list_display = ('name',)
    list_filter = ('name',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('name',)
    prepopulated_fields = {'slug': ['name'],}


admin.site.register(Plan)
admin.site.register(Product)