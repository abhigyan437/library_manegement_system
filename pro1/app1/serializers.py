from .models import Books,Members
from rest_framework import serializers
from django.contrib.auth.models import User


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
