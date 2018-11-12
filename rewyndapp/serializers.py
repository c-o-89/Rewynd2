from rest_framework import serializers
from .models import Program, Episode, Tweet, Tweeter


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image_path',
        )
        model = Program

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'program',
            'season_num',
            'episode_num',
            'episode_name',
            'episode_len',
            'air_datetime',
        )
        model = Episode

class TweeterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'screen_name',
        )
        model = Tweeter

class TweetSerializer(serializers.ModelSerializer):
    tweeter = TweeterSerializer(read_only=True)
    class Meta:
        fields = (
            'tweeter',
            'text',
            'interval',
            'retweets',
            'favorites',
            'has_media',
            'media_type',
            'media_image_url',
        )
        model = Tweet
