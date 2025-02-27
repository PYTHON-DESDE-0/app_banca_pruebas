import flet as ft
import requests

API_URL = "http://127.0.0.1:8000/login"  # URL del backend FastAPI

def Log_in(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.RED_700

    usuario = ft.TextField(label="Usuario", width=300)
    contraseña = ft.TextField(label="Contraseña", width=300, password=True, can_reveal_password=True)
    mensaje_error = ft.Text("", color=ft.colors.RED)

    def onclick_Menu(e):
        """ Función que valida el login """
        user_data = {
            "usuario": usuario.value.strip(), #Strip elimina los espacios en blanco y el value es lo que recibira
            #de el textfield
            "contraseña": contraseña.value.strip()
        }

        try:
            response = requests.post(API_URL, json=user_data)

            if response.status_code == 200:
                page.controls.clear()
                from menu import Menu  # Importa Menu solo si el login es exitoso
                Menu(page)
            else:
                mensaje_error.value = "Usuario o contraseña incorrectos"
                page.update()
        except Exception as ex:
            mensaje_error.value = f"Error de conexión: {ex}"
            page.update()

    user_container = ft.Container(
        ft.Column(
            [
                ft.Text("INICIAR SESIÓN", size=25, font_family="Times New Roman"),
                usuario,
                contraseña,
                mensaje_error
            ]
        ),
        bgcolor=ft.colors.WHITE,
        padding=40,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.BLACK)
    )

    boton = ft.Container(
        content=ft.FilledButton(
            "Iniciar Sesión",
            bgcolor=ft.colors.BLACK,
            width=380,
            on_click=onclick_Menu
        ),
    )

    page.add(user_container, boton)

if __name__ == "__main__":
    ft.app(target=Log_in)
