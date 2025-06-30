""" Declarando os Módulos """

from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, sessionmaker

# Criando o banco de dados
db = create_engine("sqlite:///pizzaria.db", echo=True)

# Instanciando a sessão
Session = sessionmaker(bind=db)
session = Session()

# Base declarativa
class Base(DeclarativeBase):
    pass

# Modelo User
class User(Base):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    nome: Mapped[str] = mapped_column(String)
    
    telefone: Mapped[int] = mapped_column(Integer)
    
    endereco: Mapped[str] = mapped_column(String)

    # Relacionamento com pedidos
    pedidos: Mapped[list["Pedido"]] = relationship(back_populates="usuario")

# Modelo Pedido
class Pedido(Base):
    __tablename__ = 'pedidos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Chave estrangeira que aponta para o usuário (aprendi estudando a biblioteca :D)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))

    # Relacionamento ORM com User (aprendi estudando a biblioteca :D)
    usuario: Mapped["User"] = relationship(back_populates='pedidos')

    # Descrição do pedido
    descricao: Mapped[str] = mapped_column(String)

    bebida: Mapped[str] = mapped_column(String)
    
# Criando um usuário e um pedido para testar no banco
from src.pagina.cadastro import nome, telefone, endereco

user = User(
    nome = nome,
    telefone=telefone,
    endereco = endereco
)

pedido1 = Pedido(
    descricao='Atum com Queijo',
    usuario=user , # associação direta
    bebida = 'Coca-Zero'
)
    
# Criando as tabelas no banco de dados
Base.metadata.create_all(db)

# Adicionado os dados no BD.
session.add_all([user, pedido1])

#ativando o ambiente 'o Famoso COMMIT'
session.commit()
