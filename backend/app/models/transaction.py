from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    amount: float
    date: str
    category: str | None = None