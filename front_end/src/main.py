import flet as ft
from log_in import Log_in  # Importamos la pantalla de inicio de sesión

def main(page: ft.Page):
    Log_in(page)  # Llamamos la función que construye la UI

ft.app(target=main)
