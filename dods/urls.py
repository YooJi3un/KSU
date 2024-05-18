from django.contrib import admin
from django.urls import path
from main.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('원하는URL/', 함수명),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
