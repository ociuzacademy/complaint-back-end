from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# from .models import Complaint
from .serializers import UserRegSerializers, loginSerializers
from .models import userreg
from rest_framework import viewsets, permissions
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# from .serializers import ComplaintSerializer


class UserCreateView(APIView):
    serializer_class = UserRegSerializers  # ✅ Explicitly define serializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            success_response = {
                "message": "User created successfully!",
                "role": "user",
                "data": serializer.data
            }
            return Response(success_response, status=status.HTTP_201_CREATED)

        error_response = {
            "message": "User creation failed. Please check the input.",
            "errors": serializer.errors
        }
        return Response(error_response, status=status.HTTP_400_BAD_REQUEST)


class loginCreateView(APIView):
    serializer_class = loginSerializers  # ✅ Explicitly define serializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']

            # Authenticate user
            user = userreg.objects.filter(email=email).first()
            if user and user.password == password:
                return Response({'message': 'User Login successful','id':user.id,'role': 'user','email':user.email,'password':user.password,'username':user.fullname}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Complaints
from .serializers import ComplaintSerializer
class UserComplaintViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling user complaints.
    """
    queryset = Complaints.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [AllowAny]

    
@api_view(['GET'])
def list_complaints_by_user(request, user_id):
    """
    List complaints for a specific user.
    """
    complaints = Complaints.objects.filter(user__id=user_id) 
    if not complaints.exists():
        return Response({"message": "No complaints found for this user."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def retrieve_complaint(request, pk):
    """
    Retrieve a single complaint by ID.
    """
    try:
        complaint = Complaints.objects.get(pk=pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)
    except Complaints.DoesNotExist:
        return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_complaint(request, pk):
    """
    Delete a complaint by ID.
    """
    try:
        complaint = Complaints.objects.get(pk=pk)
        complaint.delete()
        return Response({"message": "Complaint deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    except Complaints.DoesNotExist:
        return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)


from rest_framework.generics import ListAPIView
from adminapp.models import Category
from .serializers import CategorySerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    """ViewSet for managing feedback"""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
