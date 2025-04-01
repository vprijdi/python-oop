import pandas as pd
from Hotel import Hotel, ReservationTicket


def main():
    df = pd.read_csv("hotels.csv")

    # TODO: remove this line
    print(df)

    hotel_id = int(input("Input hotel id: "))
    hotel = Hotel(hotel_id)


    if hotel.available:
        customer_name = input("Enter your name: ")
        hotel.book()
        ticket = ReservationTicket(customer_name, hotel)
        print(ticket.generate())


main()
