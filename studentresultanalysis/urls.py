from django.contrib import admin
from django.urls import path,include


#Project of Church URLs ...
urlpatterns = [
    path('admin/', admin.site.urls),        #admin site urls.
    path('api/', include('app.urls'))       #Following the path of api site URLs
]