from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router


app = FastAPI()

origins = ["http://192.168.0.43:7080",]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


app.include_router(question_router.router)