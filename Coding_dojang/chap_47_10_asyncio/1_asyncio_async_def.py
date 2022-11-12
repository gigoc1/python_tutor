import asyncio
from PyQt5.QtCore import *
import time
 
async def hello():    # async def로 네이티브 코루틴을 만듦
    while True:
        cur_time=QTime.currentTime()
        print('Hello, world!:'+cur_time.toString())
        time.sleep(0.5)
 
loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
loop.run_until_complete(hello())    # hello가 끝날 때까지 기다림
loop.close()                        # 이벤트 루프를 닫음