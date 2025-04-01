import pandas as pd


class CreditCard:
    df = pd.read_csv("../data/cards.csv")

    def __init__(self, number):
        pass

    def validate(self, expiration, holder, cvc):
        pass