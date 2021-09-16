from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import urllib.parse
from pyBrainFxck import execute

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/muda/{message}")
async def getNyanMessage(message):
    #無駄言語をコンパイルし、その結果を返す
    message = urllib.parse.unquote(message)
    converted_message = execute(message)
    
    print(converted_message)
    return {"inputed":message,"message": converted_message,"status":"success"}
