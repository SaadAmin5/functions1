#Calculate the total cost of Holiday. It includes the combined cost of hotel, plane and car.

city_flight=input('Enter the city you are flying to: ')
num_nights= int(input('Enter the number of nights you will be staying at the hotel: '))
rental_days= int(input('Enter the number of days you will be hiring car: '))



price_per_night=50

def hotel_cost(num_nights):
    total_cost_hotel=num_nights * price_per_night
    return total_cost_hotel

Hotel_Cost=hotel_cost(num_nights)  #or print(hotel_cost(num_nights))
print('Hotel cost is: ', Hotel_Cost)



def plane_cost(city_flight):
    
    if city_flight=='London':
        flight_cost=90
        return flight_cost  #or  print(flight_cost)
        
    elif city_flight=='Paris':
        flight_cost=50
        return flight_cost
        
    elif city_flight=='New York':
        flight_cost=80
        return flight_cost
        
    elif city_flight=='Amsterdam':
        flight_cost=60
        return flight_cost
        
    else:
        return 'City is not present'

Plane_Cost=plane_cost(city_flight)
print('Plane cost is: ', Plane_Cost)



rental_cost_per_day=20

def car_rental (rental_days):
    total_cost_car_rental =rental_days * rental_cost_per_day
    return total_cost_car_rental

Car_Rental= car_rental(rental_days)
print('Car rental price is: ', Car_Rental)



def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost_holidays=Hotel_Cost + Plane_Cost + Car_Rental
    return total_cost_holidays

Total_Cost=holiday_cost(hotel_cost, plane_cost, car_rental)  #or print(holiday_cost(hotel_cost, plane_cost, car_rental))
print('Total cost of holiday is: ', Total_Cost)
