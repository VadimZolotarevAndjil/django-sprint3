from django.contrib import admin

from .models import Post, Category, Location

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)

@admin.register()
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_description"
    )

    def short_description(self, obj):
        text = obj.description or ""
        if len(text) > 100:
            return text [:100] + "…"
        return text

    list_editable = (

    )

@admin.register()
class CategoryModelAdmin(admin.ModelAdmin):

@admin.register()
class LocationModelAdmin(admin.ModelAdmin):