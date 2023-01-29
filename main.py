import requests
import telegram

TOKEN = "your_bot_token"

def handle_photo(update, context):
    # Get the image file from the update
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('image.jpg')
    
    # Send the image to TensorFlow API
    response = requests.post('TensorFlow_API_URL', files={'image': open('image.jpg', 'rb')})
    result = response.json()
    
    # Assign the result to a variable 'I'
    I = result["info"]
    
    # Send the result to ChatGPT API
    response = requests.post('ChatGPT_API_URL', data={'text': I})
    reply = response.json()
    
    # Reply to the user with the result from ChatGPT
    context.bot.send_message(chat_id=update.message.chat_id, text=reply["output"])

# Initialize the bot and add the photo handler
bot = telegram.Bot(TOKEN)
updater = telegram.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.MessageHandler(telegram.MessageType.PHOTO, handle_photo))

# Start the bot
updater.start_polling()
