# Pic2Desc
Pic2Desc is a telegram bot that generates a product description based on a picture sent by the user and posts it to the website, based on Woocommerce plugin Woocommerce API.

# Features
1. Takes a picture from the user and passes it to the Vision API for object recognition.
2. Extracts the noun and adjective from the recognition result and passes it to the Chat GPT API to generate a product description.
3. Translates the generated description to Russian using the Yandex Translator API.
4. Sends the translated description back to the user and provides two buttons for them to either place the product on a site using the Woocommerce API or generate more descriptions.

# Requirements
Telegram Bot API Key
Vision API Key
Chat GPT API Key
Yandex Translator API Key
Woocommerce API Key
Python 3
requests library
telebot library
json library

# Usage
1. Clone this repository
2. Replace the placeholders in the script with your API keys
3. Run the script using python3 pic2desc.py
4. Start a chat with your bot on Telegram and use the /start command
5. Follow the instructions given by the bot to generate a product description.
License

This project is licensed under the MIT License - see the LICENSE file for details.
