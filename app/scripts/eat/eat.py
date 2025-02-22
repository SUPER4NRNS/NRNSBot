# script/Eat/main.py
# 示例脚本
# 本脚本写好了基本的函数，直接在函数中编写逻辑即可，必要的时候可以修改函数名
# 注意：Eat 是具体功能，请根据实际情况一键替换即可
# 注意：function 是函数名称，请根据实际情况一键替换即可

import logging
import os
import sys
import asyncio
import schedule
import time

# 添加项目根目录到sys.path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.config import owner_id
from app.api import *
from app.switch import load_switch, save_switch

tmassage = "【吃饭提醒小助手】附中20分钟后放学，西公寓/教餐就餐的同学请注意错峰吃饭时间。详情请输入：军训时间表/西公寓就餐错峰时间"
groupid001 = "146073608"
groupid002 = "826214748"
groupid003 = "696071864"

# 数据存储路径，实际开发时，请将Eat替换为具体的数据存放路径
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "Eat",
)


# 查看功能开关状态
def load_function_status(group_id):
    return load_switch(group_id, "function_status")


# 保存功能开关状态
def save_function_status(group_id, status):
    save_switch(group_id, "function_status", status)
    
    
# 定时任务: 每天11:20和17:20发送消息
def schedule_daily_messages(websocket):
    def send_message_task():
        asyncio.create_task(send_group_msg(websocket, groupid001, tmassage))
        asyncio.create_task(send_group_msg(websocket, groupid002, tmassage))
        asyncio.create_task(send_group_msg(websocket, groupid003, tmassage))

    # 定义每天11:20和17:20发送消息
    #schedule.every().day.at("05:43").do(send_message_task)
    schedule.every().day.at("11:30").do(send_message_task)
    schedule.every().day.at("16:50").do(send_message_task)

# 异步运行调度任务
async def run_schedule(websocket):
    schedule_daily_messages(websocket)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)  # 使用asyncio.sleep代替time.sleep


# 群消息处理函数
async def handle_Eat_group_message(websocket, msg):
    try:
        user_id = str(msg.get("user_id"))
        group_id = str(msg.get("group_id"))
        raw_message = str(msg.get("raw_message"))
        role = str(msg.get("sender", {}).get("role"))
        message_id = str(msg.get("message_id"))

    except Exception as e:
        logging.error(f"处理Eat群消息失败: {e}")
        return


# 群通知处理函数
async def handle_Eat_group_notice(websocket, msg):
    try:
        user_id = str(msg.get("user_id"))
        group_id = str(msg.get("group_id"))
        raw_message = str(msg.get("raw_message"))
        role = str(msg.get("sender", {}).get("role"))
        message_id = str(msg.get("message_id"))

    except Exception as e:
        logging.error(f"处理Eat群通知失败: {e}")
        return


# 私聊消息处理函数
async def handle_Eat_private_message(websocket, msg):
    try:
        user_id = str(msg.get("user_id"))
        raw_message = str(msg.get("raw_message"))

    except Exception as e:
        logging.error(f"处理xxx私聊消息失败: {e}")
        return


async def Eat_main(websocket, msg):

    # 确保数据目录存在
    os.makedirs(DATA_DIR, exist_ok=True)

    await handle_Eat_group_message(websocket, msg)
    await handle_Eat_group_notice(websocket, msg)
    await handle_Eat_private_message(websocket, msg)


#asyncio.create_task(run_schedule(websocket))
