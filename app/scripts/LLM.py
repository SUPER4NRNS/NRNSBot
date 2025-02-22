# script/LLM/LLM.py

import json
import logging
from typing import Union, Tuple
from openai import OpenAI
from .config import (
    MODEL_CONFIG,
    SYSTEM_PROMPT,
    DEFAULT_MODEL,
    SAFETY_CONFIG
)

logger = logging.getLogger(__name__)

class LLMService:
    """智能模型服务核心类"""
    
    def __init__(self, model_type: str = DEFAULT_MODEL):
        """
        初始化模型服务
        
        :param model_type: 模型类型，从config.MODEL_CONFIG读取
        """
        self.model_type = model_type
        self.model_config = self._validate_config()
        self.client = OpenAI(
            api_key=self.model_config["api_key"],
            base_url=self.model_config["base_url"]
        )
    
    def _validate_config(self) -> dict:
        """配置验证增强版"""
        if self.model_type not in MODEL_CONFIG:
            available = ", ".join(MODEL_CONFIG.keys())
            raise ValueError(f"无效模型类型 '{self.model_type}'，可用模型：{available}")
        
        config = MODEL_CONFIG[self.model_type]
        required_keys = {"api_key", "base_url", "model_name"}
        missing = [k for k in required_keys if k not in config]
        if missing:
            raise KeyError(f"模型 '{self.model_type}' 缺失配置项：{missing}")
            
        return config
    
    def _build_messages(self, query: str) -> list:
        """构建安全的消息结构"""
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": self._sanitize_input(query)}
        ]
    
    @staticmethod
    def _sanitize_input(text: str) -> str:
        """输入内容安全处理"""
        text = text.strip()
        # 长度限制
        if len(text) > SAFETY_CONFIG["max_input_length"]:
            text = text[:SAFETY_CONFIG["max_input_length"]] + "..."
        # 违禁词过滤
        for word in SAFETY_CONFIG["blocked_words"]:
            if word in text:
                raise ValueError("输入包含违禁内容")
        return text

async def send_dify_request(
    user_id: str,
    query: str,
    model_type: str = DEFAULT_MODEL
) -> str:
    """
    发送标准化LLM请求
    
    :param user_id: 用户唯一标识
    :param query: 用户输入内容
    :param model_type: 模型类型（默认从config读取）
    :return: JSON标准化响应字符串
    """
    try:
        service = LLMService(model_type)
        
        response = service.client.chat.completions.create(
            model=service.model_config["model_name"],
            messages=service._build_messages(query),
            temperature=service.model_config["temperature"],
            max_tokens=service.model_config["max_tokens"],
            user=user_id
        )
        
        return json.dumps({
            "success": True,
            "answer": response.choices[0].message.content,
            "usage": {
                "total_tokens": response.usage.total_tokens,
                "model_type": model_type
            }
        })
        
    except Exception as e:
        logger.error(f"请求处理失败 | User: {user_id} | Error: {str(e)}", exc_info=True)
        return json.dumps({
            "success": False,
            "error": f"服务暂时不可用：{str(e)}",
            "usage": {}
        })

def handle_dify_response(
    response_data: Union[str, bytes, dict]
) -> Tuple[str, int, float, str]:
    """
    标准化响应处理器
    
    :param response_data: 支持str/bytes/dict三种输入格式
    :return: (回答内容, token消耗量, 估算成本, 货币单位)
    """
    try:
        # 统一输入处理
        if isinstance(response_data, dict):
            response = response_data
        elif isinstance(response_data, (bytes, bytearray)):
            response = json.loads(response_data.decode())
        else:
            response = json.loads(str(response_data))

        # 错误响应处理
        if not response.get("success", False):
            error_msg = response.get("error", "未知服务错误")
            logger.warning(f"请求失败 | Error: {error_msg}")
            return (error_msg, 0, 0.0, "CNY")

        # 获取模型配置
        model_type = response["usage"].get("model_type", DEFAULT_MODEL)
        config = MODEL_CONFIG.get(model_type, MODEL_CONFIG[DEFAULT_MODEL])
        
        # 计算成本
        total_tokens = response["usage"].get("total_tokens", 0)
        total_price = total_tokens * config["token_cost"]

        return (
            response.get("answer", "未获取到有效回复"),
            total_tokens,
            round(total_price, 4),
            "CNY"
        )
    
    except json.JSONDecodeError:
        logger.error("响应数据解析失败")
        return ("响应格式错误", 0, 0.0, "CNY")
    except KeyError as e:
        logger.error(f"响应字段缺失: {str(e)}")
        return ("响应数据不完整", 0, 0.0, "CNY")
    except Exception as e:
        logger.error(f"响应处理异常: {str(e)}", exc_info=True)
        return ("系统处理异常", 0, 0.0, "CNY")

# 单元测试
if __name__ == "__main__":
    import asyncio
    
    async def main_test():
        # 测试正常请求
        normal_res = await send_dify_request("test_user", "你好")
        print("[正常测试]", handle_dify_response(normal_res))
        
        # 测试错误请求
        error_res = await send_dify_request("test_user", "违禁内容测试")
        print("[违禁词测试]", handle_dify_response(error_res))
        
        # 测试错误模型类型
        try:
            await send_dify_request("test_user", "测试", "invalid_model")
        except Exception as e:
            print("[错误模型测试]", str(e))
    
    asyncio.run(main_test())
