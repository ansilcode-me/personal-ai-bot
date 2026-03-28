import google.generativeai as genai
import telebot

# 1. Setup your API Keys
api_key = os.getenv("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")
# --- ADD IT HERE ---
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="You are a helpful coding assistant for a student in Kerala. Keep answers concise."
)
# -------------------

bot = telebot.TeleBot("8663212255:AAGrQTpEaSxn1zdqnMeKUNWSlIQzm3lN8Hk")

# --- NEW STUDY COMMAND ---
@bot.message_handler(commands=['study'])
def ask_quiz(message):
    prompt = "Give me one challenging multiple-choice question for Kerala SSLC level. Randomly pick between Physics, Chemistry, or Math."
    response = model.generate_content(prompt)
    bot.reply_to(message, response.text)
# -------------------------

@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    # The model now knows its "personality" before it generates content
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)

bot.infinity_polling()
