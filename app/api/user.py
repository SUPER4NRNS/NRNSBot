import json
import websocket
import logging

from config import *


async def set_qq_profile(websocket, nickname, personal_note, sex):
    """
    设置账号信息
    """
    try:
        message = {
            "action": "set_qq_profile",
            "params": {
                "nickname": nickname,
                "personal_note": personal_note,
                "sex": sex,
            },
        }
        await websocket.send(json.dumps(message))
        return True
    except Exception as e:
        logging.error(f"[API]设置账号信息失败: {e}")
        return False


async def ArkSharePeer(websocket, group_id, user_id, phoneNumber):
    """
    获取推荐好友/群聊卡片
    """
    try:
        message = {
            "action": "ArkSharePeer",
            "params": {
                "group_id": group_id,
                "user_id": user_id,
                "phoneNumber": phoneNumber,
            },
        }
        await websocket.send(json.dumps(message))
        return True
    except Exception as e:
        logging.error(f"[API]获取推荐好友/群聊卡片失败: {e}")
        return False


async def ArkShareGroup(websocket, group_id):
    """
    获取推荐群聊卡片
    """
    try:
        message = {
            "action": "ArkShareGroup",
            "params": {"group_id": group_id},
        }
        await websocket.send(json.dumps(message))
        return True
    except Exception as e:
        logging.error(f"[API]获取推荐群聊卡片失败: {e}")
        return False


async def set_online_status(websocket, status, ext_status, battery_status):
    """
    设置在线状态
    """
    try:
        message = {
            "action": "set_online_status",
            "params": {
                "status": status,
                "ext_status": ext_status,
                "battery_status": battery_status,
            },
        }
        await websocket.send(json.dumps(message))
        return True
    except Exception as e:
        logging.error(f"[API]设置在线状态失败: {e}")
        return False


async def get_friends_with_category(websocket):
    """
    获取好友分组列表
    """
    try:
        message = {"action": "get_friends_with_category"}
        await websocket.send(json.dumps(message))
        return True
    except Exception as e:
        logging.error(f"[API]获取好友分组列表失败: {e}")
        return False


async def set_qq_avatar(websocket, file):
    """
    设置头像
    """
    try:
        message = {
            "action": "set_qq_avatar",
            "params": {"file": file},
            "echo": "set_qq_avatar",
        }
        await websocket.send(json.dumps(message))
        return True
    except Exception as e:
        logging.error(f"[API]设置头像失败: {e}")
        return False
