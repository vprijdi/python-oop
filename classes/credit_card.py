import pandas as pd


class CreditCard:
    """
    Validate credit card information against a CSV database.

    Provides functionality to validate card details such as expiration date, holder name,
    and CVC.

    :ivar cards_df: pandas.DataFrame
        DataFrame containing credit card data loaded from a CSV file.
    """

    cards_df = pd.read_csv("data/cards.csv", dtype=str)

    def __init__(self, number: str):
        """
        Initialize a credit card object with a card number.

        :param number: str
            The credit card number to validate.
        """

        self.number = number

    def validate(self, expiration: str, holder: str, cvc: str):
        """
        Validates credit card expiration date, holder name, and CVC.

        :param expiration: str
            Expiration date to validate.
        :param holder: str
            Holder name to validate.
        :param cvc: str
            CVC to validate.
        :return: bool
            True if expiration date, holder name, and CVC match.
            False otherwise, or if the card data is empty.
        """

        card_data = CreditCard.cards_df[CreditCard.cards_df["number"] == self.number]

        if card_data.empty:
            return False

        return (
                card_data["expiration"].values[0] == expiration
                and card_data["cvc"].values[0] == cvc
                and card_data["holder"].values[0] == holder
        )


class SecureCreditCard(CreditCard):
    """
    Secure version of CreditCard class.

    Extends CreditCard class to add password-based authentication
    functionality from a separate database.

    :ivar secure_df: pandas.DataFrame
        DataFrame containing password data for credit cards.
    """

    secure_df = pd.read_csv("data/card_security.csv", dtype=str)

    def authenticate(self, given_password):
        """
        Authenticate a credit card using a password.

        :param given_password: str
            Password provided for authentication.
        :return: bool
            True if password matches the one in the database, False otherwise.
        """

        password = SecureCreditCard.secure_df[
            SecureCreditCard.secure_df["number"] == self.number, "password"
        ].values[0]
        return password == given_password
