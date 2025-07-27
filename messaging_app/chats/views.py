from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    ...
from .pagination import MessagePagination

class MessageViewSet(viewsets.ModelViewSet):
    pagination_class = MessagePagination
