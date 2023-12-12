from django.urls import path

from .views import GetTokenView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_view'),
    path('get-token/', GetTokenView.as_view(), name='get-token_view'),
]