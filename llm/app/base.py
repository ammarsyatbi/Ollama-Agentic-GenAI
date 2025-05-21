from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
import requests
from .utils import Request, Response
from src.healthcare.flows.flow import RouterFlow
import os 

router = APIRouter()
flow = RouterFlow()

LIMIT_WINDOW = 15 

# Seperately run as frontend
# @router.get("/")
# async def page_home():
#     return FileResponse('static/home.html')

# @router.get("/main")
# async def page_main():
#     return FileResponse('static/main.html')

@router.post("/api/agent_flow")
def flow(request: Request) -> Response:
    history = request.history[:LIMIT_WINDOW]

    result = flow.kickoff(inputs={"inputs": history})
    
    return result
