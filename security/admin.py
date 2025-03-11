from django.contrib import admin
from .models import Alert
from .models import Fotografia 
from .models import AuthorizedPersonnel

# Register your models here.
admin.site.register(Alert)
admin.site.register(Fotografia)
admin.site.register(AuthorizedPersonnel)