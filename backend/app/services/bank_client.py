class BankClient:
    def __init__(self):
        pass

    async def fetch_accounts(self):
        raise NotImplementedError

    async def fetch_transactions(self, account_id: str):
        raise NotImplementedError