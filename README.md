# Python Multiprocessing and Threading Example

## Overview
Python script showing inter-process communication using `multiprocessing.Pipe()`. Involves a parent process and a child thread communicating through a pipe. The child thread receives a message from the parent, modifies it, and sends it back.

## Code Explanation

### 1. Importing Required Modules
```python
import multiprocessing
import threading
```
- `multiprocessing` is used to create a pipe for inter-process communication.
- `threading` is used to simulate a child process inside a separate thread.

### 2. Child Process Function
```python
def child_process(pipe):
    message = pipe.recv()  # Receive message from the parent
    print(f"Child received: {message}")
    
    modified_message = message.swapcase()  # Swap case of the message
    modified_message += " CHILD"  # Append "CHILD" to the message
    
    pipe.send(modified_message)  # Send modified message back to parent
    print("Child sent modified message back to parent")
```
- Reads a message from the pipe.
- Modifies the message by swapping the case of each letter and appending "CHILD".
- Sends the modified message back to the parent process.

### 3. Parent Process Function
```python
def parent_process(pipe):
    message = "COMP 512 pipe programming parent"
    print(f"Parent sending: {message}")
    
    pipe.send(message)  # Send message to the child
    
    modified_message = pipe.recv()  # Receive modified message from the child
    print(f"Parent received: {modified_message}")
```
- Sends an initial message to the child.
- Waits for and receives the modified message from the child.

### 4. Main Execution
```python
if __name__ == "__main__":
    parent_pipe, child_pipe = multiprocessing.Pipe()  # Create a pipe
    
    child_thread = threading.Thread(target=child_process, args=(child_pipe,))
    child_thread.start()  # Start the child process as a thread
    
    parent_process(parent_pipe)  # Run parent process
    
    child_thread.join()  # Wait for child thread to complete
```
- Creates a `multiprocessing.Pipe()` for communication.
- Starts a child process inside a thread using `threading.Thread()`.
- Runs the parent process to send and receive messages.
- Waits for the child thread to finish execution.

## Expected Output
```
Parent sending: COMP 512 pipe programming parent
Child received: COMP 512 pipe programming parent
Child sent modified message back to parent
Parent received: comp 512 PIPE PROGRAMMING PARENT CHILD
```

## Installation and Usage
1. Clone the respository and run it with python pipe.py

