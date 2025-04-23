from django.contrib import admin
from .models import Fotografia, Computer
from user.models import AuthorizedPersonnel

# Register your models here.
admin.site.register(Fotografia)
admin.site.register(AuthorizedPersonnel)
admin.site.register(Computer)

