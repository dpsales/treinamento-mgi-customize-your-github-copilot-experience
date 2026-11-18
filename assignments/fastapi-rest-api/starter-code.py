from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI item service"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass


@app.post("/items")
def create_item(item: dict):
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    pass
