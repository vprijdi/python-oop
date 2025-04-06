import pandas as pd


# TODO: add documentation


class CreditCard:
    cards_df = pd.read_csv("data/cards.csv", dtype=str)

    def __init__(self, number: str):
        self.number = number

    def validate(self, expiration: str, holder: str, cvc: str):
        card_data = CreditCard.cards_df[CreditCard.cards_df["number"] == self.number]

        if card_data.empty:
            return False

        return (
                card_data["expiration"].values[0] == expiration
                and card_data["cvc"].values[0] == cvc
                and card_data["holder"].values[0] == holder
        )


class SecureCreditCard(CreditCard):
    secure_df = pd.read_csv("data/card_security.csv", dtype=str)

    def authenticate(self, given_password):
        password = SecureCreditCard.secure_df[
            SecureCreditCard.secure_df["number"] == self.number, "password"
        ].values[0]
        return password == given_password
