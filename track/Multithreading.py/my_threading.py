import threading
def print_message(name, course):
    print(f"{name} and {course} are ready!")

# Create and start a thread
thread = threading.Thread(target=print_message,args = ["ujwala","python"])
thread.start()
thread.join()
# Check if the thread is alive
print(f"Process ended!")