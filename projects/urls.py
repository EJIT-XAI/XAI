from django.urls import path
from projects import views




urlpatterns = [
    path('', views.statuspage),
    path('dataload/', views.dataload),
    path('edapage/', views.edapage),
    path('automl/', views.automl),
    path('modelcreate/', views.modelcreate),
    path('xai/', views.xai),
] 

