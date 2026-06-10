from src.core.pipeline import run_pipeline
import asyncio

if __name__ == "__main__":
    user_input = input("User: ")
    result = asyncio.run(run_pipeline(user_input))
    print(result.final_output)
