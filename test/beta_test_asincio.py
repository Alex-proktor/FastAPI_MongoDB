import asyncio
import time
import aiohttp
from codetiming import Timer


async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()


async def main():
    work_queue = asyncio.Queue()
    start = time.time()

    for url in [
        "http://127.0.0.1:8000/users?",
        "http://127.0.0.1:8000/users?age=23&company=Yandex&name=Kyle%20Boyle",
        "http://127.0.0.1:8000/users?age=23&company=Yandex&name=Kyle%20Boyle",
        "http://127.0.0.1:8000/users?age=23&company=Yandex&name=Kyle%20Boyle",
        "http://127.0.0.1:8000/users?age=23&company=Yandex&name=Kyle%20Boyle",
        "http://127.0.0.1:8000/users?age=23&company=Yandex&name=Kyle%20Boyle",
        "http://127.0.0.1:8000/users?age=23&company=Yandex&name=Kyle%20Boyle",
    ]:
        await work_queue.put(url)

    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(task("1", work_queue)),
            asyncio.create_task(task("2", work_queue)),
            asyncio.create_task(task("3", work_queue)),
            asyncio.create_task(task("4", work_queue)),
            asyncio.create_task(task("5", work_queue)),
        )

    stop = time.time() - start
    print('All time: ', round(stop, 0), 'sec')


if __name__ == "__main__":
    asyncio.run(main())
