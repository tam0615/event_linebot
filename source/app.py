import json
import os
import logging
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage, PostbackEvent,FollowEvent)

import linebot_methods
import spreadsheet_methods

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def lambda_handler(event, context):
    YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
    YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
    line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
    handler = WebhookHandler(YOUR_CHANNEL_SECRET)

    signature = event["headers"]['x-line-signature']
    body = event["body"]
    path = event["path"]
    print("Request body: " + body)
    sheets = spreadsheet_methods.GetWorksheets()


    @handler.add(FollowEvent)
    def follow_message(line_event):# event: LineMessagingAPIで定義されるリクエストボディ
        linebot_methods.ReplyText(line_event, "フォロー完了")
            
    @handler.add(MessageEvent, message=TextMessage)
    def message(line_event):
        if line_event.message.text == '出欠登録':
            linebot_methods.ReplyText(line_event, line_event.message.text)

        if line_event.message.text == '参加者統計':
            linebot_methods.ReplyText(line_event, line_event.message.text)
        
        if line_event.message.text == 'メニュー':
            linebot_methods.ReplyImage(line_event,
                                       "https://share-bucket-000.s3.ap-northeast-1.amazonaws.com/479F7896-8B36-4222-B9B1-F309D0B038BE_1_105_c.jpeg", 
                                       "https://share-bucket-000.s3.ap-northeast-1.amazonaws.com/479F7896-8B36-4222-B9B1-F309D0B038BE_1_105_c.jpeg")

        if line_event.message.text == '場所':
            linebot_methods.ReplyText(line_event, "https://maps.app.goo.gl/FHx7p2shioFGatHR7")

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        logger.error("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            logger.error(" %s: %s" % (m.property, m.message))

    except InvalidSignatureError:
        logger.error("sending message happen error")
