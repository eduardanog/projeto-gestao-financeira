from sqlalchemy import Column, Integer, Float, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from db import Base


class Usuario(Base):
    __tablename__= "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column("nome", String(100), nullable=False)
    email = Column("email", String)
    telefone=Column("telefone", Integer)
    despesas = relationship("Despesa", back_populates="usuario") #conecta o 'usuario' na classe 'Despesa'


class Categoria(Base):
    __tablename__="categorias"
    id= Column(Integer, primary_key=True)
    nome_categoria=Column("nome_categoria", String(100))
    despesas= relationship("Despesa", back_populates="categoria")


class Despesa(Base):
    __tablename__="despesas"
    id=Column(Integer, primary_key=True)
    descricao=Column("descricao", String)
    valor=Column(Float)
    data=Column(Date)

    usuario_id= Column(Integer, ForeignKey("usuarios.id")) #crio uma chave estrangeira para atribuir a despensa ao usuário
    categoria_id=Column(Integer, ForeignKey("categorias.id"))
    usuario=relationship("Usuario", back_populates="despesas") #permite criar um relacionamento com usuário para acessar diretamente as info
    categoria=relationship("Categoria", back_populates="despesas")