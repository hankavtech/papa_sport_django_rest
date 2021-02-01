from rest_framework import serializers

from .models import FootballEvent


class FootballEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FootballEvent
        fields = ['match_time','event_status','country','league','match_id','participant1','participant2','event_score']