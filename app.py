from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from coinbase import MyCoinBase

app = Flask(__name__)

line_bot_api = LineBotApi('FiBbThcXH1b0Ac/q3aLm+UAgAxJuV3aWvj7Lfb3ZnBhK9wH/K7OksFIYRPAJ8q3dkHlybS6fEJy4khrxKk6857RGnY0hOU7Y8r8fFQukhxT16m5hu4vCs/exFz4A1H8q7GWwGJHrpwCMNXSwzSVeDwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('af3004544a2b0cfffa34552e5645807c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    myCB = MyCoinBase()

    if myCB.Include(event.message.text):
        price = myCB.Get(event.message.text,'TWD')
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=price + ' TWD'))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='這個幣種我沒資料耶,你需要去google一下QQ'))




if __name__ == "__main__":
    app.run(debug=True)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))