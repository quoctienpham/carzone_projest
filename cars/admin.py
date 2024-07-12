from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
	def thumbnail(self, object):
		return format_html('<img src="{}" width="50" style="border radius: 25px;" />'.format(object.car_photo.url))

	thumbnail.short_description = 'Car Image'
	list_display = ('id', 'car_title', 'thumbnail', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
	list_display_links = ('id', 'car_title', 'thumbnail',)
	list_editable = ('year', 'body_style', 'is_featured')
	list_display = ('id', 'car_title', 'thumbnail', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
	list_filter = ('city', 'model', 'body_style', 'fuel_type')
	search_fields = ('id', 'car_title', 'city', 'model', 'year', 'body_style', 'fuel_type')


admin.site.register(Car, CarAdmin)


