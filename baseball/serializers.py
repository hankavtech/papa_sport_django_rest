from rest_framework import serializers

from .models import BaseballEvent


class BaseballEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseballEvent
        fields = ['match_time','event_status','country','league','match_id','participant1','participant2','event_score']