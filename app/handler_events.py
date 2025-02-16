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
from app.scripts.QASystem.main import handle_events as handle_QASystem_events
from app.scripts.ClassTable.main import handle_events as handle_ClassTable_events
from app.scripts.KeywordsReply.main import handle_events as handle_KeywordsReply_events
from app.scripts.BlacklistSystem.main import handle_events as handle_Blacklist_events
from app.scripts.WelcomeFarewell.main import (
    handle_events as handle_WelcomeFarewell_events,
)
from app.scripts.InviteChain.main import handle_events as handle_InviteChain_events
from app.scripts.BanWords.main import handle_events as handle_BanWords_events
from app.scripts.QFNUTracker.main import handle_events as handle_QFNUTracker_events
from app.scripts.LockGroupCard.main import handle_events as handle_LockGroupCard_events
from app.scripts.SoftBan.main import handle_events as handle_SoftBan_events
from app.scripts.Custom.main import handle_events as handle_Custom_events
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
from app.switch import handle_events as handle_Switch_events


# 处理回应消息
async def handle_response_message(websocket, message):
    try:
        msg = json.loads(message)  # 将字符串消息解析为字典
        if msg.get("status") == "ok":
            await handle_BanWords_events(websocket, msg)
            await handle_QFNUClassRegistrationCheck_events(websocket, msg)
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
        await handle_Switch_events(websocket, msg)

        # 功能模块事件处理
        await handle_ImageGenerate_events(websocket, msg)
        await handle_SendAll_events(websocket, msg)
        await handle_GroupManager_events(websocket, msg)
        await handle_Crypto_events(websocket, msg)
        await handle_QASystem_events(websocket, msg)
        await handle_ClassTable_events(websocket, msg)
        await handle_KeywordsReply_events(websocket, msg)
        await handle_Blacklist_events(websocket, msg)
        await handle_WelcomeFarewell_events(websocket, msg)
        await handle_InviteChain_events(websocket, msg)
        await handle_BanWords_events(websocket, msg)
        await handle_QFNUTracker_events(websocket, msg)
        await handle_LockGroupCard_events(websocket, msg)
        await handle_SoftBan_events(websocket, msg)
        await handle_Custom_events(websocket, msg)
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
