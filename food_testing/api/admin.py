
from django.contrib import admin
from .models import FoodItem, FoodData
from import_export.admin import ImportExportMixin

#Code for csv 
class FoodDataAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name' , 'humidity', 'methane', 'temperature' , 'Quality']

class FoodItemAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['item', 'data']
# Register your models here.

#admin.site.register(FoodData)

admin.site.register(FoodItem , FoodItemAdmin)
admin.site.register(FoodData, FoodDataAdmin)
