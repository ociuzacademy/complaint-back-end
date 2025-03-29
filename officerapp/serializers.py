from rest_framework import serializers
from adminapp.models import Officer

class OfficerLoginSerializer(serializers.Serializer):
    officer_id = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        officer_id = data.get("officer_id")
        password = data.get("password")

        try:
            officer = Officer.objects.get(officer_id=officer_id)
        except Officer.DoesNotExist:
            raise serializers.ValidationError("Invalid officer ID or password.")

        if officer.Password != password:
            raise serializers.ValidationError("Invalid officer ID or password.")

        return officer



from rest_framework import serializers
from userapp.models import Complaints  # Adjust import as needed

class AssignedComplaintSerializer(serializers.ModelSerializer):
    user_fullname = serializers.CharField(source='user.fullname', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    assigned_officer_name = serializers.CharField(source='assigned_officer.Fullname', read_only=True)

    class Meta:
        model = Complaints
        fields = '__all__'

        
from rest_framework import serializers
from userapp.models import Complaints
from rest_framework import serializers
from userapp.models import Complaints


class UpdateComplaintStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = ['status_code', 'proof_of_work']
