# handlers/message_handler.py


import json
import logging
import os
import sys
import asyncio
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 表情生成器
from app.scripts.ImageGenerate.main import handle_ImageGenerate_group_message

# 群发消息
from app.scripts.SendAll.main import handle_SendAll_group_message

# 群管系统
from app.scripts.GroupManager.main import handle_GroupManager_group_message

# 编解码
from app.scripts.Crypto.main import handle_crypto_group_message

# ai对话
from app.scripts.AI.main import handle_ai_group_message

# 知识库
from app.scripts.QASystem.main import handle_qasystem_message_group

# 天气订阅
# from app.scripts.WeatherSubscribe.main import (
#     handle_WeatherSubscribe_task_Timer,
#     handle_WeatherSubscribe_task_Msg,
# )

# 课程表
from app.scripts.ClassTable.main import (
    handle_ClassTable_group_message,
    check_and_push_course_schedule,
)

# 关键词回复
from app.scripts.KeywordsReply.main import handle_KeywordsReply_group_message

# 黑名单
from app.scripts.BlacklistSystem.main import (
    handle_blacklist_message_group,
    handle_blacklist_request_event,
    handle_blacklist_group_notice,
)

# 入群欢迎和退群欢送
from app.scripts.WelcomeFarewell.main import (
    handle_WelcomeFarewell_group_notice,
    WelcomeFarewell_manage,
)

# 邀请链
from app.scripts.InviteChain.main import (
    handle_InviteChain_group_message,
    handle_InviteChain_group_notice,
)

# 违禁词
from app.scripts.BanWords.main import (
    handle_BanWords_group_message,
    handle_BanWords_response_message,
)

# 违禁词2
from app.scripts.BanWords2.main import handle_BanWords2_group_message

# QFNU追踪器
from app.scripts.QFNUTracker.main import (
    start_qfnu_tracker,
    handle_QFNUTracker_group_message,
)

# 群名片锁
from app.scripts.LockGroupCard.main import (
    handle_LockGroupCard_group_message,
)

# 软封禁
from app.scripts.SoftBan.main import SoftBan_main

# 收集阳光
from app.scripts.CollectTheSun.main import handle_CollectTheSun_group_message

# 自定义
from app.scripts.Custom.main import (
    handle_Custom_group_message,
)


# 词云
from app.scripts.WordCloud.main import (
    handle_WordCloud_group_message,
    wordcloud_task,
)

# 时间感知问候
from app.scripts.TimeAwareGreetings.main import handle_TimeAwareGreetings_group_message

# 夸夸AI
from app.scripts.KuaKuaAI.main import handle_KuaKuaAI_group_message

# 戳一戳
from app.scripts.PokePal.main import handle_PokePal_group_message

# 打断复读
from app.scripts.NoAddOne.main import handle_NoAddOne_group_message

# 考试教室查询
from app.scripts.QFNUBustExamClassroomFind.main import (
    handle_QFNUBustExamClassroomFind_group_message,
)

# 选课查询
from app.scripts.QFNUClassRegistrationCheck.main import (
    handle_QFNUClassRegistrationCheck_group_message,
    handle_QFNUClassRegistrationCheck_response_message,
)

# IP信息查询
from app.scripts.GetIPInfo.main import handle_GetIPInfo_group_message

# CET4
from app.scripts.CET4.main import handle_CET4_group_message

# Github卡片
from app.scripts.GithubCard.main import handle_GithubCard_group_message

# Bilibili推送
from app.scripts.BilibiliPush.main import (
    handle_BilibiliPush_group_message,
    check_live_and_dynamic,
    handle_BilibiliPush_meta_event,
)

# 群链接
from app.scripts.GroupLink.main import (
    handle_GroupLink_meta_event,
    handle_GroupLink_group_message,
)

# 二维码检测
from app.scripts.QRCodeInspector.main import (
    handle_QRCodeInspector_group_message,
    handle_QRCodeInspector_meta_event,
)

# 头衔自助服务
from app.scripts.TitleSelfService.main import (
    handle_TitleSelfService_group_message,
)

# 禁言轮盘
from app.scripts.MuteWheel.main import handle_MuteWheel_group_message

# 总开关
from app.switch import handle_GroupSwitch_group_message

# 菜单
from app.menu import handle_Menu_group_message

# 系统
from app.system import handle_System_group_message

# api
from app.api import *

# 配置
from app.config import *


# 处理消息事件的逻辑
async def handle_message_event(websocket, msg):
    try:
        # 处理群消息
        if msg.get("message_type") == "group":

            # 系统必需功能
            await handle_System_group_message(websocket, msg)  # 处理系统消息
            await handle_GroupSwitch_group_message(websocket, msg)  # 处理群组开关
            await handle_Menu_group_message(websocket, msg)  # 处理菜单

            # 依次执行scripts功能
            await handle_SendAll_group_message(websocket, msg)  # 处理群发消息
            await handle_ImageGenerate_group_message(websocket, msg)  # 表情生成器
            await handle_LockGroupCard_group_message(websocket, msg)  # 群名片锁
            await handle_GroupManager_group_message(websocket, msg)  # 群管系统
            await handle_crypto_group_message(websocket, msg)  # 编解码功能
            await handle_qasystem_message_group(websocket, msg)  # 处理知识库问答系统
            await handle_KeywordsReply_group_message(websocket, msg)  # 处理关键词回复
            await handle_blacklist_message_group(websocket, msg)  # 处理黑名单系统
            await handle_BanWords_group_message(websocket, msg)  # 处理违禁词系统
            await handle_BanWords2_group_message(websocket, msg)  # 处理违禁词系统(2)
            await WelcomeFarewell_manage(websocket, msg)  # 处理入群欢迎和退群欢送的管理
            await handle_InviteChain_group_message(websocket, msg)  # 处理邀请链
            await SoftBan_main(websocket, msg)  # 处理软封禁
            await handle_QFNUTracker_group_message(
                websocket, msg
            )  # 处理QFNU追踪器开关消息
            asyncio.create_task(handle_ai_group_message(websocket, msg))  # 处理ai群消息
            await handle_Custom_group_message(websocket, msg)  # 处理自定义群消息
            await handle_CollectTheSun_group_message(websocket, msg)  # 处理收集阳光
            await handle_NoAddOne_group_message(websocket, msg)  # 处理打断复读
            # await handle_WeatherSubscribe_task_Msg(websocket, msg)  # 处理天气订阅
            await handle_ClassTable_group_message(websocket, msg)  # 处理课程表
            await handle_WordCloud_group_message(websocket, msg)  # 处理词云
            await handle_KuaKuaAI_group_message(websocket, msg)  # 处理夸夸AI
            await handle_PokePal_group_message(websocket, msg)  # 处理戳一戳
            await handle_TimeAwareGreetings_group_message(
                websocket, msg
            )  # 处理时间感知问候
            await handle_QFNUBustExamClassroomFind_group_message(
                websocket, msg
            )  # 处理考试教室查询
            await handle_GetIPInfo_group_message(websocket, msg)  # 处理IP信息查询
            await handle_QFNUClassRegistrationCheck_group_message(
                websocket, msg
            )  # 处理选课查询
            await handle_CET4_group_message(websocket, msg)  # 处理CET4
            await handle_GithubCard_group_message(websocket, msg)  # 处理Github卡片
            await handle_BilibiliPush_group_message(websocket, msg)  # 处理Bilibili推送
            await handle_GroupLink_group_message(websocket, msg)  # 处理群链接
            await handle_QRCodeInspector_group_message(websocket, msg)  # 处理二维码检测
            await handle_TitleSelfService_group_message(
                websocket, msg
            )  # 处理头衔自助服务
            await handle_MuteWheel_group_message(websocket, msg)  # 处理禁言轮盘
        # 处理私聊消息
        elif msg.get("message_type") == "private":
            # 由于私聊风险较大，不处理私聊消息，仅占位
            pass

        else:
            logging.info(f"收到未知消息类型: {msg}")

    except KeyError as e:
        logging.error(f"处理消息事件的逻辑错误: {e}")


# 处理通知事件的逻辑
async def handle_notice_event(websocket, msg):

    # 处理通知
    if msg.get("post_type") == "notice":
        await handle_WelcomeFarewell_group_notice(
            websocket, msg
        )  # 处理入群欢迎和退群欢送的管理
        await handle_InviteChain_group_notice(websocket, msg)  # 处理邀请链
        await handle_blacklist_group_notice(websocket, msg)  # 处理黑名单检查


# 处理请求事件的逻辑
async def handle_request_event(websocket, msg):
    try:
        await handle_blacklist_request_event(websocket, msg)  # 处理黑名单加群请求事件
    except Exception as e:
        logging.error(f"处理请求事件的逻辑错误: {e}")


# 处理元事件的逻辑，每次心跳周期检查一次，用于启动时确保数据目录存在
async def handle_meta_event(websocket):
    try:
        await handle_BilibiliPush_meta_event(websocket)  # 处理哔哩哔哩推送元事件
        await handle_GroupLink_meta_event(websocket)  # 处理群链接元事件
    except Exception as e:
        logging.error(f"处理元事件的逻辑错误: {e}")


# 处理定时任务，每个心跳周期检查一次
async def handle_cron_task(websocket):
    try:
        await start_qfnu_tracker(websocket)  # QFNU追踪器
        await check_and_push_course_schedule(websocket)  # 课程表
        await wordcloud_task(websocket)  # 词云
        await check_live_and_dynamic(websocket)  # 检查哔哩哔哩直播和动态
        await handle_QRCodeInspector_meta_event(websocket)  # 处理二维码检测
    except Exception as e:
        logging.error(f"处理定时任务的逻辑错误: {e}")


# 处理回应消息
async def handle_response_message(websocket, message):
    try:
        msg = json.loads(message)
        if msg.get("status") == "ok":
            await handle_BanWords_response_message(websocket, message)
            await handle_QFNUClassRegistrationCheck_response_message(websocket, message)
    except Exception as e:
        logging.error(f"处理回应消息的逻辑错误: {e}")


# 处理ws消息
async def handle_message(websocket, message):
    try:
        msg = json.loads(message)

        # 处理回应消息
        if msg.get("status") == "ok":
            logging.info(f"收到回应消息：{msg}")
            await handle_response_message(websocket, message)

        # 处理事件
        if "post_type" in msg:
            logging.info(f"收到事件消息：{msg}")
            if msg["post_type"] == "message":
                # 处理消息事件
                await handle_message_event(websocket, msg)
            elif msg["post_type"] == "notice":
                # 处理通知事件
                await handle_notice_event(websocket, msg)
            elif msg["post_type"] == "request":
                # 处理请求事件
                await handle_request_event(websocket, msg)
            elif (
                msg["post_type"] == "meta_event"
                and msg["meta_event_type"] == "heartbeat"
            ):
                # 处理元事件
                await handle_meta_event(websocket)
                # 处理定时任务，每个心跳周期检查一次
                await handle_cron_task(websocket)
    except Exception as e:
        logging.error(f"处理ws消息的逻辑错误: {e}")
