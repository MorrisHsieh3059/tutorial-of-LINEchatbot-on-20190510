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
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)


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
    if text == "媽媽" or text == "母親":
        ret1 = TextSendMessage(text="母親節快樂")
        ret2 = StickerSendMessage(package_id=11537, sticker_id=52114118)
        line_bot_api.reply_message(event.reply_token, [ret1] + [ret2])
    else:
        ret = TextSendMessage(text=text)
        line_bot_api.reply_message(event.reply_token, ret)
