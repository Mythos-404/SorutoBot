from bridge.tomorin import *
import requests
from PIL import Image
import io

@on_event.message_created
def _peek(session: SessionExtension):
        session.function.register(['manapeek'])
        session.function.description = '通过Peek_API获取电脑运行图片'
        session.action(
                {
                        None: manapeek,
                }
        )

def manapeek(session):
        res = requests.get('http://127.0.0.1:1919/my/screen')
        # 转化成png
        png = Image.open(io.BytesIO(res.content))
        output = io.BytesIO()
        png.save(output, format='PNG')
        image_binary = output.getvalue()
        session.send(h.image(image_binary))
