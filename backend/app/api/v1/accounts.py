from fastapi import APIRouter

router = APIRouter()

@router.get("/accounts")
def get_accounts():
    return [
        {"id": "1", "name": "Checking", "balance": 1000.0},
        {"id": "2", "name": "Savings", "balance": 5000.0},
    ]