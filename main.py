from fastapi import FastAPI
from models import user
app = FastAPI()


@app.get("/consulta-chave/{chave}")
async def root(chave):
    return {"message": f"Sua chave é: {chave}"}


@app.get("/consulta-bool/{bool}")
async def root(entrada: bool):
    return {"A entrada é verdadeira"} if entrada else {"A entrada não é verdadeira"}


@app.get("/detalha-usuario/{user_received}")
async def root(user_received: user.User):
    user_teste = user.User("Caio Dantas", "F1704955")
    return user_teste.to_json()

