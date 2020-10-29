from django.contrib import admin

# Register your models here.
from crawler.models import ScrapyItem


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text',)


class ScrapyItemAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'data', 'date', 'url')


# Register your models here.
admin.site.register(ScrapyItem, ScrapyItemAdmin)
