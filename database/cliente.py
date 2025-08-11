# db.py
# Banco de dados temporário (em memória) de usuários

usuarios = [
    {
        "id": 1,
        "nome": "João Silva",
        "email": "joao@exemplo.com",
        "status": "Ativo"
    },
    {
        "id": 2,
        "nome": "Maria Oliveira",
        "email": "maria@exemplo.com",
        "status": "Ativo"
    },
    {
        "id": 3,
        "nome": "Carlos Souza",
        "email": "carlos@exemplo.com",
        "status": "Pendente"
    },
    {
        "id": 4,
        "nome": "Ana Costa",
        "email": "ana@exemplo.com",
        "status": "Inativo"
    }
    ,
    {
        "id": 5,
        "nome": "Pedro Santos",
        "email": "pedrinho@exemplo.com",
        "status": "Ativo"
    }
]

# Funções utilitárias para manipulação dos dados
def listar_usuarios():
    """Retorna todos os usuários"""
    return usuarios

def buscar_usuario(email):
    """Busca um usuário pelo e-mail"""
    return next((u for u in usuarios if u["email"] == email), None)

def adicionar_usuario(nome, email, status):
    """Adiciona um novo usuário"""
    usuarios.append({"nome": nome, "email": email, "status": status})

def atualizar_usuario(email, novos_dados):
    """Atualiza dados de um usuário"""
    usuario = buscar_usuario(email)
    if usuario:
        usuario.update(novos_dados)
        return True
    return False

def remover_usuario(email):
    """Remove um usuário pelo e-mail"""
    global usuarios
    usuarios = [u for u in usuarios if u["email"] != email]
    return True
