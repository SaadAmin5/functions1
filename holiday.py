#Calculate the total cost of Holiday. It includes the combined cost of hotel, plane and car.

# Input values from the user
city_flight = input('Enter the city you are flying to: ')
num_nights = int(input('Enter the number of nights you will be staying at the hotel: '))
rental_days = int(input('Enter the number of days you will be hiring car: '))

# Fixed costs
price_per_night = 50
rental_cost_per_day = 20

# Function to calculate hotel cost
def hotel_cost(num_nights, price_per_night):
    return num_nights * price_per_night

# Function to calculate plane cost based on city
def plane_cost(city_flight):
    if city_flight == 'London':
        return 90
    elif city_flight == 'Paris':
        return 50
    elif city_flight == 'New York':
        return 80
    elif city_flight == 'Amsterdam':
        return 60
    else:
        return 'City is not present'

# Function to calculate car rental cost
def car_rental(rental_days, rental_cost_per_day):
    return rental_days * rental_cost_per_day

# Function to calculate total holiday cost
def holiday_cost(num_nights, price_per_night, city_flight, rental_days, rental_cost_per_day):
    hotel_cost_val = hotel_cost(num_nights, price_per_night)
    plane_cost_val = plane_cost(city_flight)
    car_rental_cost_val = car_rental(rental_days, rental_cost_per_day)
    return hotel_cost_val + plane_cost_val + car_rental_cost_val

# Calculate and print individual costs
Hotel_Cost = hotel_cost(num_nights, price_per_night)
print('Hotel cost is:', Hotel_Cost)

Plane_Cost = plane_cost(city_flight)
print('Plane cost is:', Plane_Cost)

Car_Rental = car_rental(rental_days, rental_cost_per_day)
print('Car rental price is:', Car_Rental)

# Calculate and print total holiday cost
Total_Cost = holiday_cost(num_nights, price_per_night, city_flight, rental_days, rental_cost_per_day)
print('Total cost of holiday is:', Total_Cost)
