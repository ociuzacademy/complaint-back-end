from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OfficerLoginSerializer
from adminapp.models import Officer

class OfficerLoginView(APIView):
    serializer_class = OfficerLoginSerializer  # ✅ Explicitly set serializer class

    def post(self, request):
        serializer = self.serializer_class(data=request.data)  # ✅ Use self.serializer_class
        if serializer.is_valid():
            officer = serializer.validated_data
            return Response({"message": "Login successful", "id":officer.id,"officer_id": officer.officer_id,"password":officer.Password}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.models import Complaints
from .serializers import AssignedComplaintSerializer
from django.shortcuts import get_object_or_404
from adminapp.models import Officer  # Adjust import as needed
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.models import Complaints
from .serializers import AssignedComplaintSerializer
from django.shortcuts import get_object_or_404
from adminapp.models import Officer  # Adjust import as needed

class AssignedComplaintsView(APIView):

    def get(self, request, officer_id):
        officer = get_object_or_404(Officer, officer_id=officer_id)
        complaints = Complaints.objects.filter(assigned_officer=officer)

        if not complaints.exists():
            return Response({"message": "No work assigned"}, status=200)

        serializer = AssignedComplaintSerializer(complaints, many=True)
        return Response(serializer.data)


        
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from userapp.models import Complaints
from .serializers import UpdateComplaintStatusSerializer

class ComplaintStatusViewSet(viewsets.ViewSet):

    def partial_update(self, request, pk=None):
        """
        Partially update complaint status and/or proof_of_work (image upload).
        Allows updating only one field or both.
        """
        complaint = get_object_or_404(Complaints, id=pk)

        if not request.data:
            return Response({"error": "No data provided for update"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UpdateComplaintStatusSerializer(complaint, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Complaint status updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
