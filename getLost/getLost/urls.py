"""getLost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from users.views import StripeAuthorizeCallbackView, StripeAuthorizeView, StripePage, StripePagePractice

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.request_register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),  # django builtin logout view


    path('profile/', user_views.profile, name='profile'),


    # path('dashboard/<str:pk>/', user_views.index, name='index'),
    path('dashboard/', user_views.index, name='index'),


    path('stripeaddress/', user_views.stripeAddress, name='stripe_address'),
    path('stripesettings/', user_views.stripeSettings, name='stripe_settings'),
    # path('stripe/', user_views.Stripe, name='stripe'),
    path('stripe/', StripePage.as_view(), name='stripe'),
    path('authorize/', StripeAuthorizeView.as_view(), name='authorize'),
    path('oauth/callback/', StripeAuthorizeCallbackView.as_view(),
         name='authorize_callback'),
    path('stripepractice/', StripePagePractice.as_view(), name='stripepractice'),

    # path('settings/<str:pk>/', user_views.settings, name='settings'),
    path('settings/', user_views.settingsFinal, name='settings_final'),
    
    # path('practice/<str:pk>/', user_views.practice, name='practice'),

    # path('index/<str:pk>/customerdetail/', user_views.reservation, name='customerdetail'),
    path('', user_views.hostel_portal, name='hostelportal'),
    # path('hostelportal/', user_views.hostel_portal, name='hostelportal'),
    path('contact/', user_views.contact, name='contact'),

    path('registerlogin/', user_views.register_login_view, name='registerlogin'),
    path('profileregister/', user_views.profile_register, name='profileregister'),
    path('profileregister2/', user_views.profile_register2, name='profileregister2'),
    path('profileregister3/', user_views.profile_register3, name='profileregister3'),
    
    path('message/', user_views.message_view, name='message'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="users/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_done.html"), name="password_reset_complete"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', include('webApp.urls')),

    path('api/', include('apis.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # path('api/', include('apis.urls', namespace='api')),


    path('i18n/', include('django.conf.urls.i18n')),
    path('currencies/', include('currencies.urls')),


]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "GetLOST Admin"
admin.site.site_title = "GetLOST Admin Portal"
admin.site.index_title = "Welcome to the GetLOST Portal"
