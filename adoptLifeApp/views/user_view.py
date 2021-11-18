from django.db.models.query import QuerySet
from django.template import response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer

class GetUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class DeleteUser(APIView):
    def delete(self, request, pk):
        queryset = User.objects.all().filter(pk=pk).first();
        serializer = UserSerializer(queryset)
        try:
            user_id = serializer.data['user_id']
            queryset.delete()
            response = {
                'response': 'User was successfully deleted',
                'id_user': user_id
            }
            return Response(data=response, status=status.HTTP_200_OK)
        except Exception:
            response = {
                'error': 'There is no user with the provided id'
            }
            return Response(data=response, status= status.HTTP_400_BAD_REQUEST)

class UpdateUser(APIView):
    def put(self, request, pk):
        queryset = User.objects.all().filter(pk=pk).first();
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserList(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data=data, status= status.HTTP_202_ACCEPTED)
        return Response(data=serializer._errors, status=status.HTTP_400_BAD_REQUEST)
