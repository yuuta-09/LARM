from django.contrib import admin
from .models import Button, Angle


class AngleInline(admin.TabularInline):
    model = Angle
    extra = 1  # 新規フォーム表示数


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    inlines = [AngleInline]


@admin.register(Angle)
class AngleAdmin(admin.ModelAdmin):
    list_display = ('id', 'button', 'joint_id', 'degree', 'speed', 'created_at', 'updated_at')
    list_filter = ('button', 'joint_id')