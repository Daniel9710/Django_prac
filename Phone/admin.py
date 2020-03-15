from django.contrib import admin
from .models import Text, Color

# Register your models here.


class TextAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tid', 'txt']}),
    ]
    list_display = ('tid', 'txt')


class ColorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['cid', 'color']}),
    ]
    list_display = ('cid', 'color', 'access_time', 'update_time')


admin.site.register(Text, TextAdmin)
admin.site.register(Color, ColorAdmin)
