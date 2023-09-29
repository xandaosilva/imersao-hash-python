import flet as ft

def main(page):
    text = ft.Text("Hashzap")
    chat = ft.Column()
    user_name = ft.TextField(label = "Escreva seu nome")
    field_message = ft.TextField(label = "Escreva sua mensagem")

    def send_message_tunel(message):
        type_msg = message["type"]

        if(type_msg) == "message":
            text_message = message["text"]
            user_message = message["user"]
            chat.controls.append(ft.Text(f"{user_message}: {text_message}"))
        else:
            user_message = message["user"]
            chat.controls.append(ft.Text(f"{user_message} entrou no chat", size=12, italic=True, color=ft.colors.ORANGE_500))
        page.update()


    page.pubsub.subscribe(send_message_tunel)

    def send_message(event):
        page.pubsub.send_all({"text" : field_message.value, "user": user_name.value, "type": "message"})
        field_message.value = ""
        page.update()


    button_send_message = ft.ElevatedButton("Enviar", on_click=send_message)

    def enter_popup(event):
        page.pubsub.send_all({"user" : user_name.value, "type": "enter"})
        page.add(chat)
        popup.open = False
        page.remove(button_init)
        page.remove(text)
        page.add(ft.Row([field_message, button_send_message]))
        page.update()

    
    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title = ft.Text("Bem vindo(a) ao Hashzap"),
        content = user_name,
        actions = [ft.ElevatedButton("Entrar", on_click=enter_popup)],    
    )

    def enter_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    
    button_init = ft.ElevatedButton("Iniciar chat", on_click=enter_chat)

    page.add(text)
    page.add(button_init)


ft.app(target=main, view=ft.WEB_BROWSER)
