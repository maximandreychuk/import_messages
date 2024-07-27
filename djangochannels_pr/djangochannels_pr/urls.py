from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from emailmessages.views import LoginView, logout_user, messages_list, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages', messages_list,  name='messages_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
