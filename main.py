import pandas as pd
from classes.Hotel import Hotel, ReservationTicket
from classes.CreditCard import CreditCard


def main():
    df = pd.read_csv("data/hotels.csv")

    # TODO: remove this line
    print(df)

    hotel_id = int(input("Input hotel id: "))
    hotel = Hotel(hotel_id)

    if hotel.available:
        credit_card = CreditCard("1234")
        if credit_card.validate(expiration='12/26', holder='JOHN SMITH', cvc='123'):
            customer_name = input("Enter your name: ")
            hotel.book()
            ticket = ReservationTicket(customer_name, hotel)
            print(ticket.generate())


main()
