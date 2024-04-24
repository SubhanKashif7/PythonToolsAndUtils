import threading
import time

def setInterval(func, interval):
    def wrapper():
        while True:
            func()
            time.sleep(interval / 1000)  # Convert milliseconds to seconds for sleep
    t = threading.Thread(target=wrapper)
    t.daemon = True  # Set the thread as daemon so it exits when the main program exits
    t.start()
    return t

# Example usage
def print_message():
    print("Hello from setInterval!")

# Call setInterval with the function to be executed and the interval in milliseconds
interval_thread = setInterval(print_message, 2000)  # Execute print_message every 2 seconds (2000 milliseconds)

# Keep the program running to see the interval in action
try:
    while True:
        time.sleep(1)  # Sleep for 1 second to prevent the main program from exiting
except KeyboardInterrupt:
    print("Program terminated by user.")

def hello():
    print("hello")

