from db import Base, data_base, Session
from models import Usuario, Categoria, Despesa
from datetime import date

Base.metadata.create_all(bind=data_base)
d_b=Session()

usuario= Usuario(nome="Maria Eduarda")
d_b.add(usuario)
d_b.commit()

categoria=Categoria(nome_categoria="Alimentação")
d_b.add(categoria)
d_b.commit()

despesa=Despesa(
    descricao="Jantar em restaurante",
    valor=89.90,
    data=date.today(),
    usuario_id=usuario.id,
    categoria_id=categoria.id
)

d_b.add(despesa)
d_b.commit()


for i in d_b.query(Despesa).all():
    print(f"{i.descricao}: R$ {i.valor} - {i.categoria.nome_categoria}")