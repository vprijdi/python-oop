import pandas as pd


class Hotel:
    hotels_df = pd.read_csv("hotels.csv")

    def __init__(self, hotel_id):
        row = Hotel.hotels_df[Hotel.hotels_df["id"] == hotel_id]

        if row.empty:
            raise ValueError(f"Hotel with ID {hotel_id} not found.")

        self.hotel_id = hotel_id
        self.hotel_id = row["id"].values[0]
        self.hotel_name = row["name"].values[0]
        self.city = row["city"].values[0]
        self.capacity = row["capacity"].values[0]
        self.available = row["available"].values[0].lower() == "yes"

    @staticmethod
    def view_hotels():
        print(Hotel.hotels_df)

    def book(self):
        if not self.available:
            raise NoAvailabilityException(self.hotel_name)

        self.available = False
        Hotel.hotels_df.loc[Hotel.hotels_df["id"] == self.hotel_id, "available"] = "yes" \
            if self.available else "no"
        Hotel.hotels_df.to_csv("hotels.csv", index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.name = customer_name
        self.hotel = hotel_object

    def generate(self):
        pass


class NoAvailabilityException(Exception):
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        super().__init__(f"{hotel_name} has no availability")
