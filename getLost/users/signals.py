from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from users import models
# from celery.schedules import crontab
# from celery.task import periodic_task
from django.utils import timezone


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
      Token.objects.create(user=instance)
    
    
for user in models.User.objects.all():
    Token.objects.get_or_create(user=user)

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def build_profile_on_user_creation(sender, instance, created, **kwargs):
  if created:
    if instance.account_type == "2":
      profile = Profile(user=instance)
      profile.save()
    else:
      print("it is not true")

#####################################################################################################################
######### HAD TO COMMENT OUT SO SERIALIZER CAN WORK BY CREATING USER AND CUSTOMER PROFILE AT THE SAME TIME WITHOUT CALLING 
######### SIGNAL TO CREATE USER AS WELL, MAKING TWO USERS WHICH RETURNS ERROR
#####################################################################################################################
# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile_customer')
# def build_customer_profile_on_user_creation(sender, instance, created, **kwargs):
#   if created:
#     print(instance.pk)
#     print(user.pk)
#     if instance.account_type == "3":
#       profile = CustomerProfile(user=instance)
#       profile.save()
#     else:
#       print("it is not true")
  

@receiver(post_save, sender=Profile, dispatch_uid='save_new_profile_roomdetail')
def build_roomdetail_on_profile_creation(sender, instance, created, **kwargs):
  if created:
    roomdetail = RoomDetail(hostel=instance)
    roomdetail.save()


