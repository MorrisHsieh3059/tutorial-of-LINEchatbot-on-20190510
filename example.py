from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent, PostbackTemplateAction,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)

from carousel import *
app = Flask(__name__)

# line_bot_api = LineBotApi("EU/swMZys0cHv8L7BBqgOiYcbeCSiOtZrvA0OJQ3HFfoVKBZ8+Pj4cQvzPa5E0XoMleBSv2rmxDsDBSkbZTPGIZT3ql7eg2LL3N/vsWZuDh7msj0+H5cXj2oNjYs7BAmPB42+obIPk/pAWvUzZK4ZwdB04t89/1O/w1cDnyilFU=", "http://localhost:8080")
# handler = WebhookHandler("e565f1b39d4a254f9c089ac7b6d06cab")
line_bot_api = LineBotApi("YOUR TOKEN", "http://localhost:8080")
handler = WebhookHandler("YOUR SECRET")

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    # your code is here
    text = event.message.text
    userid = event.source.user_id

    if text == 'carousel':
        ct_container = [column1, column2]
        carousel_template = CarouselTemplate(columns=ct_container)
        template_message = TemplateSendMessage(template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data

    if data == 'love_pecu':
        ret1 = TextSendMessage(text='我也愛你唷~')
        ret2 = StickerMessage(package_id=11537,sticker_id=52002742)
        line_bot_api.reply_message(event.reply_token, [ret1] + [ret2])
    elif data == 'love_shi':
        ret1 = TextSendMessage(text='謝謝你唷~')
        ret2 = StickerMessage(package_id=11537,sticker_id=52002743)
        line_bot_api.reply_message(event.reply_token, [ret1] + [ret2])
