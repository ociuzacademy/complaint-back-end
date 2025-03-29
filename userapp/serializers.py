from typing import __all__
from rest_framework import serializers
from .models import *  # Import your model
from rest_framework import serializers


class UserRegSerializers(serializers.ModelSerializer):
    class Meta:
        model = userreg
        fields = '__all__'

class loginSerializers(serializers.ModelSerializer):
    class Meta:
        model = userreg
        fields = ['email', 'password']

from rest_framework import serializers
from .models import Complaints

class ComplaintSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Complaints
        fields = [
            'id', 'name', 'email', 'phone', 'address', 'city', 'latitude', 'longitude', 
            'photo', 'description', 'status_code', 'created_at', 'aadhaar_photo', 
            'date_of_incident', 'proof_of_work', 'user', 'category_name', 'assigned_officer'
        ]


from rest_framework import serializers
from adminapp.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'rate', 'feedback','created_at']
