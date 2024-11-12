from typing import Union
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


food_items = {
    'indian' : [ "Samosa", "Dosa" ],
    'american' : [ "Hot Dog", "Apple Pie"],
    'italian' : [ "Ravioli", "Pizza"]
}

class AvaliableCusine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


@app.get("/")
def welcome():
    return f"Hello welcome to the app"

@app.get("/food/{cusine}")
def get_food(cusine: AvaliableCusine):
    return f"{food_items[cusine]}"
