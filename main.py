from src.core.pipeline import run_pipeline
import threading
import time
import asyncio

def spinner(stop_event):
    i = 0
    ANIMATION = ["   ", ".  ", ".. ", "...", " ..", "  .", "   "]
    while not stop_event.is_set():
        print(f"\rAgent: {ANIMATION[i % len(ANIMATION)]}", end="")
        time.sleep(0.2)
        i += 1

if __name__ == "__main__":
    c = 0
    while c < 20:
        try:
            user_input = input("User: ")
            
            stop_loading = threading.Event()
            thread = threading.Thread(target=spinner, args=(stop_loading,))
            
            thread.start()
            
            result = asyncio.run(run_pipeline(user_input))
            
        finally:
            stop_loading.set()
            thread.join()
            c += 1
        
        print(f"\rAgent: {result.final_output}")