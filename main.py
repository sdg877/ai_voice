import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli,  llm
from livekit.agents.voice_assistant import VoiceAssistant

load_dotenv()

