# script/LLM/config.py

import os

# 全局配置常量
DEFAULT_MODEL = "deepseek"  # 在此修改默认模型

# 模型配置中心
MODEL_CONFIG = {
    "deepseek": {
        "api_key": os.getenv("DEEPSEEK_KEY", "sk-xxx"),
        "base_url": "https://api.siliconflow.cn/v1",
        "model_name": "deepseek-ai/DeepSeek-V3",
        "token_cost": 0.0001,  # 每token成本（单位：CNY）
        "max_tokens": 4096,
        "temperature": 0.7
    },
    "kimi": {
        "api_key": os.getenv("KIMI_KEY", "sk-xxx"),
        "base_url": "https://api.moonshot.cn/v1",
        "model_name": "moonshot-v1-8k",
        "token_cost": 0.00015,
        "max_tokens": 8192,
        "temperature": 0.5
    }
}

# 系统级提示词
SYSTEM_PROMPT = """你是由W1ndys和半圆子SUPER4NRNS开发的智能助手fufu，请遵守：
1. 使用自然的中文口语化回复
2. 对不确定信息明确说明
3. 拒绝回答隐私/安全问题
4. 禁用Markdown格式
5. 保持回复简洁（最多3段）"""

# 安全配置
SAFETY_CONFIG = {
    "max_input_length": 2000,  # 输入最大字符数
    "rate_limit": 5,  # 每分钟最大请求数
    "blocked_words": ["暴力", "政治敏感", "违法内容"]  # 违禁词列表
}
