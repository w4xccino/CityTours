from django.contrib import admin
from .models import Lugar

# Register your models here.
class LugarAdmin(admin.ModelAdmin):
  list_display = ('nombre','descripcion')
  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()


admin.site.register(Lugar,LugarAdmin)
