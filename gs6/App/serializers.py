from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # 3. Validators
    def start_with_r(value):
        if value[0].lower() !='r':
            raise ValidationError("Name should be start with r")
    
    name = serializers.CharField(validators=[start_with_r]) 
    # name = serializers.CharField(read_only=True) # Explicitly pass name
    class Meta:
        model = Student
        # fields = ["id", "name", "roll", "city"]
        fields = "__all__"
        # exclude = ["name"]
        # read_only_fields = ["name", "roll"]
        # extra_kwargs = {"name":{"read_only":True}}


    
    # 1. Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise ValidationError("Seat Full...")
        return value
    
    # # 2. Object Level Validation
    def validate(self, data):
        print("Data: ", data)
        nm = data.get("name")
        ct = data.get("city")

        if nm.lower() == "rohit" and ct.lower() != 'ahmedabad':
            raise ValidationError("City must be Ahmedabad")
        return data
    