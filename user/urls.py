from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from security import views as securityViews
from administration import views as adminViews
from user import views as userViews  # <- Aquí están tus vistas de login, registrar, etc.
from user.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userViews.home, name='home'),
    path('alerts/', adminViews.alerts, name='alerts'),
    path('personnel', userViews.personnel, name='personnel'),
    path('registrar/', userViews.registrar_usuario, name='registrar_usuario'),
    path('login/', userViews.login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('administrar-usuarios/', userViews.admin_users_view, name='admin_users'),
    path('administrar-usuarios/eliminar/<int:user_id>/', userViews.delete_user_view, name='delete_user'),

    # Manejo de archivos multimedia
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Extra para debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
