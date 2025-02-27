import flet as ft

def Menu(page: ft.Page):
    
    page.add(
        ft.Text('hola')
    )
    
if '__name__'== '__main__':
    ft.app(Menu)