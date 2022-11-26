#!/usr/bin/env python3
import signal
import asyncio
import logging

from bilibiliq.auth import Auth
from bilibiliq.rest.message.model import Image
from bilibiliq.rest.message import MessageClient
from bilibiliq.rest.message.event import (
    Event,
    AtEvent,
    LikeEvent,
    ReplyEvent,
    RecallEvent,
    MessageEvent,
    SystemNotifyEvent,
)

# 用你自己的方式获取 Web 的 Auth
auth = Auth.load_from_file(uid=1025582085)
client = MessageClient(auth)


@client.handle()
async def callback(event: Event, client: MessageClient):
    if isinstance(event, RecallEvent):
        message = event.message
        s = "".join(str(i) for i in message.content)  # type: ignore
        logging.info(f"{event.sender_uid} 撤回了一条消息：{s}")
    elif isinstance(event, MessageEvent):
        if len(event.content) == 1 and isinstance(event.content[0], Image):
            logging.info(f"{event.sender_uid} 发送了一张图片：{event.content[0].url}")
        else:
            msg = ''.join(str(i) for i in event.content)
            logging.info(f"{event.sender_uid} 发送了一条消息：{msg}")
            if msg == "/image":
                with open(
                    "./example.png",
                    "rb",
                ) as f:
                    image = await client.upload_image(f.read())
                await client.send_msg(event.sender_uid, 2, image)
            elif msg.startswith("/echo"):
                await client.send_msg(event.sender_uid, 1, msg[5:])
    elif isinstance(event, (ReplyEvent, AtEvent)):
        msg = ''.join(str(i) for i in event.item.source_content)
        is_reply = isinstance(event, ReplyEvent)
        logging.info(
            f"{event.user.nickname}（UID：{event.sender_uid}）"
            f"{'等人' if is_reply and event.is_multi else ''}"
            f"{'回复' if is_reply else '@'}了你：{msg}"
        )
    elif isinstance(event, LikeEvent):
        logging.info(
            f"{event.users[0].nickname}（UID：{event.sender_uid}）"
            f"{'等人' if len(event.users)>1 else ''}点赞，共 {event.counts} 个赞"
        )
    elif isinstance(event, SystemNotifyEvent):
        logging.info(f"收到系统通知：\n标题：{event.title}\n内容：{event.content}")


async def run():
    # client.add_handler(callback)
    await client.start_fetch_service()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    close = asyncio.Event()

    def shutdown(sig, frame):
        close.set()

    for sign in {
        signal.SIGINT,
        signal.SIGTERM,
    }:
        signal.signal(sign, shutdown)

    async def wait_cleanup():
        await close.wait()
        await client.close()

    loop = asyncio.get_event_loop()
    loop.create_task(run())
    loop.run_until_complete(wait_cleanup())
