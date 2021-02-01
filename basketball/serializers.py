from rest_framework import serializers

from .models import BasketballEvent


class BasketballEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BasketballEvent
        fields = ['match_time','event_status','country','league','match_id','participant1','participant2','event_score']