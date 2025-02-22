# 系统级配置
SYSTEM_PROMPT = (
    "你是fufu，另一个名字是半圆子...（保持原有提示词）"
)

# 默认模型
DEFAULT_MODEL = "deepseek"

# LLM配置
LLM_CONFIG = {
    "deepseek": {
        "api_key": "sk-oxlloaaehkzstuijyirpixydoondqkooljmygoovvozzjupd",
        "base_url": "https://api.siliconflow.cn/v1",
        "model_name": "deepseek-ai/DeepSeek-V3"
    },
    "qwen": {
        "api_key": "sk-21e36652eebc4013bc54ed1ca733ab3d",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model_name": "qwen-plus"
    },
    "dify": {
        "api_key": "dify-your-key-here",
        "base_url": "https://api.dify.ai/v1"
    }
}
