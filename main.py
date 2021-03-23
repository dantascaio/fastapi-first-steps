from typing import Optional

from fastapi import FastAPI
from models import user
from models.model import ModelName

app = FastAPI()


@app.get("/consulta-chave/{chave}")
async def root(chave: str):
    return {"message": f"Sua chave é: {chave}"}


@app.get("/consulta-bool/{bool}")
async def boolean(entrada: bool):
    return {"A entrada é verdadeira"} if entrada else {"A entrada não é verdadeira"}

@app.get("/models/{model_name}")
async def select_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return { "model_name" : model_name, "message": "Alexnet rocks!!" }
    if model_name.value == "resnet":
        return { "model_name" : model_name, "message": "Let's use some resnet!" }
    return {"model_name" : model_name, "message": "I'm not sure about this one"}

@app.get("/select-item/{user_id}/items/{item_id}")
async def select_user_item(user_id : int, item_id: int, details: Optional[str] = "no details",
                           full_context: bool = False):
    item = {"Item_id": item_id, "Owner_id": user_id}
    if details != 'no details':
        item.update({"Details" : details})
    if full_context:
        item.update({"Context": f"The item {item_id} belongs to User {user_id}"})
    return item






# @app.get("/detalha-usuario/{user_received}")
# async def root(user_received: user.User):
#     user_teste = user.User("Caio Dantas", "F1704955")
#     return user_teste.to_json()

