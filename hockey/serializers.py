from rest_framework import serializers

from .models import HockeyEvent


class HockeyEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyEvent
        fields = ['match_time','event_status','country','league','match_id','participant1','participant2','event_score']