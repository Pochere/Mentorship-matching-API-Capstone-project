from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny


# User Registration Endpoint
@api_view(['POST'])
def register_user(request):
    """
    Register a new user (mentor or mentee)
    Required fields: username, password, email
    """
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Validation
    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Checks if username already exists
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    # Creates the user
    user = User.objects.create_user(username=username, password=password, email=email)

    # Creates a token for the user
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        'message': 'User registered successfully!',
        'token': token.key
    }, status=status.HTTP_201_CREATED)


# Login Endpoint (uses DRF’s built-in token system)
class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })
