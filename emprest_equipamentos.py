import flet as ft
def main(page:ft.Page):
    page.title='PROGRAMA DE EMPRÉSTIMO DE EQUIPAMENTOS'
    page.padding=20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo=ft.Text('PROGRAMA DE EMPRÉSTIMO DE EQUIPAMENTOS',size=20)
   

    nome=ft.TextField(hint_text='Nome do responsável')
    equipamento=ft.Dropdown(label='Equipamento a ser emprestado: ', options=[
        ft.DropdownOption(key='Notebook'),
        ft.DropdownOption(key='Projetor'),
        ft.DropdownOption(key='Multímetro')
    ])
    quantidade=ft.TextField(hint_text='Quantidade de equipamentos',keyboard_type=ft.KeyboardType.NUMBER)
    registro=ft.Column()

    def registrar(e):
        if not nome.value or not equipamento.value or not quantidade.value:
            registro.controls.append(
            ft.Text('Preencha os campos acima.'))
        elif not quantidade.value.isdigit() or int(quantidade.value)<=0  :
            registro.controls.append(
            ft.Text('Insira uma quantidade válida'))
        else:
            registro.controls.extend([
                ft.Text(f'Responsável: {nome.value}'),
                ft.Text(f'Equipamento: {equipamento.value}'),
                ft.Text(f'Quantidade: {quantidade.value}')
            ])
        page.update()
    
    btn_registro=ft.Button(content='Registrar Empréstimo',on_click=registrar)
    
    coluna=ft.Column([titulo,nome,equipamento,quantidade,btn_registro,registro],
       horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True,scroll=ft.ScrollMode.AUTO)


    page.add(coluna)
ft.run(main)
        


