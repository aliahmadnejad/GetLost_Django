from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm, RequestForm
from .models import Request, Profile, User, CustomerProfile, RoomDetail, Reservation
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import messages
from django.utils.translation import ngettext

User = get_user_model() # Creates User Model

class CustomUserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = Profile
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    # inlines = (CustomUserInline, )
    # The forms to add and change user instances
    form = UserAdminChangeForm  # Edit View
    add_form = UserAdminCreationForm  # Create View

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_active', 'account_type',)   # db displays these fields---- add "get_name" to get hostel name
    list_filter = ('is_admin', 'is_staff', 'is_active', 'account_type',)            # Filter through db with these fields
    fieldsets = (
        ('Authentication Info', {'fields': ('email', 'password', 'username',)}),
        # ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('account_type', 'is_admin', 'is_staff', 'is_active', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'account_type')}
         ),
    )
    search_fields = ('email', 'username',)
    ordering = ('email',)
    filter_horizontal = ()

    # Gets name of hostel linked to user model - not using because we also have travelers
    def get_name(self, obj):
        return obj.profile.hostel_name
        
    get_name.admin_order_field = 'profile'  # Allows column order sorting
    get_name.short_description = 'Hostel Name'  # Renames column head
admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user',]  # Search Fieds uses emails to find users
    list_display = ('id', 'hostel_name', 'user', 'get_email', 'phone', 'country')   # db displays these fields
    list_filter = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'new')}),
        ('Hostel Info', {'fields': ('hostel_name', 'phone', 'fax',
                                    'website', 'address', 'zip_code', 'city_state', 'country', 'longitude', 'latitude', 'stripe_id', 'stripe_access_token', 'stripe_refresh_token')}),
        ('Owner Info', {'fields': ('owner_name', 'owner_phone',)}),
        ('First Manager Info', {'fields': ('first_manager_name', 'first_manager_phone', 'first_manager_email',)}),
        ('Second Manager Info', {'fields': ('second_manager_name', 'second_manager_phone', 'second_manager_email',)}),
    )
    ordering = ('user', 'hostel_name', )
    filter_horizontal = ()

    class Meta:
        model = User
    def get_email(self, obj):
        return obj.user.email

    get_email.admin_order_field = 'user'  
    get_email.short_description = 'Email'
admin.site.register(Profile, ProfileAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('hostel_name', 'email', 'phone', 'country')   # db displays these fields
    list_filter = ('email',)            # Filter through db with these fields
    search_fields = ('email', 'hostel_name',)
    ordering = ('email', )
    filter_horizontal = ()

    fieldsets = (
        ("Basic Info", {'fields': ('email', 'hostel_name', 'phone')}),
        ('Hostel Address', {'fields': ('address',
                                       'zip_code', 'city_state', 'country',)}),
    )
admin.site.register(Request, RequestAdmin)

class RoomDetailAdmin(admin.ModelAdmin):

    # form = TotalBedPasswordForm

    list_display = ('hostel', 'total_coed_beds', 'avaliability', 'occupied_beds', 'price', 'VAT')   # db displays these fields
    # Filter through db with these fields
    list_filter = ('hostel',)
    search_fields = ('hostel',)
    ordering = ('hostel', )
    filter_horizontal = ()

    fieldsets = (
        ("Basic Info", {'fields': ('hostel', 'employee_password',)}),
        ('Bed Info', {'fields': ('total_coed_beds', 'occupied_beds', 'avaliability', 'total_beds_password',)}),
        ('Price Info', {'fields': ('price', 'currency', 'VAT', 'price_password',)}),
    )
admin.site.register(RoomDetail, RoomDetailAdmin)

class CustomerProfileAdmin(admin.ModelAdmin):
    search_fields = ['user', 'first_name', 'last_name',]  # Search Fieds uses emails to find users
    list_display = ('id', 'user', 'first_name', 'last_name', 'get_email', 'phone',)   # db displays these fields
    list_filter = ('user', 'age', 'sex',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Traveler Info', {'fields': ('first_name', 'last_name', 'profile_picture', 'age', 'sex', 'stripe_id')}),
        ('Address', {'fields': ('country',)}),
        ('Emergency Contact Info', {'fields': ('emergency_contact_name', 'emergency_contact_phone')}),
    )
    ordering = ('user', 'first_name', 'last_name', )
    filter_horizontal = ()

    class Meta:
        model = User

    def get_email(self, obj):
        return obj.user.email

    get_email.admin_order_field = 'user'
    get_email.short_description = 'Email'
admin.site.register(CustomerProfile, CustomerProfileAdmin)



# class CurrencyAdmin(admin.ModelAdmin):
#     list_display = ("name", "is_active", "is_base",
#                     "is_default", "code", "symbol", "factor")
#     list_filter = ("is_active", )
#     search_fields = ("name", "code")
# admin.site.register(Currency, CurrencyAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'hostel', 'customer', 'is_confirmed',
                    'is_checked_in', 'created', 'modified')   # db displays these fields
    # Filter through db with these fields
    list_filter = ('hostel', 'customer', 'is_confirmed', 'is_checked_in',)
    search_fields = ('hostel', 'customer',)
    ordering = ('hostel', 'customer', )
    readonly_fields = ("created", "modified", 'check_out')
    filter_horizontal = ()

    fieldsets = (
        ('Information', {'fields': ('hostel', 'customer', 'created', 'modified','check_out')}),
        ('Status', {'fields': ('is_confirmed', 'is_checked_in', 'is_history',)}),
    )

    actions = ['confirm_selected','unconfirm_selected', 'checkin_selected', 'checkout_selected']

    def confirm_selected(self, request, queryset):
        updated = queryset.update(is_confirmed=True)
        self.message_user(request, ngettext(
            '%d Reservation was successfully marked as Confirmed.',
            '%d Reservations were successfully marked as Confirmed.',
            updated,
        ) % updated, messages.SUCCESS)

    def unconfirm_selected(self, request, queryset):
        updated = queryset.update(is_confirmed=False)
        queryset.update(is_checked_in=False)
        queryset.update(is_history=False)
        self.message_user(request, ngettext(
            '%d Reservation was successfully unconfirmed.',
            '%d Reservations were successfully unconfirmed.',
            updated,
        ) % updated, messages.SUCCESS)

    def checkin_selected(self, request, queryset):
        updated = queryset.update(is_checked_in=True)
        queryset.update(is_confirmed=True)
        queryset.update(is_history=True)
        self.message_user(request, ngettext(
            '%d Reservation was successfully marked as checked-in.',
            '%d Reservations were successfully marked as checked-in.',
            updated,
        ) % updated, messages.SUCCESS)

    def checkout_selected(self, request, queryset):
        updated = queryset.update(is_checked_in=False)
        queryset.update(is_history=False)
        self.message_user(request, ngettext(
            '%d Reservation was successfully unchecked-in.',
            '%d Reservations were successfully unchecked-in.',
            updated,
        ) % updated, messages.SUCCESS)

    confirm_selected.short_description = "Confirm selected Reservation"
    unconfirm_selected.short_description = "Unconfirm selected Reservation"
    checkin_selected.short_description = "Check-in selected Reservation"
    checkout_selected.short_description = "Check-out selected Reservation"
admin.site.register(Reservation, ReservationAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
