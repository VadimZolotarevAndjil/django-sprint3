from django.contrib import admin

from .models import Post, Category, Location

admin.site.register(Location)


class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_short_text",  # Указываем имя метода
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

admin.site.register(Post, PostModelAdmin) 


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
admin.site.register(Category, CategoryModelAdmin)


# class LocationModelAdmin(admin.ModelAdmin):