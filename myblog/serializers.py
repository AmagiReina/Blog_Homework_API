from rest_framework import serializers
from .models import Work


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ('id',
                  'title',
                  'description',
                  'link',
                  'author_name',
                  'author_surname',
                  'active',
                  'created_at',
                  'updated_at')
