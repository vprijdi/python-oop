import pandas as pd


class Hotel:
    """
    Represents a hotel and provides methods to interact with hotel data.

    This class reads hotel data from a CSV file into a shared DataFrame and
    provides methods to view hotel listings and book individual hotels.
    """

    hotels_df = pd.read_csv("data/hotels.csv")

    def __init__(self, hotel_id):
        """
        Initialize a Hotel object with the data from hotel database.

        :param hotel_id: str
            The unique identifier for a hotel to retrieve.
        :raises ValueError:
            If no hotel with provided ID was found.
        """

        row = Hotel.hotels_df[Hotel.hotels_df["id"] == hotel_id]

        if row.empty:
            raise ValueError(f"Hotel with ID {hotel_id} not found.")

        self.hotel_id = hotel_id
        self.hotel_name = row["name"].values[0]
        self.city = row["city"].values[0]
        self.capacity = row["capacity"].values[0]
        self.available = row["available"].values[0].lower() == "yes"

    @staticmethod
    def view_hotels():
        """
        Display the current list of hotels in the database.

        This method prints the internal DataFrame containing all hotel records.
        Does not return any value.
        """
        print(Hotel.hotels_df)

    def book(self):
        """
        Books the current hotel if available.

        This method marks the hotel as unavailable and updates the hotel database.
        It writes the updated availability status to 'hotels.csv'.

        :raises NoAvailabilityException:
            If the hotel is already fully booked (not available).
        """

        if not self.available:
            raise NoAvailabilityException(self.hotel_name)

        self.available = False
        Hotel.hotels_df.loc[Hotel.hotels_df["id"] == self.hotel_id, "available"] = "yes" \
            if self.available else "no"
        Hotel.hotels_df.to_csv("hotels.csv", index=False)


class ReservationTicket:
    """
    Reservation ticket for a customer booking a hotel.

    Stores customer name and the associated hotel object.
    """

    def __init__(self, customer_name, hotel_object):
        """
        Initialize a ReservationTicket.

        :param customer_name: str
            Name of the customer making a reservation.
        :param hotel_object: Hotel
            The Hotel object that has been booked.
        """

        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        """
        Generate a formatted reservation ticket.

        :return: str
            A formatted string containing information about a reservation.
        """

        return f"""
Thank you for your reservation!
Here is your booking data:
Name: {self.customer_name}
Hotel Name: {self.hotel.hotel_name}
"""


class NoAvailabilityException(Exception):
    """Exception raised when attempting to book a hotel that has no availability."""

    def __init__(self, hotel_name):
        """
        Initialize an exception with a custom message.

        :param hotel_name: str
            The name of the hotel that has no availability.
        """

        self.hotel_name = hotel_name
        super().__init__(f"{hotel_name} has no availability")
