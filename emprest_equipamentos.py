import flet as ft
def main(page:ft.Page):
    '''page.title='PROGRAMA DE EMPRÉSTIMO DE EQUIPAMENTOS'
    page.bgcolor(ft.Colors.CYAN_100)'''
    titulo=ft.Text('PROGRAMA DE EMPRÉSTIMO DE EQUIPAMENTOS',size=20)
   

    nome=ft.TextField(hint_text='Nome do responsável')
    equipamento=ft.Dropdown(label='Equipamento a ser emprestado: ', options=[
        ft.DropdownOption(key='Notebook'),
        ft.DropdownOption(key='Projetor'),
        ft.DropdownOption(key='Multímetro')
    ])
    quantidade=ft.TextField(hint_text='Quantidade de equipamentos')

    page.add(titulo,nome,equipamento,quantidade)
ft.run(main)
        


