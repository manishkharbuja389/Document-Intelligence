from fastapi import FastAPI
from app.routes import queries
from app.routes import search, indicators, context

app = FastAPI()

app.include_router(search.router)
app.include_router(indicators.router)
app.include_router(context.router)
app.include_router(queries.router)

@app.get("/")
def root():
    return {"message": "Document Intelligence Pipeline Running"}