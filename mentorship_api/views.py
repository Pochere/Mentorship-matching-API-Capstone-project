from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Mentor, Mentee, MentorshipSession
from .serializers import MentorSerializer, MenteeSerializer, SessionSerializer

# -----------------------
# Model viewsets (your CRUD endpoints)
# -----------------------
# -----------------------
# Model viewsets (your CRUD endpoints)
# -----------------------
class MentorViewSet(viewsets.ModelViewSet):
    serializer_class = MentorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return mentors linked to the logged-in user
        return Mentor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach the logged-in user as this mentor
        serializer.save(user=self.request.user)


class MenteeViewSet(viewsets.ModelViewSet):
    serializer_class = MenteeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mentee.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Shows only sessions related to the logged-in user
        if hasattr(user, 'mentor'):
            return MentorshipSession.objects.filter(mentor=user.mentor)
        elif hasattr(user, 'mentee'):
            return MentorshipSession.objects.filter(mentee=user.mentee)
        return MentorshipSession.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'mentor'):
            serializer.save(mentor=user.mentor)
        elif hasattr(user, 'mentee'):
            serializer.save(mentee=user.mentee)

# Auth endpoints (register & login)

# Public: registers a new user and return a token
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Register a new user. Required fields in JSON body: username, password, email (email optional).
    Returns: { "message": "...", "token": "<token>" }
    """
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    # Basic validation
    if not username or not password:
        return Response({'error': 'username and password are required.'},
                        status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'username already exists.'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'message': 'User registered successfully',
        'token': token.key,
        'user_id': user.id,
        'username': user.username
    }, status=status.HTTP_201_CREATED)


# Login view using DRF's ObtainAuthToken, but respond with token + basic user info
class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # uses serializer from ObtainAuthToken (validates username/password)
        response = super().post(request, *args, **kwargs)
        token_key = response.data.get('token')
        token = Token.objects.get(key=token_key)
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })
