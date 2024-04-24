import threading

def setTimeout(func, delay):
    timer = threading.Timer(delay / 1000, func)  # Convert milliseconds to seconds for delay
    timer.start()

# Example usage
def print_message():
    print("Hello from setTimeout!")

# Call setTimeout with the function to be executed and the delay in milliseconds
setTimeout(print_message, 3000)  # Execute print_message after 3 seconds (3000 milliseconds)
