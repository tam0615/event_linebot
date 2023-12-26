import os
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage)

#Set Environ in advance
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def GetProfile(line_event):
    return line_bot_api.get_profile(line_event.source.user_id)

def ReplyText(line_event,text):
    line_bot_api.reply_message(
        line_event.reply_token, TextSendMessage(text= text)
        )

def ReplyContent(line_event,content):
    line_bot_api.reply_message(
        line_event.reply_token, content
        )

def ReplyImage(line_event,url_org, url_prev):
    line_bot_api.reply_message(
        line_event.reply_token,ImageSendMessage(url_org, url_prev)
        )