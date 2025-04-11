from rest_framework import viewsets, permissions
from users.models import Users
from users.serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        return Users.objects.all()

    def perform_create(self, serializer):
        serializer.save()