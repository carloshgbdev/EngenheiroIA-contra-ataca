from app.core.config import settings

def process_conversation(message):
    return {"response": f"I am {settings.CHATBOT_NAME}, how can I help you?"}
