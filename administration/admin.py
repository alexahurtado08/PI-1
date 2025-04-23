from django.contrib import admin
from .models import Alert
from .models import Fotografia
from user.models import AuthorizedPersonnel
from administration.models import Computer

# Register your models here.
admin.site.register(Alert)
admin.site.register(Fotografia)
admin.site.register(AuthorizedPersonnel)
admin.site.register(Computer)
