from asyncio import ensure_future, wait, get_event_loop
from aiohttp import ClientSession


async def initiate_request(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)


tasks = []
for i in range(5):
    task = ensure_future(initiate_request('http://bing.com'))
    tasks.append(task)


loop = get_event_loop()
loop.run_until_complete(wait(tasks))
