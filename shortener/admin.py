from django.contrib import admin
from shortener.models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass

# Register your models here.
