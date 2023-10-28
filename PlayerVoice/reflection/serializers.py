from django.utils import timezone
from rest_framework import serializers

from .models import Reflection, Journal
from player.models import Player
from player.serializers import PlayerSerializer

class ReflectionSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    player = PlayerSerializer()
    rating = serializers.IntegerField()
    match_description = serializers.CharField()
    comment = serializers.CharField(allow_null=True)
    created_at = serializers.DateTimeField()

    class Meta:
        model = Reflection
        fields = '__all__'


class CreateReflectionSerializer(serializers.Serializer):
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    rating = serializers.IntegerField()
    match_description = serializers.CharField()
    comment = serializers.CharField()

    class Meta:
        model = Reflection
        fields = ['player', 'rating', 'match_description', 'comment']


class JournalSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    player = PlayerSerializer()
    public = serializers.BooleanField()
    title = serializers.CharField()
    get_up = serializers.CharField()
    feelings = serializers.CharField()
    entry = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Journal
        fields = '__all__'


class CreateJournalSerializer(serializers.Serializer):
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    public = serializers.BooleanField()
    title = serializers.CharField()
    get_up = serializers.CharField()
    feelings = serializers.CharField()
    entry = serializers.CharField()

    class Meta:
        model = Journal
        fields = ['player', 'public', 'title', 'get_up', 'feelings', 'entry']
    
    
    ## TODO: 
    # reflection models, viewsets
    # moderation package
    # authorisation, login