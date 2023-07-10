from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Student


def start_with_r(value):
    if value[0].lower() != "r":
        raise ValidationError("Name should start with r")

class StudentSerializer(serializers.Serializer):
    # 3. Validators
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        print("Before Instance: ", instance.city)
        instance.city = validated_data.get("city", instance.city)
        print("After Instance: ", instance.city)
        instance.save()
        return instance
    

    # 1. Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise ValidationError("Seat Full...")
        return value
    
    # 2. Object Level Validation
    def validate(self, data):
        print("Data: ", data)
        nm = data.get("name")
        ct = data.get("city")

        if nm.lower() == "rohit" and ct.lower() != 'ahmedabad':
            raise ValidationError("City must be Ahmedabad")
        return data