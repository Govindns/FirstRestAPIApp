from testapp.models import HydJobs,PuneJobs,BegrJobs
from testapp.api.serializers import Hydserializer
from rest_framework import viewsets

class HydCRUD(viewsets.ModelViewSet):
    queryset = HydJobs.objects.all()
    serializer_class = Hydserializer

