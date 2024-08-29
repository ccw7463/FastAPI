from configs.prompt import *
from utils.text_to_sql import *
from utils.util import *
from models.model import qwen_llm # aya_llm
LLM = qwen_llm

import chainlit as cl
from configs.profile import GetProfile
chat_profiles = GetProfile()