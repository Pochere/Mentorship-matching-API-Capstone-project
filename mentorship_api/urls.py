from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MentorViewSet, MenteeViewSet, SessionViewSet, register_user, CustomAuthToken

# Router registrations
router = DefaultRouter()
router.register(r'mentors', MentorViewSet, basename='mentor')
router.register(r'mentees', MenteeViewSet, basename='mentee')
router.register(r'sessions', SessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', CustomAuthToken.as_view(), name='login'),
]
