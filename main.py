from fastapi import FastAPI
from routers import fake_llm_router

app = FastAPI()

app.include_router(fake_llm_router)