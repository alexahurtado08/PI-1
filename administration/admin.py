from django.contrib import admin
from administration.models import Alert
from administration.models import Fotografia
from administration.models import AuthorizedPersonnel
from administration.models import Computer

# Register your models here.
admin.site.register(Alert)
admin.site.register(Fotografia)
admin.site.register(AuthorizedPersonnel)
admin.site.register(Computer)
