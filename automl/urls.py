from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='automl'
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('upload/',views.upload_file, name="upload"),
    path('chart/',views.chart, name="chart"),
    path('table/',views.table, name="table"),
    path('howdoi/',views.howdoi_view, name="howdoi"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
