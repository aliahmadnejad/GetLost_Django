# from . import views

# from django.urls import include, path
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.urls import path, include
# from .views import UserRecordView
# from rest_framework.authtoken import views
from . import views
 
# app_name = 'api'
urlpatterns = [
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # path('user/', UserRecordView.as_view(), name='users'),
    # path('', views.UserRecordView, name="api-overview"),
    path('', views.apiOverview, name="api-overview"),
    # path('profile-list/', views.profileList, name="profile-list"),
    # path('profile-detail/<str:pk>', views.profileDetail, name="profile-detail"),
    # path('profile-create/', views.profileCreate, name="profile-create"),
    # path('profile-update/<str:pk>', views.profileUpdate, name="profile-update"),
    # path('profile-delete/<str:pk>', views.profileDelete, name="profile-delete"),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', views.UserListView.as_view()),
    path('users/register/', views.UserCreateView.as_view()),
    path('users/<str:pk>/', views.UserDetailView.as_view()),
    path('change_password/<str:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    path('hostelprofile/', views.HostelProfileListView.as_view()),
    path('hostelroomdetail/', views.HostelRoomDetailListView.as_view()), 
    
    path('hostelroomdetail/<str:pk>/', views.HostelRoomDetailView.as_view()),
    path('hostelprofile/<str:pk>/', views.HostelProfileDetailView.as_view()),
    path('travelerprofile/', views.TravelerProfileListView.as_view()),
    path('travelerprofile/register/', views.TravelerProfileCreateView.as_view()),
    path('travelerprofile/<str:pk>/', views.TravelerProfileDetailView.as_view()),
    path('travelerstripe/<str:pk>/', views.TravelerStripeListView.as_view()),

    path('reservations/', views.ReservationListView.as_view()),
    path('reservations/create/', views.ReservationCreateView.as_view()),
    path('reservations/<str:pk>/', views.ReservationDetailView.as_view()),

    path('api-token-auth/', views.CustomAuthToken.as_view()),


]
