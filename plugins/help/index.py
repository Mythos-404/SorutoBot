from bridge.tomorin import on_activator, on_event, h, admin_list, SessionExtension

@on_event.message_created
def _help(session: SessionExtension):
    session.function.register(['help']) #自定义回复示例
    session.function.description = '帮助'
    session.action(
        {
            None: help,
        }
    )

def help (session):
    session.send("帮助文档:https://cong.reikohaku.fun/#/newbotproject")