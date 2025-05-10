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

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'  # ✅ Includes name, email, and all other fields


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


from rest_framework import serializers
from .models import Complaints

class ComplaintDetailSerializer(serializers.ModelSerializer):
    category_label = serializers.CharField(source='category.name', read_only=True)  # ✅ Using 'category_label' instead of 'category_name'

    class Meta:
        model = Complaints
        fields = [
            'id', 'name', 'email', 'phone', 'address', 'city', 'latitude', 'longitude',
            'photo', 'description', 'status_code', 'created_at', 'aadhaar_photo',
            'date_of_incident', 'proof_of_work', 'user', 'category_label', 'assigned_officer'
        ]  # ✅ 'category' replaced with 'category_label'
