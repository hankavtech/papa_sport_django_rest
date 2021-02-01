from django.http import JsonResponse, HttpResponse
from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import TennisEvent
from .serializers import TennisEventSerializer

@api_view(['GET'])
def getTennisMatches(request):
    if request.method == 'GET':
        event_status = request.query_params.get('event_status')
        event_type = request.query_params.get('type')
        country = request.query_params.get('country')
        tournament = request.query_params.get('tournament')
        participant1 = request.query_params.get('team1')
        participant2 = request.query_params.get('team2')
        match_id = request.query_params.get('match_id')
        surface=request.query_params.get('surface')
        filters = {}
        if event_status:
            filters['event_status'] = event_status
        if tournament:
            filters['event_name']=tournament
        if participant1:
            filters['participant1'] = participant1
        if participant2:
            filters['participant2'] = participant2
        if match_id:
            filters['match_id'] = match_id
        tennis_matches = TennisEvent.objects.filter(**filters)
        if event_type:
            if event_type.lower() in ['men','women','doubles']:
                tennis_matches=tennis_matches.filter(event_type__iregex=rf'.* {event_type}.*')
        if country:
            tennis_matches=tennis_matches.filter(event_name__iregex=rf'.*({country}).*')
        if surface:
            tennis_matches = tennis_matches.filter(event_name__iregex=rf'.*,.*{surface}.*')

        serialized_tennis_matches=TennisEventSerializer(tennis_matches,many=True)
        return Response(serialized_tennis_matches.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        content=JSONParser().parse(request)
        serializer=TennisEventSerializer(content)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getTennisMatchFromId(request,match_id):
    if request.method == 'GET':
        tennis_match=TennisEvent.objects.filter(match_id=match_id)
        serialized_tennis_match=TennisEventSerializer(tennis_match,many=True)
        return Response(serialized_tennis_match.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        content=JSONParser().parse(request)
        serializer=TennisEventSerializer(content)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def createMatchesFromFile(request):
    file1 = open('tennis/tennismatches.txt', 'r')
    lines = file1.readlines()

    for line in lines:
        try:
            match_array = line.strip().split("||")
            event = TennisEvent(match_time=parse_datetime(match_array[0]), event_status='Scheduled',
                                  event_type=match_array[1],
                                  event_name=match_array[2], match_id=match_array[3], participant1=match_array[4],
                                  participant2=match_array[5],
                                  event_score='')
            event.save()
        except:
            pass

    return HttpResponse("success")






