from django.contrib import admin
from django.urls import path, include
from pybo import views

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('polls/', include('polls.urls')),
    path('common/', include('common.urls'))
]
