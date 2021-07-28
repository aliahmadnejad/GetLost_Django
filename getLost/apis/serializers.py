from rest_framework import serializers
# from users.models import Profile
from users import models
from rest_framework.validators import UniqueTogetherValidator
from django_countries import Countries
from users.models import CustomerProfile
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
import six
from django.utils.encoding import force_text
# from django.contrib.auth.models import User
from django_countries.serializers import CountryFieldMixin
import stripe
from getLost import settings


stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = "2020-08-27"
        
class SerializableCountryField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super(SerializableCountryField, self).__init__(choices=Countries())

    def to_representation(self, value):
        if value in ('', None):
            # normally here it would return value. which is Country(u'') and not serialiable
            return ''
            # return value
            # return force_text(value)
        return super(SerializableCountryField, self).to_representation(value)
        # return self.choice_strings_to_values[six.text_type(value)]
        # return force_text(super(SerializableCountryField, self).to_representation(value))

class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = models.User
        # fields = '__all__'
        fields = (
                    'id',
                    'username',
                    'email',
                    'password',
                    'account_type',
                )
        read_only_field = ('id',)
        # extra_kwargs = {
        #     'username': {
        #         'validators': [UnicodeUsernameValidator()],
        #     },
        #     'email': {
        #         'validators': [EmailValidator]
        #     }
        # }

    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     user_id = self.context['request'].user
    #     print("the input value is " , value)
    #     print(user.id)
    #     print(user.username)
    #     print(models.User.objects.filter(email=value).exclude(
    #         pk=user.pk).exists())

    #     if models.User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use.33"})
    #     return value

    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if models.User.objects.exclude(pk=user.pk).filter(username=value).exists():
    #         raise serializers.ValidationError(
    #             {"username": "This username is already in use.33"})
    #     return value

    # def create(self, validated_data):
    #             user = models.User.objects.create_user(**validated_data)
    #             return user
    # extra_kwargs = {'username': {'required': False}, 'email': {
    #     'required': False}, 'password': {'required': False}, }



    def create(self, validated_data):
        # user = models.User(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        #     account_type=validated_data['account_type']
        # )
        user = models.User(
            email=validated_data['email'],
            username=validated_data['email'],
            account_type=validated_data['account_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        print("WE HERE - user")
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        # instance.username = validated_data.get('email', instance.username)
        instance.save()
        return instance
    

    # validators = [
    #     UniqueTogetherValidator(
    #         queryset=models.User.objects.all(),
    #         fields=['username', 'email']
    #     )
    # ]

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class TravelerStripeSerializer(serializers.ModelSerializer):
    ephemeral_key = serializers.SerializerMethodField()
    class Meta:
        model = models.CustomerProfile
        fields = (
        # 'id', 'user', 'stripe_id',
        'ephemeral_key',)
        # read_only_fields = ('ephemeral_key',)
    
    def get_ephemeral_key(self, obj):
        key = stripe.EphemeralKey.create(
            customer=obj.stripe_id, stripe_version=stripe.api_version)
        print(key)
        return key
        
class TravelerProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user = UserSerializer(required=True)
    # country = SerializableCountryField(allow_blank=True, required=False, allow_null=True, default="US")
    
    print(models.CustomerProfile.stripe_id)
#    ephemeral_key = serializers.SerializerMethodField()
    

    class Meta:
        model = models.CustomerProfile
        fields = ('id', 'user', 'first_name', 'middle_name', 'last_name', 
        'country', 
        'phone', 'emergency_contact_name', 'emergency_contact_relation' , 'emergency_contact_email', 'emergency_contact_phone', 'stripe_id', #'ephemeral_key'
        )
        read_only_fields = ('id', 'stripe_id',
#         'ephemeral_key'
         )
        # optional_fields = ['country',]
        # extra_kwargs = {"country": {"required": False, "allow_null": True}}
    
#    def get_ephemeral_key(self, obj):
#        key = stripe.EphemeralKey.create(
#            customer=obj.stripe_id, stripe_version=stripe.api_version)
#        print(key)
#        return key

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        customer_profile, created = CustomerProfile.objects.update_or_create(user=user, 
                                                        first_name=validated_data.pop('first_name'), 
                                                        middle_name=validated_data.pop('middle_name'), 
                                                        last_name=validated_data.pop('last_name'),
                                                        # country=validated_data.pop('country'),
                                                        # phone=validated_data.pop('phone'),
                                                        # emergency_contact_name=validated_data.pop('emergency_contact_name'),
                                                        # emergency_contact_phone=validated_data.pop('emergency_contact_phone'),
                                                        )
        customer_profile.save()
        return customer_profile
    
    def update(self, instance, validated_data):
        print("WE HERE - traveler")
        current_user = self.context['request'].user
        print("The current user is  ", current_user)
        user = validated_data.get('user')
        if (user != None):
            if (user.get('email') != None):
                instance.user.email = user.get('email')
                instance.user.username = user.get('email')
            if (user.get('username') != None):
                instance.user.username = user.get('username')
            instance.user.save()
 
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.country = validated_data.get('country', instance.country)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.emergency_contact_name = validated_data.get('emergency_contact_name', instance.emergency_contact_name)
        instance.emergency_contact_relation = validated_data.get('emergency_contact_relation', instance.emergency_contact_relation)
        instance.emergency_contact_email = validated_data.get('emergency_contact_email', instance.emergency_contact_email)
        instance.emergency_contact_phone = validated_data.get('emergency_contact_phone', instance.emergency_contact_phone)
        instance.save()
        return instance

class HostelProfileSerializer(serializers.ModelSerializer):
    country = SerializableCountryField(allow_blank=True)
    email = serializers.CharField(source='user.email')
    # room_details = HostelRoomDetailSerializer()
    class Meta:
        model = models.Profile
        fields = ('id', 'user', 'hostel_name', 'email', 'phone', 'fax', 'website', 'address', 
                'city_state', 'zip_code', 'country', 'latitude', 'longitude', 'stripe_id',  
                # 'room_details',
        )
        read_only_fields = ('id', 'stripe_id')




class HostelRoomDetailSerializer(serializers.ModelSerializer):
    hostel = HostelProfileSerializer(required=True)
    class Meta:
        model = models.RoomDetail
        fields = ('id', 'avaliability', 'price', 'currency',
                  'VAT', 'hostel')
        # lookup_field = 'hostel.id'



        

class ReservationSerializer(serializers.ModelSerializer):
    # Changes hostel and customer reference to name instead of ID on API
    # hostel = serializers.CharField(source='hostel.user') 
    # customer = serializers.CharField(source='customer.user')
    class Meta:
        model = models.Reservation
        fields = ('hostel', 'customer', 'is_confirmed', 'is_checked_in',)

    def create(self, validated_data):
        reservation = models.Reservation(
            hostel=validated_data['hostel'],
            customer=validated_data['customer'],
            is_confirmed=validated_data['is_confirmed'],
            is_checked_in=validated_data['is_checked_in'],
        )
        reservation.save()
        return reservation
# class TravelerProfileSerializer(serializers.ModelSerializer):
#     country = SerializableCountryField(allow_blank=True)

#     class Meta:
#         model = models.CustomerProfile
#         fields = ('first_name', 'middle_name', 'last_name', 'country')

#     def create(self, validated_data):
#         customer_profile= models.CustomerProfile(first_name=validated_data['first_name'],
#                                                 middle_name=validated_data['middle_name'],
#                                                 last_name=validated_data['last_name'],
#                                                 country=validated_data['country'],
#                                                 )
#         customer_profile.save()
#         return customer_profile



# class UserSerializer(serializers.ModelSerializer):
#     profile = TravelerProfileSerializer(required=True)

#     class Meta:
#         model = models.User
#         fields = (
#             'username',
#             'email',
#             'password',
#             'account_type',
#             'profile',
#         )
#     def create(self, validated_data):
#         user = models.User(
#             email=validated_data['email'],
#             username=validated_data['username'],
#             account_type=validated_data['account_type']
#         )
#         user.set_password(validated_data['password'])
#         profile_data = validated_data.pop('profile')
#         profile = TravelerProfileSerializer.create(TravelerProfileSerializer(), validated_data=profile_data)
#         user_profile, created = models.User.objects.create(email=validated_data.pop('email'),
#                                                                      username=validated_data.pop('username'),
#                                                                      account_type=validated_data.pop('account_type'),
#                                                                      password=validated_data.pop('password'),
#                                                                      profile=profile)
        
#         user_profile.save()
#         return user_profile
