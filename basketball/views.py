from django.http import JsonResponse, HttpResponse
from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import BasketballEvent
from .serializers import BasketballEventSerializer

@api_view(['GET','POST'])
def getBasketballMatches(request):
    if request.method == 'GET':
        event_status = request.query_params.get('event_status')
        country = request.query_params.get('country')
        league = request.query_params.get('league')
        participant1 = request.query_params.get('team1')
        participant2 = request.query_params.get('team2')
        match_id = request.query_params.get('match_id')
        filters = {}
        if event_status:
            filters['event_status'] = event_status
        if participant1:
            filters['participant1'] = participant1
        if participant2:
            filters['participant2'] = participant2
        if match_id:
            filters['match_id'] = match_id
        basketball_matches = BasketballEvent.objects.filter(**filters)
        if country:
            basketball_matches = basketball_matches.filter(country__iregex=rf'.*{country}.*')
        if league:
            basketball_matches = basketball_matches.filter(league__iregex=rf'^{league}.*| {league}.*')
        serialized_basketball_matches = BasketballEventSerializer(basketball_matches, many=True)
        return Response(serialized_basketball_matches.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        content=JSONParser().parse(request)
        serializer=BasketballEventSerializer(content)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getBasketballMatchFromId(request,match_id):
    if request.method == 'GET':
        basketball_match=BasketballEvent.objects.filter(match_id=match_id)
        serialized_basketball_match=BasketballEventSerializer(basketball_match,many=True)
        return Response(serialized_basketball_match.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def createMatchesFromFile(request):
    file1 = open('basketball/basketballmatches.txt', 'r')
    lines = file1.readlines()

    for line in lines:
        try:
            match_array = line.strip().split("||")
            event = BasketballEvent(match_time=parse_datetime(match_array[0]), event_status='Scheduled',
                                  country=match_array[1],
                                  league=match_array[2], match_id=match_array[3], participant1=match_array[4],
                                  participant2=match_array[5],
                                  event_score='')
            event.save()
        except:
            pass

    return HttpResponse("success")




