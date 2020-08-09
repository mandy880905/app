
from flask import Flask, request, abort

from urllib.request import urlopen

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)

app = Flask(__name__)

line_bot_api = ('wLW5wDgclXe+jQN8XCMNiCpUamwoJYR0pBhKtLY6St2UuaALEx2XupOaP/L1fXPTU19fwe7pfj47yr4SXopx+UVOir77Fk1yXB+Qa8/+5GOdCPkjTTVgXwtB69DxlrZkVpcr4PKTYqF7tUDNnwZwnAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b059c0330779399f67bfe611dd6373e9')
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID

    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    else:
        reply_text = text

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
