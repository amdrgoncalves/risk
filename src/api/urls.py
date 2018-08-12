from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/v1/risks/<int:pk>/',
        views.get_risk_type,
        name='get_risk_type'
    ),
    path(
        'api/v1/risks/',
        views.get_risks,
        name='get_risks'
    )
]
