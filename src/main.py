from src.vault import Vault
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(docs_url="/")
vault = Vault()


class Item(BaseModel):
    name: str
    message: str
    ccn: str


@app.post("/item")
async def create_item(item: Item):
    item.message = vault.encrypt(item.message)
    item.ccn = vault.encode(item.ccn, "ccn")

    # store in db
    # db.add(item)

    return item
