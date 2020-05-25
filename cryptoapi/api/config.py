class Config:

    def __init__(self) -> None:
        self.BASE_HTTP_URL: str = 'https://api.apikey.io/api/v1'
        self.BASE_TESTNET_HTTP_URL: str = 'https://testnet-api.apikey.io/api/v1'
        self.BASE_WEB_HOOKS_URL: str = 'https://api.apikey.io/whooks-api/'
        self.WS_BASE_URL: str = 'wss://api.apikey.io/ws/'
