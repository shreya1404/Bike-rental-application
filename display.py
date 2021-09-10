from bike_rented import BikeRental, Customer
import sqlite3
from datetime import  datetime

def main():
    shop = BikeRental(200)
    customer = Customer()
    while True:
        print("""
        ====== Two Wheeler Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $4
        3. Request a bike on daily basis $6
        4. Request a bike on weekly basis $30
        5. Return a bike
        6. Exit
        """)
        choice = input("Enter Your Choice:")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            shop.displaystock()

        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
            customer.rentalBasis = 1
            now = datetime.now()

        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2
            now = datetime.now()

        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3
            now = datetime.now()

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            cost=customer.bill
            customer.rentedbikes=customer.bikes
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
    print("Thank you for using the bike rental system.")
    AvailableBikes = shop.stock
    RentedBikes=customer.rentedbikes
    BookingDate=now.date()
    #BookingTime=now.time()
    RentedCost=cost
    print(AvailableBikes,RentedBikes,BookingDate,RentedCost)
    connection = sqlite3.connect("rental.db")
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO bike(AvailableBikes, RentedBikes, BookingDate, RentedCost) VALUES (?,?,?,?)",
        (AvailableBikes, RentedBikes, BookingDate, RentedCost))
    connection.commit()
if __name__=="__main__":
    main()
