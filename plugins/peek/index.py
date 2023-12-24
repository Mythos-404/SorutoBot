from bridge.tomorin import *
import requests
from PIL import Image
import io

@on_event.message_created
def _peek(session: SessionExtension):
        session.function.register(['saltpeek'])
        session.function.description = '通过Peek_API获取电脑运行图片'
        session.action(
                {
                        None: saltpeek,
                }
        )

def saltpeek(session):
        res = requests.get('http://127.0.0.1:1919/my/screen') #获取电脑屏幕（https://github.com/YoisakiKnd/ChieriBot_peek_API）
        # 转化成png
        png = Image.open(io.BytesIO(res.content))
        output = io.BytesIO()
        png.save(output, format='PNG')
        image_binary = output.getvalue()
        session.send(h.image(image_binary))
