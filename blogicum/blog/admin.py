from django.contrib import admin

from .models import Post, Category, Location

admin.site.register(Category)
admin.site.register(Location)


class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "pub_date"
    )

    def text(self, obj):
        text = obj.description or ""
        if len(text) > 100:
            return text [:100] + "…"
        return text

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

# @admin.register()
# class CategoryModelAdmin(admin.ModelAdmin):

# @admin.register()
# class LocationModelAdmin(admin.ModelAdmin):