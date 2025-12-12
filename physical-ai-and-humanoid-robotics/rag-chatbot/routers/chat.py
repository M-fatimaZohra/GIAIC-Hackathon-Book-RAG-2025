from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from my_agent.course_agent import course_agent
import asyncio
from agents import Runner


router = APIRouter()

# Pydantic model for the incoming request body
class ChatRequest(BaseModel):
    message: str

# Initialize the agent once at startup
agent_instance = None

@router.on_event("startup")
async def startup_event():
    global agent_instance
    agent_instance = course_agent
    print("Course agent initialized.")

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not agent_instance:
        raise HTTPException(status_code=503, detail="Agent not initialized.")

    try:
        # Run the agent asynchronously using Runner.run
        result = await Runner.run(agent_instance, request.message)

        # Access the final_output from RunResult object
        final_output = result.final_output
        if isinstance(final_output, dict):
            response = final_output.get("response", "I don't know.")
            sources = final_output.get("sources", [])
        else:
            # Handle case where final_output might be a string or other type
            response = str(final_output) if final_output else "I don't know."
            sources = []

        return {"response": response, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")
