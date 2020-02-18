from django.urls import path
from projects import views


app_name='projects'

urlpatterns = [
    path('', views.statuspage, name='status'),
    path('loaddata/', views.loaddata, name='loaddata'),
    path('edapage/', views.edapage, name='edapage'),
    path('automl/', views.automl,name='automl'),
    path('modelcreate/', views.modelcreate,name='modelcreate'),
    path('xai/', views.xai,name='xai'),
] 

