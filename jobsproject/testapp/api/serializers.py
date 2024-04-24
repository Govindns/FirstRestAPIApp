from rest_framework.serializers import Serializer,ModelSerializer
from testapp.models import HydJobs

class Hydserializer(ModelSerializer):
    class Meta:
        model=HydJobs
        fields='__all__'
