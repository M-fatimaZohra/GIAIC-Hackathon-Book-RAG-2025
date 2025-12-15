import traceback
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
        print(f"Chat Endpoint Step 1: Received request with message: '{request.message[:50]}...'")

        # Run the agent asynchronously using Runner.run
        print("Chat Endpoint Step 2: Running agent with Runner...")
        result = await Runner.run(agent_instance, request.message)
        print("Chat Endpoint Step 2: Agent run completed successfully")

        # Access the final_output from RunResult object
        print("Chat Endpoint Step 3: Extracting final_output from RunResult...")
        final_output = result.final_output
        print(f"Chat Endpoint Step 3: Final output type: {type(final_output)}")

        if isinstance(final_output, dict):
            print("Chat Endpoint Step 4: Processing dictionary output...")
            response = final_output.get("response", "I don't know.")
            sources = final_output.get("sources", [])
            print(f"Chat Endpoint Step 4: Extracted response (length: {len(response)}), sources count: {len(sources)}")
        else:
            # Handle case where final_output might be a string or other type
            print("Chat Endpoint Step 4: Processing non-dictionary output...")
            response = str(final_output) if final_output else "I don't know."
            sources = []
            print(f"Chat Endpoint Step 4: Converted to string response (length: {len(response)}), empty sources")

        print("Chat Endpoint Step 5: Returning response to user")
        return {"response": response, "sources": sources}
    except Exception as e:
        import traceback
        print(f"ERROR in chat_endpoint - Chat Error: {e}")
        print(f"Full traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")
