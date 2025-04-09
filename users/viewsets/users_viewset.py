from rest_framework import viewsets, permissions
from users.models import Users
from users.serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Users.objects.all()

    def perform_create(self, serializer):
        serializer.save()