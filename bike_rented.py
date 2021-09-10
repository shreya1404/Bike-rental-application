import datetime
class BikeRental:

    def __init__(self, stock=None):
        self.stock = stock

    def displaystock(self):
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def rentBikeOnHourlyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $4 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now.hour

    def rentBikeOnDailyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $6 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now.hour

    def rentBikeOnWeeklyBasis(self, n):
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $30 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now.hour

    def returnBike(self, request):
        rentalTime, rentalBasis, bikes = request
        bill = 0
        if rentalTime and rentalBasis and bikes:
            self.stock += bikes
            if rentalBasis == 1:
                bill = rentalTime * 300 * bikes

            elif rentalBasis == 2:
                bill = rentalTime * 450 * bikes

            elif rentalBasis == 3:
                bill = rentalTime * 2250 * bikes

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        self.rentedbikes=0

    def requestBike(self):
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0