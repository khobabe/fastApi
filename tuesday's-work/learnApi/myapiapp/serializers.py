from rest_framework import serializers
from myapiapp.models import StudentInformation

# create serializers here:
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = StudentInformation
        fields = "__all__"
        