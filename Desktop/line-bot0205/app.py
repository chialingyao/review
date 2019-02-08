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

app = Flask(__name__)

line_bot_api = LineBotApi('r7sj2S01EoafYqsWV7aPx3KN/8Pb312Va+F8vZffoqI85s+c36il7ysLASE5vCFfEdK8gtPsrvclgnSalaeei3XEQHPD6dPZPO+1RDWplp0oP9WzfiV2YeYcmt2VIQGVSfbkRj+bZcDrFCHv3F1VNQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('767d08776cff00b556562d7660ea0652')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()