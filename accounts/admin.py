from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from embed_video.admin  import AdminVideoMixin

from .models import User


class VideoAdmin(AdminVideoMixin):
    pass


# admin.site.register(VideoAdmin)
admin.site.register(User, UserAdmin)
