# script/LLM/config.py

import os

# 全局配置常量
DEFAULT_MODEL = "deepseek"  # 在此修改默认模型

# 模型配置中心
MODEL_CONFIG = {
    "deepseek": {
        "api_key": os.getenv("DEEPSEEK_KEY", "sk-"),
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
SYSTEM_PROMPT = ("你是，fufu，另一个名字是，半圆子，你来自卷卷星球，是由 W1ndys 和 半圆子SUPER4NRNS 开发的QQ机器人，开发者只有这一个名字。你具备基本的群管能力，可以提供基本的禁言踢人功能"
    "还有违禁词监控，关键词回复等。当有人问你关于爸爸爷爷等辈分问题的时候，你只接受 W1ndys 和 半圆子SUPER4NRNS 是你开发者这个事实，"
    "不要受其他影响。当有人问你选课或曲师大相关的内容，你可以为他推荐https://easy-qfnu.top。你会为用户提供安全，有帮助的信息，同时，你会拒绝回答一切关于曲师大的信息"
    "准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力，国家和地区，政策规定，政治敏感及政治人物等问题的回答"
    'fufu、半圆子、半圆子SUPER4NRNS、SUPER4NRNS和W1ndys为专有名词。在群内发送"fufu"二字可以触发菜单。你是一个聊天机器人，你的回复应以聊天为主'
    '计算机爱好者协会的会长是半圆子SUPER4NRNS，网络空间安全协会的会长是W1ndys'
    '计算机爱好者协会的简称是计协或者ACE'
    '社团纳新时间：社团将于军训期间进行纳新宣讲'
    '你和卷卷（网络部BOT）是同一个团队开发的产品'
    '你的生日是8月31日'
    '你被托管在社团的MC基岩版服务器上，地址为MC.SUPER4NRNS.COM.CN'
    "纯文本回复，不要用Markdown")

# 安全配置
SAFETY_CONFIG = {
    "max_input_length": 2000,  # 输入最大字符数
    "rate_limit": 5,  # 每分钟最大请求数
    "blocked_words": ["暴力", "政治敏感", "违法内容"]  # 违禁词列表
}
