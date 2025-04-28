import app.core.config as config

def process_conversation(message):
    return {"response": f"I am {config.CHATBOT_NAME}, how can I help you?"}
