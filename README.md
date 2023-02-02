# Pic2Desc
<p align="center">
<img src="https://github.com/artempl88/Pic2Desc/blob/main/Pic2Desc_logo.png">
</p>
Pic2Desc is a telegram bot that generates a product description based on a picture sent by the user and posts it to the website, based on Woocommerce plugin by Woocommerce API.

# Features
1. Takes a picture from the user and passes it to the Vision API for object recognition.
2. Converts pictures to descriptive captions with high accuracy
3. Supports various image formats (JPEG, PNG, etc.)
4. Extracts the noun and adjective from the recognition result and passes it to the Chat GPT API to generate a product description.
5. Translates the generated description to Russian using the Yandex Translator API.
6. Sends the translated description back to the user and provides two buttons for them to either place the product on a site using the Woocommerce API or generate more descriptions.
7. Generates captions in real-time
8. Easy to use and navigate interface
9. Option to save captions for later use

# Requirements
1. A device with a camera or access to image files
2. Internet connection for image analysis
3. Telegram Bot API Key
4. Vision API Key
5. Chat GPT API Key
6. Yandex Translator API Key
7. Woocommerce API Key
8. Python 3
9. requests library
10. telebot library
11. json library

# Usage
1. Clone this repository
2. Replace the placeholders in the script with your API keys
3. Run the script using python3 pic2desc.py
4. Start a chat with your bot on Telegram and use the /start command
5. Follow the instructions given by the bot to generate a product description.

License
This project is licensed under the MIT License - see the LICENSE file for details.
