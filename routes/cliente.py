from flask import Blueprint, render_template
from database.cliente import listar_usuarios#, adicionar_usuario, buscar_usuario, atualizar_usuario, remover_usuario

cliente_route = Blueprint('cliente', __name__)

"""
Rota de clientes

    - /clientes/ (GET) - Listar todos os clientes
    - /clientes/new (GET) - Renderizar o formulário para cadastrar um novo cliente
    - /clientes/new (POST) - Processar o cadastro de um novo cliente
    - /clientes/<id> (GET) - Obter dados de um cliente específico
    - /clientes/<id>/cadastrar (GET) - Cadastrar um novo cliente
    - /clientes/<id>/editar (PUT) - Editar dados de um cliente específico
    - /clientes/<id>/excluir (DELETE) - Excluir um cliente específico
"""

@cliente_route.route('/')
def listar_clientes():
    lista = listar_usuarios()
    return render_template('lista_clientes.html', clientes= lista)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/new', methods=['GET', 'POST'])
def formulario_cliente():
    """formuario para cadastrar um novo cliente."""
    return render_template('formulario_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """Exibir detalhes de um cliente específico."""
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit', methods=['PUT'])
def editar_formulario_cliente(cliente_id):
    """formulario para editar um cliente específico."""
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """deleltar um cliente específico."""
    pass