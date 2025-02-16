# handlers/message_handler.py


import json
import logging
import os
import sys
import asyncio
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 统一从各模块导入事件处理器
from app.scripts.ImageGenerate.main import handle_events as handle_ImageGenerate_events
from app.scripts.SendAll.main import handle_events as handle_SendAll_events
from app.scripts.GroupManager.main import handle_events as handle_GroupManager_events
from app.scripts.Crypto.main import handle_events as handle_Crypto_events
from app.scripts.AI.main import handle_events as handle_AI_events
from app.scripts.QASystem.main import handle_events as handle_QASystem_events
from app.scripts.ClassTable.main import handle_events as handle_ClassTable_events
from app.scripts.KeywordsReply.main import handle_events as handle_KeywordsReply_events
from app.scripts.BlacklistSystem.main import handle_events as handle_Blacklist_events
from app.scripts.WelcomeFarewell.main import (
    handle_events as handle_WelcomeFarewell_events,
)
from app.scripts.InviteChain.main import handle_events as handle_InviteChain_events
from app.scripts.BanWords.main import handle_events as handle_BanWords_events
from app.scripts.BanWords2.main import handle_events as handle_BanWords2_events
from app.scripts.QFNUTracker.main import handle_events as handle_QFNUTracker_events
from app.scripts.LockGroupCard.main import handle_events as handle_LockGroupCard_events
from app.scripts.SoftBan.main import handle_events as handle_SoftBan_events
from app.scripts.CollectTheSun.main import handle_events as handle_CollectTheSun_events
from app.scripts.Custom.main import handle_events as handle_Custom_events
from app.scripts.WordCloud.main import handle_events as handle_WordCloud_events
from app.scripts.TimeAwareGreetings.main import (
    handle_events as handle_TimeAwareGreetings_events,
)
from app.scripts.KuaKuaAI.main import handle_events as handle_KuaKuaAI_events
from app.scripts.PokePal.main import handle_events as handle_PokePal_events
from app.scripts.NoAddOne.main import handle_events as handle_NoAddOne_events
from app.scripts.QFNUBustExamClassroomFind.main import (
    handle_events as handle_QFNUBustExamClassroomFind_events,
)
from app.scripts.QFNUClassRegistrationCheck.main import (
    handle_events as handle_QFNUClassRegistrationCheck_events,
)
from app.scripts.GetIPInfo.main import handle_events as handle_GetIPInfo_events
from app.scripts.CET4.main import handle_events as handle_CET4_events
from app.scripts.GithubCard.main import handle_events as handle_GithubCard_events
from app.scripts.BilibiliPush.main import handle_events as handle_BilibiliPush_events
from app.scripts.GroupLink.main import handle_events as handle_GroupLink_events
from app.scripts.QRCodeInspector.main import (
    handle_events as handle_QRCodeInspector_events,
)
from app.scripts.TitleSelfService.main import (
    handle_events as handle_TitleSelfService_events,
)
from app.scripts.MuteWheel.main import handle_events as handle_MuteWheel_events

# 系统模块
from app.system import handle_events as handle_System_events
from app.menu import handle_events as handle_Menu_events
from app.switch import handle_events as handle_Switch_events


# 处理消息事件的逻辑
async def handle_message_event(websocket, msg):
    try:
        # 处理群消息
        if msg.get("message_type") == "group":

            # 系统必需功能
            await handle_System_events(websocket, msg)  # 处理系统消息
            await handle_Switch_events(websocket, msg)  # 处理群组开关
            await handle_Menu_events(websocket, msg)  # 处理菜单

            # 依次执行scripts功能
            await handle_SendAll_events(websocket, msg)  # 处理群发消息
            await handle_ImageGenerate_events(websocket, msg)  # 表情生成器
            await handle_LockGroupCard_events(websocket, msg)  # 群名片锁
            await handle_GroupManager_events(websocket, msg)  # 群管系统
            await handle_Crypto_events(websocket, msg)  # 编解码功能
            await handle_QASystem_events(websocket, msg)  # 处理知识库问答系统
            await handle_KeywordsReply_events(websocket, msg)  # 处理关键词回复
            await handle_Blacklist_events(websocket, msg)  # 处理黑名单系统
            await handle_BanWords_events(websocket, msg)  # 处理违禁词系统
            await handle_BanWords2_events(websocket, msg)  # 处理违禁词系统(2)
            await handle_WelcomeFarewell_events(
                websocket, msg
            )  # 处理入群欢迎和退群欢送的管理
            await handle_InviteChain_events(websocket, msg)  # 处理邀请链
            await handle_SoftBan_events(websocket, msg)  # 处理软封禁
            await handle_QFNUTracker_events(websocket, msg)  # 处理QFNU追踪器开关消息
            asyncio.create_task(handle_AI_events(websocket, msg))  # 处理ai群消息
            await handle_Custom_events(websocket, msg)  # 处理自定义群消息
            await handle_CollectTheSun_events(websocket, msg)  # 处理收集阳光
            await handle_NoAddOne_events(websocket, msg)  # 处理打断复读
            # await handle_WeatherSubscribe_task_Msg(websocket, msg)  # 处理天气订阅
            await handle_ClassTable_events(websocket, msg)  # 处理课程表
            await handle_WordCloud_events(websocket, msg)  # 处理词云
            await handle_KuaKuaAI_events(websocket, msg)  # 处理夸夸AI
            await handle_PokePal_events(websocket, msg)  # 处理戳一戳
            await handle_TimeAwareGreetings_events(websocket, msg)  # 处理时间感知问候
            await handle_QFNUBustExamClassroomFind_events(
                websocket, msg
            )  # 处理考试教室查询
            await handle_GetIPInfo_events(websocket, msg)  # 处理IP信息查询
            await handle_QFNUClassRegistrationCheck_events(
                websocket, msg
            )  # 处理选课查询
            await handle_CET4_events(websocket, msg)  # 处理CET4
            await handle_GithubCard_events(websocket, msg)  # 处理Github卡片
            await handle_BilibiliPush_events(websocket, msg)  # 处理Bilibili推送
            await handle_GroupLink_events(websocket, msg)  # 处理群链接
            await handle_QRCodeInspector_events(websocket, msg)  # 处理二维码检测
            await handle_TitleSelfService_events(websocket, msg)  # 处理头衔自助服务
            await handle_MuteWheel_events(websocket, msg)  # 处理禁言轮盘
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
        await handle_WelcomeFarewell_events(
            websocket, msg
        )  # 处理入群欢迎和退群欢送的管理
        await handle_InviteChain_events(websocket, msg)  # 处理邀请链
        await handle_Blacklist_events(websocket, msg)  # 处理黑名单检查


# 处理请求事件的逻辑
async def handle_request_event(websocket, msg):
    try:
        await handle_Blacklist_events(websocket, msg)  # 处理黑名单加群请求事件
    except Exception as e:
        logging.error(f"处理请求事件的逻辑错误: {e}")


# 处理元事件的逻辑，每次心跳周期检查一次，用于启动时确保数据目录存在
async def handle_meta_event(websocket):
    try:
        await handle_BilibiliPush_events(websocket)  # 处理哔哩哔哩推送元事件
        await handle_GroupLink_events(websocket)  # 处理群链接元事件
    except Exception as e:
        logging.error(f"处理元事件的逻辑错误: {e}")


# 处理定时任务，每个心跳周期检查一次
async def handle_cron_task(websocket):
    try:
        await handle_QFNUTracker_events(websocket)  # QFNU追踪器
        await handle_ClassTable_events(websocket)  # 课程表
        await handle_WordCloud_events(websocket)  # 词云
        await handle_BilibiliPush_events(websocket)  # 检查哔哩哔哩直播和动态
        await handle_QRCodeInspector_events(websocket)  # 处理二维码检测
    except Exception as e:
        logging.error(f"处理定时任务的逻辑错误: {e}")


# 处理回应消息
async def handle_response_message(websocket, message):
    try:
        msg = json.loads(message)
        if msg.get("status") == "ok":
            await handle_BanWords_events(websocket, message)
            await handle_QFNUClassRegistrationCheck_events(websocket, message)
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
            return

        logging.info(f"收到事件消息：{msg}")

        # 系统基础功能
        await handle_System_events(websocket, msg)
        await handle_Menu_events(websocket, msg)
        await handle_Switch_events(websocket, msg)

        # 功能模块事件处理
        await handle_ImageGenerate_events(websocket, msg)
        await handle_SendAll_events(websocket, msg)
        await handle_GroupManager_events(websocket, msg)
        await handle_Crypto_events(websocket, msg)
        await handle_AI_events(websocket, msg)
        await handle_QASystem_events(websocket, msg)
        await handle_ClassTable_events(websocket, msg)
        await handle_KeywordsReply_events(websocket, msg)
        await handle_Blacklist_events(websocket, msg)
        await handle_WelcomeFarewell_events(websocket, msg)
        await handle_InviteChain_events(websocket, msg)
        await handle_BanWords_events(websocket, msg)
        await handle_BanWords2_events(websocket, msg)
        await handle_QFNUTracker_events(websocket, msg)
        await handle_LockGroupCard_events(websocket, msg)
        await handle_SoftBan_events(websocket, msg)
        await handle_CollectTheSun_events(websocket, msg)
        await handle_Custom_events(websocket, msg)
        await handle_WordCloud_events(websocket, msg)
        await handle_TimeAwareGreetings_events(websocket, msg)
        await handle_KuaKuaAI_events(websocket, msg)
        await handle_PokePal_events(websocket, msg)
        await handle_NoAddOne_events(websocket, msg)
        await handle_QFNUBustExamClassroomFind_events(websocket, msg)
        await handle_QFNUClassRegistrationCheck_events(websocket, msg)
        await handle_GetIPInfo_events(websocket, msg)
        await handle_CET4_events(websocket, msg)
        await handle_GithubCard_events(websocket, msg)
        await handle_BilibiliPush_events(websocket, msg)
        await handle_GroupLink_events(websocket, msg)
        await handle_QRCodeInspector_events(websocket, msg)
        await handle_TitleSelfService_events(websocket, msg)
        await handle_MuteWheel_events(websocket, msg)

    except Exception as e:
        logging.error(f"处理ws消息的逻辑错误: {e}")
