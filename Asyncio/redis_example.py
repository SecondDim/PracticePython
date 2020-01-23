import time
import asyncio
import redis


def now(): return time.time()


def get_redis():
    connection_pool = redis.ConnectionPool(host='127.0.0.1', db=9)
    return redis.Redis(connection_pool=connection_pool)


rcon = get_redis()


async def worker():
    print('Start worker')

    while True:
        start = now()
        task = rcon.rpop("queue")
        if not task:
            await asyncio.sleep(1)
            continue
        print('Wait ', int(task))
        await asyncio.sleep(int(task))
        print('Done ', task, now() - start)


def main():
    asyncio.ensure_future(worker())
    asyncio.ensure_future(worker())

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt as e:
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()


if __name__ == '__main__':
    main()
