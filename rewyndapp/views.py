#orignal was: from django.shortcuts import render

from django.shortcuts import render
from .models import Program, Episode, Tweeter, Tweet
from .tasks import sdelta
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProgramSerializer, EpisodeSerializer, TweetSerializer
import datetime

def index(request):
    template = "rewyndapp/b_index.html"
    return render(request, template)

def programs_page(request):
    program_list = Program.objects.filter(is_active=True)
    template = "rewyndapp/c_programs_page.html"
    context = {
        "program_list": program_list,
    }
    return render(request, template, context)

def program_listview(request, program_id):
    episode_list = Program.objects.get(pk=program_id).episode_set.filter(is_active=True)
    program = Program.objects.get(pk=program_id)
    # use get_list_or_404 here
    w = map(lambda x: x.season_num, episode_list)
    seasons = list(set(w))
    template = "rewyndapp/c_episode_list.html"
    context = {
        "episode_list": episode_list,
        "seasons": seasons,
        "program": program,
    }
    return render(request, template, context)

def episode_page(request, id):
    tweet_list = Episode.objects.get(pk=id).tweet_set.filter(is_active=True, is_retweet=False, favorites__gte=3).order_by('interval')
    template = "rewyndapp/c_episode_page.html"
    context = {
        "tweet_list":tweet_list,
        "sdelta":sdelta.seconds*1000,
    }
    return render(request, template, context)

def about_page(request):
    template = "rewyndapp/c_about_page.html"
    return render(request, template)


class ProgramList(generics.ListAPIView):
    queryset = Program.objects.filter(is_active=True)
    serializer_class = ProgramSerializer

class EpisodeList(APIView):
    def get(self, request, program_id, format=None):
        queryset = Episode.objects.filter(program=program_id,is_active=True)
        serializer = EpisodeSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

class EpisodeTweets(APIView):
    def get(self, request, episode_id, format=None):
        queryset = Episode.objects.get(pk=episode_id).tweet_set.filter(is_active=True, is_retweet=False, favorites__gte=3).order_by('interval')
        serializer = TweetSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)
