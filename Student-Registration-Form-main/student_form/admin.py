from django.contrib import admin
from .models import Details 


# admin.site.register(Details)

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','college_name','course')
    ordering = ('first_name',)
    search_fields =('first_name','last_name')