from pydantic import BaseModel


class Dealerproduct(BaseModel):
    id: int
    product_key: str
    price: float
    product_url: str
    product_name: str
    date: str
    dealer_id: int
