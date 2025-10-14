"""
DefaultRouter() automatically generates RESTful URLs for our ViewSets.
router.register() connects each ViewSet to a URL prefix (like /mentors/).
urlpatterns then includes these routes so Django recognizes them.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MentorViewSet, MenteeViewSet, SessionViewSet

router = DefaultRouter()
router.register(r'mentors', MentorViewSet)
router.register(r'mentees', MenteeViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
