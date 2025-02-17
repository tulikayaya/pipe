import multiprocessing
import threading

def child_process(pipe):
    # receive the message from the parent
    message = pipe.recv()
    print(f"Child received: {message}")

    # change the case of each character
    modified_message = message.swapcase()

    # add "CHILD" to the end of the message
    modified_message += " CHILD"

    # send the modified message back to the parent
    pipe.send(modified_message)
    print("Child sent modified message back to parent")

def parent_process(pipe):
    # create the message to send to the child
    message = "COMP 512 pipe programming parent"
    print(f"Parent sending: {message}")

    # send the message to the child
    pipe.send(message)

    # wait for the modified message from the child
    modified_message = pipe.recv()
    print(f"Parent received: {modified_message}")

if __name__ == "__main__":
    # create a pipe for communication
    parent_pipe, child_pipe = multiprocessing.Pipe()

    # create and start the child thread
    child_thread = threading.Thread(target=child_process, args=(child_pipe,))
    child_thread.start()

    # run the parent process
    parent_process(parent_pipe)

    # wait for the child thread to finish
    child_thread.join()