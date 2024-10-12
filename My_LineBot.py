from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage
from POST_AI import cout
app = Flask(__name__)

# 用你的 Channel Access Token 和 Channel Secret 替换下面的字符串
line_bot_api = LineBotApi("lYCh8DNGuXZ+eUQKrNnEIJUdW4XX0h/AAKz27/dfWUy81HEM21u0VRthPqi3tHkUT3eM3K2zcGNZSoFXQ9jTVPEqhSIKW+5LsfdSsxTHTu9HkVOG2amfdixKM3EG0YQ40PY0/V3lSZ7c8CDmvbMiNAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("14220887a1262d99c11e2086837ca184")

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=cout(event.message.text)))
        
if __name__ == "__main__":
    app.run(port=5050)
