from rest_framework import serializers

from .models import CricketEvent


class CricketEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CricketEvent
        fields = ['match_time','event_status','country','league','match_id','participant1','participant2','event_score']