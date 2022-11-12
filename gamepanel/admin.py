from django.contrib import admin

# Register your models here.
from . import models

class PanelAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Panel, PanelAdmin)
admin.site.register(models.NumberMaster, PanelAdmin)