from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.chat import router as chat_router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configure CORS
# In a production environment, replace "*" with the actual domain of your Docusaurus frontend
origins = [
    os.getenv("FRONTEND_URL", "http://localhost:3000"), # Default for local development
    "https://giaic-hackathon-book-rag-2025.vercel.app" # Your deployed Docusaurus site
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the chat router
app.include_router(chat_router, prefix="/api")

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

# Basic rate limiting placeholder (can be enhanced with actual libraries like `fastapi-limiter`)
# @app.middleware("http")
# async def add_rate_limit_header(request: Request, call_next):
#     response = await call_next(request)
#     response.headers["X-RateLimit-Limit"] = "60"
#     response.headers["X-RateLimit-Remaining"] = "59"
#     return response

