from rest_framework import serializers
from todo.models import TODO

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = "__all__"
        