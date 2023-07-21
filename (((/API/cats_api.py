from API.base import BaseApi


class CatsApi(BaseApi):
    async def get_waifu(self, category: str):
        answer = await self.get(f'https://cdn2.thecatapi.com/images/{id}.jpg')
        return answer['url']


cats_api = CatsApi()