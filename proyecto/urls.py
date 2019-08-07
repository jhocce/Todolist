from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('Apps.user.url')),
    path('user/', include(('Apps.user.url', 'users'), namespace="user")),
    path('tareas/', include(('Apps.tareas.url', 'tareas'), namespace="tareas")),

]


