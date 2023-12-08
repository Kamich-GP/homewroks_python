from pydantic import BaseModel
from typing import Optional, List, Dict

class User(BaseModel):
    name: List[str]
    mail: str
    adress: str

class Banks(BaseModel):
    name: User
    rating: int
    opened: str

class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: Banks

class Balance(BaseModel):
    card: Cards
    amount: int
    currency: int