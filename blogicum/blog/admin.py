from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .models import Post, Category, Location


class CustomUserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active"
    )
    list_filter = (
        "is_staff",
        "is_active"
    )
    search_fields = (
        "username",
        "email"
    )


class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_short_text",
        "pub_date"
    )

    def get_short_text(self, obj):
        text = obj.text or ""
        if len(text) > 100:
            return text[:100] + "…"
        return text
    
    get_short_text.short_description = "Текст"

    search_fields = (
        "title",
        "author",
        "location",
        "category"
    )
    list_filter = (
        "location",
        "category"
    )
    list_display_links = (
        "title",
    )


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_short_description"
    )

    def get_short_description(self, obj):
        description = obj.description or ""
        if len(description) > 100:
            return description [:100] + "…"
        return description

    get_short_description.short_description = "Описание"

    search_fields = (
        "title",
    )
    list_filter = (
        "slug",
    )

    list_display_links = (
            "title",
        )



class LocationModelAdmin(admin.ModelAdmin):
    list_display = (
            "name",
        )

User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Location, LocationModelAdmin)
