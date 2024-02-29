def hotel_cost(num_nights):
    #Calculate the total cost for the hotel stay.
    
    hotel_price_per_night = 100  
    return num_nights * hotel_price_per_night

def plane_cost(city_flight):
    #Calculate the cost for the flight based on the chosen city.
    
    city_flight_costs = {
        "New York": 600,
        "Paris": 300,
        "Tokyo": 1000
        
    }
    
    if city_flight in city_flight_costs:
        return city_flight_costs[city_flight]
    else:
        return "City not found. Please choose a valid city for the flight."

def car_rental(rental_days):
    #Calculate the total cost of the car rental.
    
    daily_rental_cost = 50  
    return rental_days * daily_rental_cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    """Calculate the total cost for the holiday."""
    return hotel_cost + plane_cost + car_rental

def main():
    try:
        # ask for user input
        city_flight = input("Enter the city you will be flying to (e.g., New York, Paris, Tokyo): ")
        num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
        rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

        # Calculate costs
        hotel_total_cost = hotel_cost(num_nights)
        flight_total_cost = plane_cost(city_flight)
        car_total_cost = car_rental(rental_days)
        total_holiday_cost = holiday_cost(hotel_total_cost, flight_total_cost, car_total_cost)

        # Print holiday details
        print("\nHoliday Details:")
        print(f"City of Flight: {city_flight}")
        print(f"Hotel Cost: £{hotel_total_cost}")
        print(f"Flight Cost: £{flight_total_cost}")
        print(f"Car Rental Cost: £{car_total_cost}")
        print(f"Total Holiday Cost: £{total_holiday_cost}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for number of nights and rental days.")

if __name__ == "__main__":
    main()


