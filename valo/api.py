import aiohttp
import discord
from .var import Token

class API:
    def __init__(self, bot : discord.Client):
        self.base = BaseAPI(bot)
        self.asia = AsiaAPI(bot)
        self.europe = EuropeAPI(bot)
        self.america = AmericaAPI(bot)


class BaseAPI:
    def __init__(self, bot : discord.Client):
        self._bot = bot
        self._url = None
        self._token = Token.API

    async def _get(self, url : str):
        async with aiohttp.ClientSession() as session:
            response = await session.get(f'{url}?api_key={self._token}')
            return await response.json()
    
    async def get_account(self, gameName : str, tagLine : str):
        url = f'{self._url}riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}'
        return await self._get(url)

    async def contents(self):
        url = f'{self._url}val/content/v1/contents'
        return await self._get(url)

    async def matchlists(self, puuid : str):
        url = f'{self._url}val/match/v1/matchlists/by-puuid/{puuid}'
        return await self._get(url)

class AsiaAPI(BaseAPI):
    def __init__(self, bot : discord.Client):
        super().__init__(bot)
        self._url = 'https://asia.api.riotgames.com/'


class AmericaAPI(BaseAPI):
    def __init__(self, bot : discord.Client):
        super().__init__(bot)
        self._url = 'https://americas.api.riotgames.com/'


class EuropeAPI(BaseAPI):
    def __init__(self, bot : discord.Client):
        super().__init__(bot)
        self._url = 'https://europe.api.riotgames.com/'
        