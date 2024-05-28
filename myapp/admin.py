from django.contrib import admin
from .models import c_user
# Register your models here.
from django.utils.html import format_html

class user_Admin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.c_image:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.c_image.url))
        else:
            return 'No Image'
    image_tag.short_description = 'Image'
    list_display = ["c_name", "image_tag","c_email","c_password","c_encrpted"]
admin.site.register(c_user,user_Admin)
