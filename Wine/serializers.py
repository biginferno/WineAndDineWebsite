from rest_framework import serializers
from .models import Wine

class WineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wine
        fields = ('wine_name', 'wine_color', 'wine_varietal')
        # fields = '__all__'











