from django.http import QueryDict
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Client, Project, TimeLog
from api.serializers import ClientSerializer, ProjectSerializer, TimeLogSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, generics
from api.permissions import IsOwner
from rest_framework.response import Response
from api.utils import parseJsonDateToPythonDate


class ClientViewSet(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TimeLogViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = TimeLog.objects.all()
    serializer_class = TimeLogSerializer

    def get_queryset(self):
        filters: QueryDict = self.request.query_params
        date_from = filters.get('date_from')
        date_to = filters.get('date_to')
        query = TimeLog.objects.filter(owner=self.request.user)

        if date_from:
            date = parseJsonDateToPythonDate(date_from)
            if date:
                query = query.filter(date__gte=date)
    
        if date_to:
            date = parseJsonDateToPythonDate(date_from)
            if date:
                query = query.filter(date__gte=date)

        return query

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        client = project.client
        serializer.save(owner=self.request.user, client=client)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
