from typing import Tuple

from django.contrib import admin
from .models import Category
from .models import Post,BlogComment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("imageTag", "title", "description", "url", "add_date")
    search_fields = ("title",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("imageTag", "title", "cat")
    search_fields = ("title",)
    list_filter = ("cat",)
    list_per_page = 35

    class Media:
        js = ("https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js","js/script.js",)

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment")

admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
admin.site.register(Category, CategoryAdmin)
