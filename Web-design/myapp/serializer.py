from rest_framework import serializers
from .models import GeneBcells, GeneCD4, GeneNkcells, GeneCD8, GeneMonocytes


class GeneSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = GeneBcells
        fields = '__all__'