import queue

my_queue = queue.LifoQueue()

while True:
    user_input = input("Enter an integer to add to the queue, or 'done' to finish: ")

    if user_input.lower() == 'done':
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    my_queue.put(num)

    print("Current queue:", list(my_queue.queue))

while not my_queue.empty():
    last_element = my_queue.get()
    print("Removed element:", last_element)
    print("Current queue:", list(my_queue.queue))
