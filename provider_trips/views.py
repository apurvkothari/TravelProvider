from django.shortcuts import render

from rest_framework import generics, mixins
# Create your views here.
from .models import *
from .serializers import *

""" It will create Trip and show trip """
class TripsAPIView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin
                   ):

    serializer_class = TripModelSerializer
    queryset = TripModel.objects.all()
    lookup_field = 'trip_id'

    def get(self, request, trip_id=None):
        if id:
            return self.retrieve(request, trip_id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self, request, trip_id=None):
        return self.update(request, trip_id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def delete(self, request):
        return self.destroy(request, id)



