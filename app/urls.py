from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', views.cars_view, name='cars_list'),
    path('cars/<int:car_id>/', views.car_details, name='car_details'),
    path('new_car/', views.new_car_view, name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)