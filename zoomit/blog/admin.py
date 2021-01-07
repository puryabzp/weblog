from django.contrib import admin
from .models import Post, Category, Comment, PostSetting, CommentLike
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class ChildrenItemInline(admin.TabularInline):
    model = Category
    fields = ("title", "slug")
    extra = 1
    show_change_link = True


class PostItemInline(admin.TabularInline):
    model = Post
    fields = ("title", "slug")
    extra = 1
    show_change_link = True


class PostSettingInline(admin.TabularInline):
    model = PostSetting


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("slug", "title")
    list_filter = ("parent",)
    list_display = ("slug", "title", "parent")
    inlines = [
        ChildrenItemInline,
        PostItemInline
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "slug")
    list_display = ('title', 'content', 'create_at', "update_at", 'draft', "author")
    list_filter = ("draft", "title", "category", "author")
    prepopulated_fields = {"slug": ("title",), }
    date_hierarchy = "publish_time"
    inlines = [
        PostSettingInline
    ]

    def set_published(self, request, queryset):
        queryset.update(draft=False)

    set_published.short_description = "Mark selected post as published"
    actions = ["set_published"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_display = ('post', 'author', 'is_confirmed', "like_count", 'dislike_count')
    list_filter = ('post', 'author', 'is_confirmed')
    date_hierarchy = "create_at"


# Register your models here.
admin.site.register(CommentLike)
