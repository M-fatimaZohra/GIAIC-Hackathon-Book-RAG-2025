import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, function_tool, Runner
from my_config.gemini_config import CLIENT
from rag.retrieve import retrieve_context

load_dotenv()

# Configure the Gemini model using the AsyncOpenAI client
MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=CLIENT)

# Define the retrieval tool using @function_tool
@function_tool
async def retrieval_tool(query: str, top_k: int = 3) -> dict:
    """
    Retrieve relevant context from the Docusaurus book.
    Returns structured output with 'response' and 'sources'.
    """
    context_chunks = await retrieve_context(query, top_k)
    response_text = " ".join(context_chunks)
    return {
        "response": response_text if response_text else "I don't know.",
        "sources": context_chunks  # Optional: adjust for frontend
    }

# Initialize the course agent as a variable
course_agent = Agent(
    name="Course Assistant Agent",
    model=MODEL,
    instructions=(
        "You are a helpful AI assistant for the 'Physical AI & Humanoid Robotics' Docusaurus book. "
        "Answer user questions based on the provided context from the book. "
        "If the answer is not in the context, state that you don't know."
    ),
    tools=[retrieval_tool]
)

# Example usage for testing
async def main():
    while True:
        user_query = input("Ask a question about the book (or 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break
        # Run the agent asynchronously using Runner.run
    runner = Runner()
    result = await runner.run(course_agent, user_query)
    print(f"Agent Output:\n{result}")

if __name__ == "__main__":
    asyncio.run(main())

