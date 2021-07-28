import stripe
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import uuid
from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.hashers import make_password
from django_countries.fields import CountryField
from django.utils import timezone
import django
from currencies.models import Currency, CurrencyManager
from rest_framework.authtoken.models import Token
import requests
from django.http import JsonResponse
import datetime
# import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = "2020-08-27"

class UserManager(BaseUserManager):
    
    # Method to creating a new user - if you want to add or remove fields, then you change the parameters
    # MAYBE - change this field for customization 
    # ------- change is_active to False to make user not active when they create it so that we can manually activate it 
    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False): #add 'username' if you want that in
        # if not email:
        #     raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("User must have a username")
        # Create the user - user must have these fields when created 
        user_obj = self.model(
            # email = self.normalize_email(email), # Built in method from BaseUserManager - normalizes email so we can use repeatedly makes 'foobar@GMAIL.com' and 'foobar@gmail.com' the same
            username = username,            
        )
        user_obj.set_password(password) # How to set and change password
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

# This code is triggered whenever a new user has been created and saved to the database

# Custome User Class - Overrides django built in user
class User(AbstractBaseUser):

    CHOICES = (
        ('1', 'None'),
        ('2', 'Hostel'),
        ('3', 'Traveler'),  
    )

    # User Fields
    username            = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email               = models.EmailField(max_length=255, unique=True)
    # full_name         = models.CharField(verbose_name='Hostle Name', max_length=255, blank=True, null=True)
    # hostle_name       = models.CharField(max_length=255, blank=True, null=True)
    is_active           = models.BooleanField(default=True) # Can the user login - if False then they are not allowed
    is_staff            = models.BooleanField(default=False) # Staff user - not a superuser
    is_admin            = models.BooleanField(default=False) # Superuser
    # is_hostel           = models.BooleanField(default=False, blank=True, null=True )
    # is_customer         = models.BooleanField(default=False)

    account_type = models.CharField(max_length=255, choices=CHOICES, default=1)

    timestamp           = models.DateTimeField(auto_now_add=True)
    # confirm           = models.BooleanField(default=False) # Confirm email

    # Sets the Username field when logging in
    USERNAME_FIELD      = 'username'

    # Fields that are required when the user is being created
    # USERNAME_FIELD and Password and required by default
    REQUIRED_FIELDS     = []

    objects             = UserManager() # Calling user manager

    # Methods to access the information in the db and return something
    def __str__(self):
        return self.username               
    
    def get_username(self):
        "Return the identifying username for this User"
        return self.username

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def get_email(self):
        return self.email

    # Properties to check status of user
    # @property
    # def is_staff(self):
    #     return self.is_staff
    
    # @property
    # def is_admin(self):
    #     return self.is_admin
    
    # @property
    # def is_active(self):
    #     return self.is_active

# Change name to HostleProfile

class Profile(models.Model):

    user            = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # email           = models.OneToOneField(User.email, on_delete=models.CASCADE, blank=True, null=True)
    update          = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now=True)
    new             = models.BooleanField(default=True)
    
    hostel_name     = models.CharField(max_length=50, blank=True, null=True)
    phone           = PhoneNumberField(max_length=20, blank=True, null=True)
    fax             = PhoneNumberField(blank=True, null=True)
    website         = models.CharField(max_length=20, blank=True, null=True)
    
    address         = models.CharField(
        "Street", max_length=1024, blank=True, null=True)
    city_state      = models.CharField(
        "City, State", max_length=1024, blank=True, null=True)
    zip_code        = models.CharField("Zip/Postal Code", max_length=1024, blank=True, null=True)
    # country         = models.CharField(
    #     "Country", max_length=1024, blank=True, null=True)
    country = CountryField(blank_label='(select country)', null=True)
    latitude        = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    longitude       = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, default='0')
    
    owner_name              = models.CharField(max_length=20, blank=True, null=True)
    owner_phone             = models.CharField(max_length=20, blank=True, null=True)
    first_manager_name      = models.CharField(max_length=20, blank=True, null=True)
    first_manager_phone     = models.CharField(max_length=20, blank=True, null=True)
    first_manager_email     = models.CharField(max_length=20, blank=True, null=True)
    second_manager_name     = models.CharField(max_length=20, blank=True, null=True)
    second_manager_phone    = models.CharField(max_length=20, blank=True, null=True)
    second_manager_email    = models.CharField(max_length=20, blank=True, null=True)

    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    stripe_access_token = models.CharField(max_length=200, null=True, blank=True)
    stripe_refresh_token = models.CharField(max_length=200, null=True, blank=True)

    # __og_hostel_name = None
    # __og_phone = None
    # __og_address = None
    # __og_city_state = None
    # __og_country = None

    # def __init__(self, *args, **kwargs):
    #     super(Profile, self).__init__(*args, **kwargs)
    #     self.__og_hostel_name = self.hostel_name
    #     self.__og_phone = self.phone
    #     self.__og_address = self.address
    #     self.__og_city_state = self.city_state
    #     self.__og_country = self.country

    # def save(self, force_insert=False, force_update=False, *args, **kwargs):
    #     if self.hostel_name != self.__og_hostel_name:
    #         # hostel name changed 
    #         hostel_name = self.hostel_name
    #         print(hostel_name)
    #         print(__og_hostel_name)
    #         # super(Profile, self).save(*args, **kwargs)

    #     super(Profile, self).save(force_insert, force_update, *args, **kwargs)
    #     self.__og_hostel_name = self.hostel_name


    def __str__(self):
        return str(self.user)
    # def __init__(self):

    def save(self, **kwargs):
        # if (self.stripe_id != '') & (self.stripe_id is not None):
        #     print("Stripe id is not empty")
        # else:
        #     print("Stripe id is empty")
        #     # new_stripe_id = stripe.Customer.create(email=self.user.email)
        #     new_stripe_id = stripe.Account.create(
        #                                             type="express",
        #                                             country="US",
        #                                             email=self.user.email,
        #                                             capabilities={
        #                                                 "card_payments": {"requested": True},
        #                                                 "transfers": {"requested": True},
        #                                             },
        #                                             # tos_acceptance={
        #                                             #     'service_agreement': 'recipient',
        #                                             # },
        #                                         )
        #     self.stripe_id = new_stripe_id['id']
        if self.address is not None and self.city_state is not None and self.zip_code is not None:
            address_string = " ".join(
                [self.address, str(self.zip_code), self.city_state])
            api_key = "AIzaSyDJ-TSQ5f2kwiGcnJBv2RWm5fhkEJy4DpA"
            api_response = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address_string, api_key))
            api_response_dict = api_response.json()

            if api_response_dict['status'] == 'OK':
                print("it worked")
                self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
                self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
                # self.save()
            else: 
                print("it didnt work")
        super(Profile, self).save(**kwargs)

class Request(models.Model):
    username        = None
    #user           = models.OneToOneField(User, on_delete=models.CASCADE)
    email           = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    hostel_name     = models.CharField(max_length=50, blank=True, null=True)
    phone           = PhoneNumberField(max_length=20, blank=True, null=True)
    address         = models.CharField(
        "Street", max_length=1024, blank=True, null=True)
    zip_code = models.CharField(
        "Zip/Postal Code", max_length=1024, blank=True, null=True)
    city_state      = models.CharField("City, State", max_length=1024, blank=True, null=True)
    country         = models.CharField(
        "Country", max_length=1024, blank=True, null=True)
    
    is_active       = models.BooleanField(default=True)
    update          = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.user.email
        return self.hostel_name

    # Connect to user model with foreign key
    #user = models.OneToOneField(User, on_delete=models.CASCADE, default=False, blank=True)

    # Extend extra data for the User model

class HostelProfile(models.Model):

    user        = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    # email     = models.EmailField(max_length=255, blank=True, null=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now=True)
    new         = models.BooleanField(default=True)

    hostel_name = models.CharField(max_length=50, blank=True, null=True)
    phone       = PhoneNumberField(max_length=20, blank=True, null=True)
    fax         = PhoneNumberField(blank=True, null=True)
    website     = models.CharField(max_length=20, blank=True, null=True)

    address     = models.CharField(
        "Street", max_length=1024, blank=True, null=True)
    zip_code = models.CharField(
        "Zip/Postal Code", max_length=1024, blank=True, null=True)
    city_state  = models.CharField(
        "City, State", max_length=1024, blank=True, null=True)
    country     = models.CharField(
        "Country", max_length=1024, blank=True, null=True)

    def __str__(self):
        return str(self.user)
    # def __init__(self):

class HostelOwner(models.Model):
    owner_name      = models.CharField(max_length=20, blank=True, null=True)
    owner_phone     = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class HostleManagers(models.Model):
    first_manager_name      = models.CharField(
        max_length=20, blank=True, null=True)
    first_manager_phone     = models.CharField(
        max_length=20, blank=True, null=True)
    first_manager_email     = models.CharField(
        max_length=20, blank=True, null=True)
    second_manager_name     = models.CharField(
        max_length=20, blank=True, null=True)
    second_manager_phone    = models.CharField(
        max_length=20, blank=True, null=True)
    second_manager_email    = models.CharField(
        max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class RoomDetail(models.Model):
    hostel = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    # total_coed_beds = models.IntegerField(blank=True, null=True)
    total_coed_beds = models.IntegerField(default=0)
    total_beds_password = models.CharField(max_length=100, blank=True, null=True)

    # occupied_beds = models.IntegerField(blank=True, null=True)
    # avaliability = models.IntegerField(blank=True, null=True)
    occupied_beds = models.IntegerField(default=0)
    avaliability = models.IntegerField(default=0)

    # price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,)
    price_password = models.CharField(max_length=100, blank=True, null=True)
    # balance = MoneyField(null=True, max_digits=14, decimal_places=2,
    #                      default_currency=None)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    VAT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,)
    
    employee_password = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.hostel)

    # CREATE A SAVE() METHOD TO CALCULATE THE OCCUPIDE_BEDS
    def save(self, *args, **kwargs):
        # self.total_bed_password = make_password(self.total_bed_password)
        # calculate sum before saving.
        self.avaliability = self.calculate_avaliability()
        super(RoomDetail, self).save(*args, **kwargs)

    def calculate_avaliability(self):
        try:
            total_coed_beds = self.total_coed_beds
            occupied_beds = self.occupied_beds
            return total_coed_beds - occupied_beds
        except KeyError:
            return 0

    # def add_room(self):
    #     try:
    #         occupied_beds = self.occupied_beds
    #         return occupied_beds + 1
    #     except KeyError:
    #         return 0

    # def minus_room(self):
    #     try:
    #         occupied_beds = self.occupied_beds
    #         return occupied_beds - 1
    #     except KeyError:
    #         return 0

class CustomerProfile(models.Model):
    sex_choices = (('F', 'Female'), ('M', 'Male'), ('U', 'Unsure'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    ## you need to set a default profile picture
    profile_picture = models.ImageField(upload_to='pictures', null=True, blank=True, default="media/pictures/791218_man_512x512.png")
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(
        max_length=1, choices=sex_choices, blank=True, null=True)
    # country = models.CharField("Country", max_length=1024, blank=True, null=True)
    country = CountryField(blank_label='(select country)', null=True)

    # email = models.OneToOneField(User.email, on_delete=models.CASCADE, blank=True, null=True)
    # email = models.EmailField(max_length=255, blank=True, null=True, unique=True, default="example@gmail.com")
    phone = PhoneNumberField(max_length=20, blank=True, null=True,)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True, )
    emergency_contact_relation = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_email = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_phone = PhoneNumberField(max_length=20, blank=True, null=True)
    
    stripe_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):

        if (self.stripe_id != '') & (self.stripe_id is not None):
            print("Stripe id is not empty")
            key = stripe.EphemeralKey.create(customer=self.stripe_id, stripe_version=stripe.api_version)
            print(key)
        else:
            print("Stripe id is empty")
            name = self.first_name + " " + self.last_name
            new_stripe_id = stripe.Customer.create(email=self.user.email, name=name)
            self.stripe_id = new_stripe_id['id']

        # if self.first_name and self.last_name:
        #     self.first_name = self.first_name.title() # Capitalize first letter of the word
        #     self.last_name = self.last_name.title()
        super(CustomerProfile, self).save(*args, **kwargs)
        
class Reservation(models.Model):
    hostel = models.ForeignKey(Profile, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    # reservation_date_time = models.DateTimeField(
    #     auto_now=False, auto_now_add=False, blank=True, null=True)
    # expected_arrival = models.DateTimeField(
    #     auto_now=False, auto_now_add=False, blank=True, null=True)
    # expected_departure = models.DateTimeField(
    #     auto_now=False, auto_now_add=False, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)
    is_checked_in = models.BooleanField(default=False)
    is_history = models.BooleanField(default=False)


    ## Switch made_on with created after testing 
    made_on = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)

    # Timezone == UTC – The World's Time Standard
    created = models.DateField(editable=False, null=True, default=django.utils.timezone.now)
    modified = models.DateTimeField(editable=False, null=True)


    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, blank=True, null=True)
 
    def __str__(self):
        return str(self.hostel)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
            self.check_out = self.created.date() + datetime.timedelta(days=1)
            # Add 1 to Occupied Beds in RoomDetail Model when Reservation is created for that Hostel
            room_detail = RoomDetail.objects.get(hostel=self.hostel)
            if room_detail.total_coed_beds != room_detail.occupied_beds:
                room_detail.occupied_beds += 1
                room_detail.save()
        self.modified = timezone.now()
        self.is_checked_in = self.checkedIn()
        self.is_history = self.history()
        super(Reservation, self).save(*args, **kwargs)
    
    def checkedIn(self):
        try:
            is_confirmed = self.is_confirmed
            is_checked_in = self.is_checked_in
            if is_confirmed != True:
                return False
            else:
                return is_checked_in
        except KeyError:
            return 0 

    def history(self):
        try:
            is_confirmed = self.is_confirmed
            is_checked_in = self.is_checked_in
            if is_confirmed == True and is_checked_in == True:                
                return True
            else: 
                return False
        except KeyError:
            return 0

    # @property
    # def is_expired(self):
    #     seconds_in_hour = 3600
    #     if (datetime.now() - self.reservation_date).seconds > seconds_in_hour
    #     return True
    #     else:
    #         return False
        
    #     if ticket_instance.is_expired:
    #         #do something




# class Currency(models.Model):
# #     code = models.CharField(max_length=3, blank=True, null=True)
# #     name = models.CharField(max_length=50, blank=True, null=True)
# #     symbol = models.CharField(max_length=5, blank=True, null=True)
# #     factor = models.IntegerField(blank=True, null=True)
# #     is_active = models.BooleanField(default=False)
# #     is_base = models.BooleanField(default=False)
# #     is_default = models.BooleanField(default=False)

# #     class Meta:
# #         verbose_name_plural = "Currencies"

#     code = models.CharField(max_length=3, primary_key=True)
#     name = models.CharField(max_length=55, db_index=True)
#     symbol = models.CharField(max_length=4, blank=True, db_index=True)
#     factor = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True, help_text='Specifies the currency rate ratio to the base currency.')

#     is_active = models.BooleanField(default=True, help_text='The currency will be available.')
#     is_base = models.BooleanField(default=False, help_text='Make this the base currency against which rate factors are calculated.')
#     is_default = models.BooleanField(default=False, help_text='Make this the default user currency.')



#     class Meta:
#         ordering = ['name']
#         verbose_name = ('currency')
#         verbose_name_plural = ('currencies')

#     # def __str__(self):
#     #     return self.code

#     # def save(self, **kwargs):
#     #     # Make sure the base and default currencies are unique
#     #     if self.is_base is True:
#     #         self.__class__._default_manager.filter(
#     #             is_base=True).update(is_base=False)

#     #     if self.is_default is True:
#     #         self.__class__._default_manager.filter(
#     #             is_default=True).update(is_default=False)

#     #     # Make sure default / base currency is active
#     #     if self.is_default or self.is_base:
#     #         self.is_active = True

#     #     super(Currency, self).save(**kwargs)



