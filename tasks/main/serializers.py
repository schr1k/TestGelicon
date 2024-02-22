from .models import Performer, Task
from rest_framework import serializers


class PerformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Performer
        fields = ['id', 'name']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    performer = serializers.PrimaryKeyRelatedField(queryset=Performer.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'comment', 'priority', 'performer', 'created_at']
