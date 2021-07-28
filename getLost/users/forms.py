from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Request, Profile, RoomDetail, Reservation
from django.forms import ModelForm
from currencies.models import Currency, CurrencyManager
from django_countries.templatetags import countries
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget




User = get_user_model()

class RegisterForm(forms.ModelForm):

    username = forms.CharField() # add label here to change
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # maybe change message to the first login
            raise forms.ValidationError(
                "Are you sure you are registered? we cannot find this user.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

# Form for admin to create a user
class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
        
    CHOICES = (
        ('1', 'None'),
        ('2', 'Hostel'),
        ('3', 'Traveler'),
    )

    account_type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    class Meta:
        model = User
        fields = ('email', 'username', ) # Add fields here for user to be required 

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("Are you sure you are registered? we cannot find this user.") ##maybe change message to the first login
    #     return username

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    username = forms.CharField()
    # password = ReadOnlyPasswordHashField()
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <br><a href=\"../password/\">THIS FORM</a>."))

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

#Form for Logging in
class LoginForm(forms.Form):
    username = forms.CharField(label='ID Number', required=True)
    password = forms.CharField(label='PIN', widget=forms.PasswordInput, required=True)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # maybe change message to the first login
            raise forms.ValidationError(
                "Are you sure you are registered? we cannot find this user.")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid Password")
        elif user is None:
            pass
        else:
            return password

# Login Form for when user has key
# class RegisterLoginForm(forms.Form):
#     username = forms.CharField(label='ID Number')
#     password = forms.CharField(label='PIN', widget=forms.PasswordInput)

# Form to ask user for email to create account
class RequestForm(forms.ModelForm):
    username = None
    class Meta:
        model = Request
        fields = ('hostel_name', 'email', 'phone',
                  'address', 'zip_code', 'city_state', 'country')

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(RequestForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['email'].required = True
        self.fields['hostel_name'].required = True
        
        for field in self.fields.values():
            field.error_messages = {'required': 'The field {fieldname} is required'.format(
                fieldname=field.label)}


    
    # Makes sure email is unique
    def save(self, commit=True):
        user = super(RequestForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# Form for the final register questions
class ProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ('hostel_name', 'address', 'zip_code', 'city_state', 'country', 'phone',
                  'fax', 'website', 'owner_name', 'owner_phone', 'first_manager_name', 
                  'first_manager_phone', 'first_manager_email', 'second_manager_name', 'second_manager_phone', 'second_manager_email'
                  )

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.hostel_name = self.cleaned_data["hostel_name"]
        if commit:
            user.save()
            print("save function worked")
        return user

class IndexForm(forms.ModelForm):

    occupied_beds = forms.IntegerField()

    class Meta:
        model = RoomDetail
        fields = ('occupied_beds',)

class ConfirmForm(forms.ModelForm):

    is_confirmed = forms.BooleanField()

    class Meta:
        model = Reservation
        fields = ('is_confirmed',)


class CheckinForm(forms.ModelForm):

    is_checked_in = forms.BooleanField()

    class Meta:
        model = Reservation
        fields = ('is_checked_in',)

class PriceForm(forms.ModelForm):

    price = forms.DecimalField()

    class Meta:
        model = RoomDetail
        fields = ('price',)
class PricePasswordForm(forms.ModelForm):
    price_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RoomDetail
        fields = ('price_password',)

class TotalBedsForm(forms.ModelForm):

    # total_beds_password = forms.CharField(widget=forms.PasswordInput)
    total_coed_beds = forms.IntegerField()

    class Meta:
        model = RoomDetail
        fields = ('total_coed_beds',)


class TotalBedsPasswordForm(forms.ModelForm):

    total_beds_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RoomDetail
        fields = ('total_beds_password',)


class PublicInfoForm(forms.ModelForm):
    country = CountryField().formfield()
    class Meta:
        model = Profile
        fields = ('hostel_name', 'phone',
                  'address', 'zip_code', 'city_state', 'country')

class PublicInfoEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class PrivateInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('hostel_name', 'address', 'zip_code', 'city_state', 'country', 'phone',
                  'fax', 'website', 'owner_name', 'owner_phone', 'first_manager_name',
                  'first_manager_phone', 'first_manager_email', 'second_manager_name', 'second_manager_phone', 'second_manager_email')

class MasterPasswordForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput, )
#     password2 = forms.CharField(
#     label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('password',)
    def clean_password(self):
        password = self.cleaned_data.get("password")
        # password = self.check_password(self.cleaned_data.get("password"))
        if password:
            return password
        else:
            print("PASSWORD is wrong")
    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #         return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MasterPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])  
        # password = self.cleaned_data["password"]
        # if password:
        #     print("IT WORKED")
        #     user.set_password(password)
        # else:
        #     print("IT DIDNT WORK")
        if commit:
            user.save()
        return user

class EmployeePasswordForm(forms.ModelForm):
    employee_password = forms.CharField(
        required=False, widget=forms.PasswordInput)

    class Meta:
        model = RoomDetail
        fields = ('employee_password', )

class PracticeForm(forms.ModelForm):  ## create password check here as well with if loop saying if it matches or not
    password = forms.CharField(widget=forms.PasswordInput, )
    password_flag = True

    class Meta:
        model = User
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super(PracticeForm, self).__init__(*args, **kwargs)

    def set_password_flag(self):
        self.password_flag = False
        return 0

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if self.password_flag == False:
            print("it is wrong")
            raise forms.ValidationError(
                "The password that you have entered is wrong.")
        else:
            print("it works")
        return password


# create password check here as well with if loop saying if it matches or not
class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, )
    password_flag = True

    class Meta:
        model = User
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)

    def set_password_flag(self):
        self.password_flag = False
        return 0

    def clean_password(self):
        password = self.cleaned_data.get("check-password")
        if self.password_flag == False:
            print("it is wrong")
            raise forms.ValidationError(
                "The password that you have entered is wrong.")
        else:
            print("it works")
        return password

class LanguageCurrencyForm(forms.ModelForm):
    # balance = MoneyField()
    VAT = forms.DecimalField()
    currency = forms.ModelChoiceField(queryset=Currency.objects.all())

    class Meta:
        model = RoomDetail
        fields = ('currency', 'VAT',)

class StripeBillingForm(forms.Form):
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)
