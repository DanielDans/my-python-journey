# freeCodeCamp code
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)
# freeCodeCamp project 2
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = base_price + service_charges + extra_charges - discount
    print('Final price of ticket:', final_price)
else:
    print('Ticket booking failed due to restrictions')
# freeCodeCamp project 3
distance_mi = 10 # miles
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True
if distance_mi == False:
    print(False)
elif distance_mi <= 1:
    if is_raining == True:
        print(False)
    else:
        print(True)
elif distance_mi <= 6:
    if is_raining == True:
        if has_bike == False:
            print(False)
    if is_raining == False:
        if has_bike == False:
            print(False)
        else:
            print(True)
elif distance_mi > 6:
    if has_car == True or has_ride_share_app == True:
        print(True)
    else:
        print(False)
# fun project
gabe = int(input('on a scale of 1-100, how gay is gabe: '))
if gabe == 100:
    print('exactly that')
elif gabe < 85:
    print('too little')
elif gabe > 100 or gabe < 1:
    print('follow the damn scale')
elif gabe >= 85 and gabe < 100:
    print('close')