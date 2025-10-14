# This is a file Django REST Framework uses to define how models are converted to and from JSON.

from rest_framework import serializers
from .models import Mentor, Mentee, MentorshipSession

# Serializer for Mentor model
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'  # All includes all fields from the Mentor model


# Serializer for Mentee model
class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentee
        fields = '__all__'


# Serializer for Session model
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipSession
        fields = '__all__'
