from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import Http404
from users.models import Profile
from users import models
from . import serializers

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView 
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
# from .serializers import UserSerializer
# from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions

# from django.contrib.auth import get_user_model
# User = get_user_model()
# from users.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from requests.api import request

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/profile-list/',
        'Detail': '/profile-detail/<str:pk>/',
        'Create': '/profile-create/',
        'Update': '/profile-update/<str:pk>/',
        'Delete': '/profile-delete/<str:pk>/',
    }
    return Response(api_urls)

# @api_view(['GET'])
# def profileList(request):
#     profile = Profile.objects.all()
#     serializer = ProfileSerializer(profile, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def profileDetail(request, pk):
#     profile = Profile.objects.get(id=pk)
#     serializer = ProfileSerializer(profile, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def profileCreate(request):
#     serializer = ProfileSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def profileUpdate(request, pk):
#     profile = Profile.objects.get(id=pk)
#     serializer = ProfileSerializer(instance=profile, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def profileDelete(request, pk):
#     profile = Profile.objects.get(id=pk)
#     profile.delete()
#     return Response("Item Successfully Deleted!")


class UserListView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    # authentication_classes = (TokenAuthentication,)
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    ## USEFUL: used this when you want to make the creation of another model that a user does always connect to the account thats logged in. 
    # e.g if a user makes a reservation, it will connect to their instance thats logged in anf use that email
    # def perform_create(self, serializer):
    #     serializer.save(email=self.request.user)

class UserCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAdminUser]
    # permission_classes = [IsAdminUser]
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.AllowAny]


class ChangePasswordView(generics.UpdateAPIView):

    queryset = models.User.objects.all()
    # permission_classes = (IsAuthenticated,)
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ChangePasswordSerializer

class HostelProfileListView(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.HostelProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HostelRoomDetailListView(generics.ListCreateAPIView):
    queryset = models.RoomDetail.objects.all()
    serializer_class = serializers.HostelRoomDetailSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





class HostelRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    # lookup_field = "avaliability"
    queryset = models.RoomDetail.objects.all()
    serializer_class = serializers.HostelRoomDetailSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]






class HostelProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.HostelProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TravelerProfileListView(generics.ListCreateAPIView):
    queryset = models.CustomerProfile.objects.all()
    serializer_class = serializers.TravelerProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TravelerStripeListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomerProfile.objects.all()
    serializer_class = serializers.TravelerStripeSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TravelerProfileCreateView(generics.CreateAPIView):
    serializer_class = serializers.TravelerProfileSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAdminUser]

class TravelerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomerProfile.objects.all()
    serializer_class = serializers.TravelerProfileSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    # def get_queryset(self):
    #     profile = self.request.user
    #     print("the user is  " + profile)
    #     return super().get_queryset()

    # def update(self, request, *args, **kwargs):
    #     print("WE HERE - view")
    #     serializer = self.serializer_class(
    #         request.user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class ReservationListView(generics.ListCreateAPIView):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReservationCreateView(generics.CreateAPIView):
    serializer_class = serializers.ReservationSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAdminUser]

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

# class UserListView(APIView):
#     """
#     API View to create or get a list of all the registered
#     users. GET request returns the registered users whereas
#     a POST request allows to create a new user.
#     """
#     permission_classes = [IsAdminUser]

#     def get(self, format=None):
#         users = models.User.objects.all()
#         serializer = serializers.UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = serializers.UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             {
#                 "error": True,
#                 "error_msg": serializer.error_messages,
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )


# class UserDetailView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

#     def get_object(self, pk):
#         try:
#             return models.User.objects.get(pk=pk)
#         except models.User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = serializers.UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = serializers.UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
