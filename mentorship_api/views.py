#Views handle all incoming HTTP requests(eg. GET, POST, PUT, DELETE)

from django.shortcuts import render
from rest_framework import viewsets
from .models import Mentor, Mentee, MentorshipSession
from .serializers import MentorSerializer, MenteeSerializer, SessionSerializer

# ModelViewSet automatically provides all CRUD functionality
# ViewSet for Mentor model
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()           # Fetches all mentors from DB
    serializer_class = MentorSerializer       # Uses MentorSerializer to handle JSON conversion

# ViewSet for Mentee model
class MenteeViewSet(viewsets.ModelViewSet):
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer

# ViewSet for Session model
class SessionViewSet(viewsets.ModelViewSet):
    queryset = MentorshipSession.objects.all()
    serializer_class = SessionSerializer

