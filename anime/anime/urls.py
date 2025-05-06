from django.urls import path, include
from django.contrib import admin
<<<<<<< HEAD

urlpatterns = [
    path('api/', include("api.urls")), 
    path('admin/', admin.site.urls),
=======
from api.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('anime/achievements/', anime_achievements),
    path('anime/achievements/completed/', completed_achievements),
    path('anime/<str:tag_name>/<int:anime_id>/achievements/', anime_tag_achievements),
    path('api/achievements/',create_achievement),
>>>>>>> ca88e7910aa161598d49bac1b65aacb816dc4efd
]