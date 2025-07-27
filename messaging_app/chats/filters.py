import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.CharFilter(field_name='sender__username')
    receiver = django_filters.CharFilter(field_name='receiver__username')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'created_at']
