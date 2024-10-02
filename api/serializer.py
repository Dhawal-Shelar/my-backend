from .models import *
from rest_framework.serializers import ModelSerializer


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = "__all__"