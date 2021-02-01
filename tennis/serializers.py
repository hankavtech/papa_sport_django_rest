from rest_framework import serializers

from .models import TennisEvent


class TennisEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TennisEvent
        fields = ['match_time','event_status','event_type','event_name','match_id','participant1','participant2','event_score']
