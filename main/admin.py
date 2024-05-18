from django.contrib import admin
from .models import Artwork, Comment

admin.site.register(Comment)

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'description', 'image', 'video')  # 비디오 필드 추가
    list_filter = ('section',)

admin.site.register(Artwork, ArtworkAdmin)