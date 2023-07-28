from django.contrib import admin
from dotenv.main import with_warn_for_invalid_lines

from .models import Products , Comment



class ProductCommentInline(admin.TabularInline):
    model = Comment
    fialds = ["author", "active", "stars","body",]





@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "active",]
    inlines = [
        ProductCommentInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["product", "author", "active", "stars", "body"]

