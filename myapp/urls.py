from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
    path('<int:pk>', views.detail,name="detail"),
    path('ratelimit/', views.APIrateLimit),
    path('featureflag/', views.feature_flag_view),
    path('logs/', views.audit_log_view, name='audit_logs'),
    path('create-item/', views.create_item, name='create_item'),
    path('health-check/', views.health_check, name='health_check'),
]