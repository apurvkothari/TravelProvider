from rest_framework import serializers

from.models import TripModel

class TripModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripModel
        fields = '__all__'
#        fields = ['id', 'account_name', 'users', 'created']