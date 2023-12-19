from django.contrib import admin
from django.utils.html import format_html

from .models import Team, Member

EMPTY_VALUE = '---пусто--'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'display_image_preview',
                    'team', 'time_create')
    search_fields = ('name', 'second_name', 'team')
    list_filter = ('name', 'second_name', 'team')
    empty_value_display = EMPTY_VALUE

    def display_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />',
                               obj.image.url)
        else:
            return 'No Image'

    display_image_preview.short_description = 'Изображение'
