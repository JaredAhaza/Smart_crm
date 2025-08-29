from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Register a new user with role assignment"""
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role', 'agent')  # default to agent
        
        # Validate required fields
        if not all([username, email, password]):
            return Response({
                'error': 'Username, email, and password are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return Response({
                'error': 'Username already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({
                'error': 'Password validation failed',
                'details': e.messages
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Assign role
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except Group.DoesNotExist:
            # If group doesn't exist, create it
            group = Group.objects.create(name=role)
            user.groups.add(group)
        
        return Response({
            'message': f'User {username} created successfully with role {role}',
            'user_id': user.id
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'error': 'Registration failed',
            'details': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
