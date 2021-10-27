import stripe
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, RequestForm, LoginForm, ProfileForm, ConfirmForm, PriceForm, TotalBedsForm, PublicInfoForm, PublicInfoEmailForm, PrivateInfoForm, MasterPasswordForm, EmployeePasswordForm, PracticeForm, PasswordForm, LanguageCurrencyForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, User, Reservation, CustomerProfile, RoomDetail
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict
# from test.dtracedata import instance
import logging
from django.views.decorators.csrf import csrf_protect
from rest_framework.reverse import reverse
from django.views import View
from users.forms import StripeBillingForm
from django.db.models import ObjectDoesNotExist
from django.conf import settings
import urllib
import requests

stripe.api_key = settings.STRIPE_SECRET_KEY

def request_register(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You will be contacted in the next 24hrs for verification.')
            return redirect('message')
        else:
            print("There is an error")
    else:
        form = RequestForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
  ## For this to work, you might need a def form_valid() method

# ##user must be logged in to view this page
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    print(profile.id)
    return render(request, 'users/profile.html')

def hostel_portal(request):
    return render(request, 'users/hostel_portal.html')

def contact(request):
    return render(request, 'users/contact.html')
# @csrf_exempt
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        print("user is authenticated")
        return redirect('index')
    else:
        print("user is not authenticated")
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # variable=parameter
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                profile = Profile.objects.get(user=request.user)
                if user.account_type == '2':
                    # maybe you dont need to save profile
                    user.profile.save()
                    return redirect('index')
                else:
                    messages.error(request, 'User is Not a Hostel')
                    return redirect('login')
            else:
                messages.error(request, 'Username Or Password is incorrect')
                return redirect('login')
            
            # if user is not None:
            #     login(request, user)
            #     # Check to see if user is new - if user is new, send them to profile registeration page
            #     profile = Profile.objects.get(user=request.user)
            #     if user.account_type == '2':
            #         # if request.user.profile.new == True:
            #         if (request.user.profile.hostel_name is None or 
            #                     request.user.profile.phone is None or
            #                     request.user.profile.address is None or
            #                     request.user.profile.city_state is None or
            #                     request.user.profile.country is None or
            #                     request.user.profile.owner_name is None or
            #                     request.user.profile.owner_phone is None or
            #                     request.user.profile.zip_code is None):
            #             request.user.profile.new = False
            #             user.profile.save()
            #             return redirect('profileregister')
            #         else:
            #             print("the users id is: ", profile.id)
            #             return redirect('index')
            #     else:
            #         messages.error(request, 'User is Not a Hostel')
            #         return redirect('login')
            # else:
            #     messages.error(request, 'Username Or Password is incorrect')
            #     return redirect('login')
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)

# NOT BEING USED
def register_login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # variable=parameter
        user = authenticate(request, username=username, password=password)
        # login(request, user)
        # # Check to see if user is new - if user is new, send them to profile registeration page
        # profile = Profile.objects.get(user=request.user)
        # if request.user.profile.new == True:
        #     request.user.profile.new = False
        #     user.profile.save()
        #     return redirect('profileregister')
        # else:
        #     return redirect('index')
        if user is not None:  
            if user.account_type == '2':
                # maybe you dont need to save profile
                login(request, user)
                profile = Profile.objects.get(user=request.user)
                print("its a hostel")
                user.profile.save()
                return redirect('index')
            else:
                print("its a traveler")
                messages.error(request, 'User is Not a Hostel')
                return redirect('registerlogin')
        else:
            messages.error(request, 'Username Or Password is incorrect')
            return redirect('registerlogin')
   
    context = {
        "form": form
    }
    return render(request, "users/profile_login.html", context)

@login_required
@csrf_protect
def profile_register(request): 
    profile = Profile.objects.get(user=request.user) 
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = profile)
        print("Hello world")
        print(form['hostel_name'].value())
        print(form['phone'].value())
        if form.is_valid():
            print("it is valid")
            form.save()
            return redirect('profileregister2')
        else:
            print("it is not valid")
            print(form.errors)
    else:
        form = ProfileForm(instance = profile)

    context = {'form': form}
    return render(request, 'users/profile_register.html', context)

@login_required
@csrf_protect
def profile_register2(request):
    profile = Profile.objects.get(user=request.user)
    roomdetails = RoomDetail.objects.get(hostel=profile)
    if request.method == 'POST':
        form = LanguageCurrencyForm(request.POST, instance=roomdetails)

        if form.is_valid():
            form.save()
            return redirect('profileregister3')
        else:
            print(form.errors)
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'users/profile_register02.html', context)

@login_required
def profile_register3(request):
    return render(request, 'users/profile_register03.html')

def message_view(request):
    return render(request, 'users/message.html')

@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(username=profile.user)
    password_check = False
    master_pass = False
    employee_pass = False

    if (request.user.profile.hostel_name is None or
    request.user.profile.phone is None or
    # request.user.profile.email is None or
    request.user.profile.address is None or
    request.user.profile.city_state is None or
    request.user.profile.country is None or
    request.user.profile.owner_name is None or
    request.user.profile.zip_code is None or
            request.user.profile.first_manager_name is None):
        return redirect('profileregister')
    else:  
        reservations = profile.reservation_set.all()
        obj = CustomerProfile.objects.get(id=1)
        # Check to see if hostel has RoomDetail model connected to it, if not, pass as empty
        try:
            roomdetails = RoomDetail.objects.get(hostel=profile)
        except RoomDetail.DoesNotExist:
            roomdetails = None
        
        # Here
        # print("the reservation count is")
        # print(reservations.count())
        # print(reservations.filter(is_confirmed=True).count())

        if request.method == 'POST':
            res_form = ConfirmForm()
            # checkin_form = CheckinForm()
            price_form = PriceForm()
            total_beds_form = TotalBedsForm()
            # price_password_form = PricePasswordForm()
            # total_beds_password_form = TotalBedsPasswordForm()
            password_form = PasswordForm()
            password_form = PasswordForm(request.POST, instance=profile)

            input_password = request.POST.get('check-password')
            if input_password:
                print("PASSWORD CHECK FORM")

                master_pass = user.check_password(input_password)
                if (input_password == roomdetails.employee_password):
                    employee_pass = True
                else:
                    employee_pass = False
                if (master_pass == True or employee_pass == True):
                    print("one of the passwords are true")
                    password_check = True
                else:
                    print("both passwords are incorrect")
                    password_check = False

                if password_check:
                    print("Password Check: It is Correct")
                    password_check = True
                else:
                    password_form.set_password_flag()
                    print("Password Check: it is Incorrect")
                    # print(practice_form.errors)
                    # print(practice_form.errors.as_data())
                    # print(practice_form.errors.as_json())

            name = request.POST.get("price")
            if request.POST.get('is_confirmed') == 'True':
                # it = request.POST.get('is_confirmed')
                res_id = request.POST.get('reservation-id')
                instance = get_object_or_404(Reservation, pk=res_id)
                res_detail = reservations.get(id=instance.id)
                res_form = ConfirmForm(request.POST, instance=res_detail)
                if res_form.is_valid():
                    new_form = res_form.save()
                    return JsonResponse({'is_confirmed': model_to_dict(new_form)})
                else:
                    return redirect(request.path_info)
            # elif request.POST.get('is_checked_in') == 'True':
            #     it = request.POST.get('is_checked_in')
            #     res_id = request.POST.get('reservation-id')
            #     instance = get_object_or_404(Reservation, pk=res_id)
            #     res_detail = reservations.get(id=instance.id)
            #     checkin_form = CheckinForm(request.POST, instance=res_detail)
            #     if checkin_form.is_valid():
            #         new_form = checkin_form.save()
            #         return JsonResponse({'is_checked_in': model_to_dict(new_form)})
            #     else:
            #         return redirect(request.path_info)
            elif 'price' in request.POST:
                print("price button works")
                price_form = PriceForm(request.POST, instance=roomdetails)
                print(price_form)
                if price_form.is_valid():
                    new_form = price_form.save()
                    return JsonResponse({'price': model_to_dict(new_form)})
                else:
                    return redirect(request.path_info)
            # elif 'price_password' and 'price_password_confirm' in request.POST:
            #     print('this worked')
            #     price_password_form = PricePasswordForm(
            #         request.POST, instance=roomdetails)
            #     print(price_password_form)
            #     if price_password_form.is_valid():
            #         new_form = price_password_form.save()
            #         return JsonResponse({'price_password': model_to_dict(new_form)})
            #     else:
            #         print("didnt work")
            #         return redirect(request.path_info)
            elif 'total_coed_beds' in request.POST:
                total_beds_form = TotalBedsForm(request.POST, instance=roomdetails)
                if total_beds_form.is_valid():
                    new_form = total_beds_form.save()
                    return JsonResponse({'total_coed_beds': model_to_dict(new_form)})
                else:
                    return redirect(request.path_info)
            # elif 'total_beds_password' and 'total_beds_password_confirm' in request.POST:
            #     print('this worked')
            #     total_beds_password_form = TotalBedsPasswordForm(
            #         request.POST, instance=roomdetails)
            #     if total_beds_password_form.is_valid():
            #         new_form = total_beds_password_form.save()
            #         return JsonResponse({'total_beds_password': model_to_dict(new_form)})
            #     else:
            #         print("didnt work")
            #         return redirect(request.path_info)
            # elif 'plus' or 'minus' in request.POST:
            #     print("checking loop 7")
            #     form = IndexForm(request.POST, instance=roomdetails)
            #     if form.is_valid():
            #         new_form = form.save()
            #         return JsonResponse({'occupied_beds': model_to_dict(new_form)}, status=200)
            #     else:
            #         return redirect(request.path_info)
            # else:
            #     print("checking loop 8")
            #     message = "it didnt work"
            #     return(message)
        elif request.is_ajax and request.method == "GET":
            # print("it was a get request")
            res_form = ConfirmForm()
            price_form = PriceForm()
            total_beds_form = TotalBedsForm()
            password_form = PasswordForm()
        else:
            # form = IndexForm()
            
            # checkin_form = CheckinForm()
            res_form = ConfirmForm()
            price_form = PriceForm()
            total_beds_form = TotalBedsForm()
            password_form = PasswordForm()
            # price_password_form = PricePasswordForm()
            # total_beds_password_form = TotalBedsPasswordForm()
            

        context = {'profile': profile, 'reservations': reservations, 'password_check': password_check, "master_pass": master_pass,
                    "employee_pass": employee_pass, "password_form": password_form, 'profile_picture': obj.profile_picture, 'roomdetails': roomdetails, 
                    # 'checkin_form': checkin_form,'price_password_form': price_password_form, 'total_beds_password_form': total_beds_password_form, 'form': form,
                    'price_form': price_form, 'total_beds_form': total_beds_form, "res_form": res_form,}
        return render(request, "users/index.html", context)

@login_required
def settingsFinal(request):
    profile = Profile.objects.get(user=request.user)
    # profile = Profile.objects.get(id=pk)
    user = User.objects.get(username=profile.user)
    password_check = False

    try:
        roomdetails = RoomDetail.objects.get(hostel=profile)
    except RoomDetail.DoesNotExist:
        roomdetails = None

    if request.method == 'POST':
        public_info_form = PublicInfoForm(request.POST, instance=profile)
        public_info_email_form = PublicInfoEmailForm(request.POST, instance=user)
        private_info_form = ProfileForm(request.POST, instance=profile)
        master_pass_form = MasterPasswordForm(request.POST, instance=user)
        employee_pass_form = EmployeePasswordForm(request.POST, instance=roomdetails)
        lang_currency_form = LanguageCurrencyForm(request.POST, instance=roomdetails)
        ## RENAMED
        # practice_form = PracticeForm
        password_form = PasswordForm(request.POST, instance=profile)
        
        # This Section is for accessing the forms validation error - you cannot access it after .isValid()
        # NOT NEEDED FOR VALIDATION
        input_password = request.POST.get('check-password')
        if input_password:
            print("PASSWORD CHECK FORM")
            password_check = user.check_password(input_password)
            print(input_password)
            if password_check:
                print("Password Check: It is Correct")
            else:
                password_form.set_password_flag()
                print("Password Check: it is Incorrect")

        input_password_change = request.POST.get('employee_password')
        if input_password_change:
            print("its employee password")
        elif request.POST.get('password'):
            print(" it is finding password")
     
        # if password_form.is_valid():
        #     # OR request.POST.get('password')
        #     print("PASSWORD CHECK FORM")
        #     input_password = password_form.cleaned_data['check-password']
        #     password_check = user.check_password(input_password)
        if public_info_form.is_valid() and public_info_email_form.is_valid() and not 'fax' in request.POST:
            print("PUBLIC INFO FORM")
            print(request.POST)
            public_info = public_info_form.save()
            public_info_email = public_info_email_form.save()
            return redirect('settings_final')
        elif 'fax' in request.POST and private_info_form.is_valid() and public_info_email_form.is_valid():
            print("PRIVATE INFO FORM")
            private_info = private_info_form.save()
            public_info_email = public_info_email_form.save()
            return redirect('settings_final')
        elif request.POST.get('password'):
            if master_pass_form.is_valid():
                print("MASTER FORM")
                master_pass = master_pass_form.save()
                return redirect('settings_final')
        elif request.POST.get('employee_password'):
            if employee_pass_form.is_valid():
                print("Employee FORM")
                employee_pass = employee_pass_form.save()
                return redirect('settings_final')
            else:
                print("Other")
        elif request.POST.get('currency'):
            if lang_currency_form.is_valid():
                print("Currency form is valid")
                lang_currency = lang_currency_form.save()
                return redirect('settings_final')
        elif request.POST.get('password') and request.POST.get('employee_password'):
            if master_pass_form.is_valid() and employee_pass_form.is_valid():
                print("PASSWORD FORM")
                master_pass = master_pass_form.save()
                employee_pass = employee_pass_form.save()
                return redirect('settings_final')
    else:
        print("NONE OF THE FORMS")
        password_form = PasswordForm()
        public_info_form = PublicInfoForm()
        public_info_email_form = PublicInfoEmailForm()
        private_info_form = ProfileForm()
        master_pass_form = MasterPasswordForm()
        employee_pass_form = EmployeePasswordForm()
        lang_currency_form = LanguageCurrencyForm()
        
    context = {'profile': profile, 'user': user, 'roomdetails': roomdetails,
               'password_check': password_check, "password_form": password_form, 'public_info_form': public_info_form,
               'public_info_email_form': public_info_email_form, 'private_info_form': private_info_form,
               'master_pass_form': master_pass_form, 'employee_pass_form': employee_pass_form,
                'lang_currency_form': lang_currency_form
                }
    return render(request, 'users/settings_final.html', context)

def stripeAddress(request):
    return render(request, 'users/stripe_address.html')

def stripeSettings(request):
    return render(request, 'users/stripe_page.html')

def stripePage(request):
    return render(request, 'users/stripe.html')

class StripePage(View):
    template_name = "users/stripe.html"
    # form = StripeBillingForm()

    
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(username=profile.user)
        print(profile.user.username)
        try:
            form = StripeBillingForm()
            context = {
                'form': form,
            }

            if (profile.stripe_id != '' and profile.stripe_id is not None):
                print("the profile stripe id is not empty")
                # customer = stripe.Customer.retrieve(profile.stripe_id)
                account = stripe.Account.retrieve()
                context.update({
                    'profile': profile
                })
                # print("HEY HEY EGHGTGEVE::::", customer.address)
                # cards = stripe.Customer.list_sources(
                #     profile.stripe_id,
                #     limit=3,
                #     object='card'
                # )
                # card_list = cards['data']
                # print(card_list)
                # if len(card_list) > 0:
                #     # update the context with the default card
                #     context.update({
                #         'card': card_list[0],
                #         'cards': card_list
                #     })
            else:
                print("the profile stripe id is empty")

            return render(self.request, self.template_name, context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("index")

    
    def post(self, *args, **kwargs):
        form = StripeBillingForm(self.request.POST or None)
        return render(self.request, self.template_name)

class StripeAuthorizeView(View):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(username=profile.user)
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        if (profile.stripe_id == '' and profile.stripe_id is None):
            url = 'https://connect.stripe.com/oauth/authorize'
            params = {
                'response_type': 'code',
                'scope': 'read_write',
                'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
                'redirect_uri': f'http://127.0.0.1:8000/oauth/callback'
            }
            url = f'{url}?{urllib.parse.urlencode(params)}'
            print(url)
            return redirect(url)
        else:
            link = stripe.AccountLink.create(
                account=profile.stripe_id,
                refresh_url="http://127.0.0.1:8000/dashboard/",
                return_url="http://127.0.0.1:8000/dashboard/",
                type="account_onboarding",
            )
            print("The link stuff: ", link)
            print(link.url)
            url = link.url
            return redirect(url)
        
class StripeAuthorizeCallbackView(View):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(username=profile.user)
        code = request.GET.get('code')
        if code:
            data = {
                'client_secret': settings.STRIPE_SECRET_KEY,
                'grant_type': 'authorization_code',
                'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
                'code': code
            }
            url = 'https://connect.stripe.com/oauth/token'
            resp = requests.post(url, params=data)
            print(profile.hostel_name)
            print(resp.json())
            print("The responses Stripe Account Id is:   ",
                  resp.json()['stripe_user_id'])
            profile.stripe_id = resp.json()['stripe_user_id']
            profile.stripe_access_token = resp.json()['access_token']
            profile.stripe_refresh_token = resp.json()['refresh_token']
            profile.save()
            

        

        url = reverse('stripe')
        response = redirect(url)
        return response

class StripePagePractice(View):
    template_name = "users/stripepractice.html"
    # form = StripeBillingForm()

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        user = User.objects.get(username=profile.user)
            
        print(profile.user.username)
        try:
            form = StripeBillingForm()
            context = {
                'form': form,
            }

            if (profile.stripe_id != '' and profile.stripe_id is not None):
                print("the profile stripe id is not empty")
                stripe_account = stripe.Account.retrieve(profile.stripe_id)
                print(stripe_account)
                # customer = stripe.Customer.retrieve(profile.stripe_id)
                account = stripe.Account.retrieve()
                context.update({
                    'profile': profile
                })
                # print("HEY HEY EGHGTGEVE::::", customer.address)
                # cards = stripe.Customer.list_sources(
                #     profile.stripe_id,
                #     limit=3,
                #     object='card'
                # )
                # card_list = cards['data']
                # print(card_list)
                # if len(card_list) > 0:
                #     # update the context with the default card
                #     context.update({
                #         'card': card_list[0],
                #         'cards': card_list
                #     })
            else:
                print("the profile stripe id is empty")

            return render(self.request, self.template_name, context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("index")

    def post(self, *args, **kwargs):
        form = StripeBillingForm(self.request.POST or None)
        return render(self.request, self.template_name)

# @login_required
# def settings(request, pk):
#     profile = Profile.objects.get(id=pk)
#     user = User.objects.get(username = profile.user)

#     try:
#         roomdetails = RoomDetail.objects.get(hostel=profile)
#     except RoomDetail.DoesNotExist:
#         roomdetails = None

#     if request.method == 'POST':
#         print("ITS A POST METHOD")
#         public_info_form = PublicInfoForm(request.POST, instance = profile)
#         public_info_email_form = PublicInfoEmailForm(request.POST, instance=user)
#         private_info_form = ProfileForm(request.POST, instance = profile)
#         master_pass_form = MasterPasswordForm(request.POST, instance=user)
#         employee_pass_form = EmployeePasswordForm( request.POST, instance= roomdetails)

#         print(request.POST)

#         if 'fax' in request.POST:
#             if 'fax' in request.POST and private_info_form.is_valid() and public_info_email_form.is_valid():
#                 print("PRIVATE INFO FORM")
#                 private_info = private_info_form.save()
#                 public_info_email = public_info_email_form.save()
#                 return redirect('settings', pk=pk)
#         elif 'password' and  not 'employee_password' and not 'hostel_name' in request.POST:
#             if master_pass_form.is_valid():
#                 print("MASTER FORM")
#                 master_pass = master_pass_form.save()
#                 return redirect('settings', pk=pk)
#         elif 'employee_password' and not 'password' and not 'hostel_name' in request.POST:
#             if employee_pass_form.is_valid():
#                 print("Employee FORM")
#                 employee_pass = employee_pass_form.save()
#                 return redirect('settings', pk=pk)
#             else:
#                 print("Other")
#         elif 'password' and 'employee_password' and not 'hostel_name' in request.POST:
#             if master_pass_form.is_valid() and employee_pass_form.is_valid():
#                 print("PASSWORD FORM")
#                 master_pass = master_pass_form.save()
#                 employee_pass = employee_pass_form.save()
#                 return redirect('settings', pk=pk)
#         else:
#             if public_info_form.is_valid() and public_info_email_form.is_valid():
#                 print("PUBLIC INFO FORM")
#                 public_info = public_info_form.save()
#                 public_info_email = public_info_email_form.save()
#                 return redirect('settings', pk=pk)

#     elif request.method == "GET":
#         print("ITS A GET METHOD")
#         public_info_form = PublicInfoForm()
#         public_info_email_form = PublicInfoEmailForm()
#         private_info_form = ProfileForm()
#         master_pass_form = MasterPasswordForm(request.GET, instance=roomdetails)
#         employee_pass_form = EmployeePasswordForm(request.GET, instance=roomdetails)
#         print(request.GET)
#         # success = master_pass_form.check_password(request.GET['password'])
#         # if success:
#         #     # do your email changing magic
#         #     print("PASSWORD check worked")
#         # else:
#         #     print("PASSWORD check  did not worked")
#         #     return http.HttpResponse("Your password is incorrect")
#         # ## LANGUAGE AND CURRENCY FORM
#     else:
#         public_info_form = PublicInfoForm()
#         public_info_email_form = PublicInfoEmailForm()
#         private_info_form = ProfileForm()
#         master_pass_form = MasterPasswordForm()
#         employee_pass_form = EmployeePasswordForm()


#     context = {'profile': profile, 'user': user, 'public_info_form': public_info_form,
#                'public_info_email_form': public_info_email_form, 'private_info_form': private_info_form,
#                'roomdetails': roomdetails,
#                'master_pass_form': master_pass_form, 'employee_pass_form': employee_pass_form,
#                }

#     return render(request, 'users/settings.html', context)


# @csrf_protect
# @login_required
# def practice(request, pk):
#     profile = Profile.objects.get(id=pk)
#     user = User.objects.get(username=profile.user)
#     password_check = False

#     try:
#         roomdetails = RoomDetail.objects.get(hostel=profile)
#     except RoomDetail.DoesNotExist:
#         roomdetails = None

#     if request.method == 'POST':
#         print(request.POST)
#         if request.is_ajax():
#             print( "it is ajax")
#         else:
#             print('it is not ajax')

#         public_info_form = PublicInfoForm(request.POST, instance = profile)
#         public_info_email_form = PublicInfoEmailForm(request.POST, instance=user)
#         practice_form = PracticeForm(request.POST, instance=profile)
#         # IMPORTANT: maybe use this to get the individual inputs from request to see which form you need to save to.
#         input_password = request.POST.get('password')
#         # print(test)
#         if input_password:
#             password_check = user.check_password(input_password)
#             if password_check:
#                 print("1. okay for real it works this time")
#             else:
#                 practice_form.set_password_flag()
#                 print("1. also it doesnt work")
#                 messages.error(request, 'Username Or Password is incorrect')
#                 print(practice_form.errors)
#                 print(practice_form.errors.as_data())
#                 print(practice_form.errors.as_json())

#         if practice_form.is_valid():
#             # print(request.POST)
#             input_password = practice_form.cleaned_data['password']
#             password_check = user.check_password(input_password)
#             # print(input_password)
#             # print(user.password)
#             # print(password_check)
#             if password_check:
#                 print("2. The Passwords are the same")
#             else:
#                 print("2. The passwords are not the same")

#         elif public_info_form.is_valid() and public_info_email_form.is_valid():
#             print("PUBLIC INFO FORM")
#             public_info = public_info_form.save()
#             public_info_email = public_info_email_form.save()
#             return redirect('practice', pk=pk)
#     else:
#         public_info_form = PublicInfoForm()
#         public_info_email_form = PublicInfoEmailForm()
#         practice_form = PracticeForm()

#         # # print(request.POST)
#         # if 'password' in request.POST:
#         #     # print("password form")
#         #     practice_form = PracticeForm(request.POST, instance=profile)

#         #     if practice_form.is_valid():
#         #         input_password = practice_form.cleaned_data['password']
#         #         print(input_password)
#         #         if user.check_password(input_password):
#         #             password_check = user.check_password(input_password)
#         #             print("The Passwords are the same")
#         #         else:
#         #             print("The passwords are not the same")
#         # elif 'hostel_name' in request.POST:
#         #     # print("other form")
#         #     public_info_form = PublicInfoForm(request.POST, instance=profile)
#         # else:
#         #     practice_form = PracticeForm()
#         #     public_info_form = PublicInfoForm()
#         # print(user.password)
#         # # print(practice_form)

#     context = {'profile': profile, 'user': user, 'roomdetails': roomdetails,
#                'password_check': password_check, "practice_form": practice_form, 'public_info_form': public_info_form,
#                'public_info_email_form': public_info_email_form,
#      }

#     return render(request, 'users/practice.html', context)
