from rest_framework import serializers
from main.models import Students



class StudentsSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'departament']
