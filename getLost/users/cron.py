from users.models import Reservation, RoomDetail
from django.utils import timezone
import datetime

def is_reservation_expired():
    #   Query all reservations in our database
    reservations = Reservation.objects.all()
    index = 0
    for res in reservations:
        index = index + 1
        if res.reservation_experation != None:
            if res.is_confirmed == False and res.is_checked_out == False:
                if res.reservation_experation < timezone.now():
                    roomdetails = RoomDetail.objects.get(
                    hostel=res.hostel)
                    res.delete()
                    roomdetails.occupied_beds = roomdetails.occupied_beds + 1
                    roomdetails.save()
    return "completed deleting Reservation at {}".format(timezone.now())


def check_out():
    #   Query all reservations in our database
    reservations = Reservation.objects.all()
    for reservation in reservations:
        # print(reservation.hostel)
        # print(reservation.customer)
        # print(reservation.is_confirmed)
        # print(reservation.is_checked_out)
        # print(reservation.confirmation_experation)
        if reservation.is_confirmed == True and reservation.confirmation_experation is not None and reservation.confirmation_experation < timezone.now() and reservation.is_checked_out == False:
            print("we made it here")
            print(reservation.customer)
            roomdetails = RoomDetail.objects.get(hostel=reservation.hostel)
            reservation.is_checked_out = True
            roomdetails.occupied_beds = roomdetails.occupied_beds + 1
            reservation.save()
            roomdetails.save()
    return "completed setting Reservation to checked out at {}".format(timezone.now())


# def check_out():
#     #   Query all reservations in our database
#     today = datetime.today().strftime('%Y-%m-%d')
#     reservations = Reservation.objects.filter(is_confirmed=True)

#     for reservation in reservations:
#         experation = reservation.confirmation_experation.strftime('%Y-%m-%d')
#         if experation < today:
#             reservation.is_checked_out = True
#             reservation.save()
#     return "completed setting Reservation to checked out at {}".format(timezone.now())

# at 3am you have to:
# --- reset occupied beds to 0 - 
# --- 
