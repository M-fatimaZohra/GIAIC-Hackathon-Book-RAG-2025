import os
import asyncio
import traceback
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, function_tool, Runner
from my_config.gemini_config import CLIENT
from rag.retrieve import retrieve_context

load_dotenv(override=True)

# Configure the Gemini model using the AsyncOpenAI client
MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash-lite", openai_client=CLIENT)

# Define the retrieval tool using @function_tool
@function_tool
async def retrieval_tool(query: str, top_k: int = 3) -> dict:
    """
    Retrieve relevant context from the Docusaurus book.
    Returns structured output with 'response' and 'sources'.
    """
    try:
        print(f"Agent Tool Step 1: Starting retrieval for query: '{query[:50]}...'")
        context_chunks, sources = await retrieve_context(query, top_k)
        print(f"Agent Tool Step 2: Retrieval completed, got {len(context_chunks)} context chunks and {len(sources)} sources")

        response_text = " ".join(context_chunks) if context_chunks else "I don't know."
        print(f"Agent Tool Step 3: Response prepared, text length: {len(response_text)}")

        return {
            "response": response_text,
            "sources": sources  # Return actual sources
        }
    except Exception as e:
        print(f"ERROR in retrieval_tool - Tool Error: {e}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        return {
            "response": "Error retrieving context from the knowledge base.",
            "sources": []
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

