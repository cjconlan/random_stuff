"""
A simple while loop to periodically get all new messages from a list/queue, 
allow time to process them then get more messages without losing any.
"""

import random, string, time, collections, threading

class Device(threading.Thread):
    """
    This is the mocked device that keeps adding messages in a thread
    It continually add random strings to a deque
    Starts running at init, and can be stopped with stop()
    """
    def __init__(self):
        self.dq = collections.deque(maxlen=42)
        self.running = True
        super().__init__()
        self.start()
    def run(self):
        while self.running:
            length = random.randrange(50, 99)
            letters = ''.join(
                random.choice(string.ascii_letters) for x in range(length))
            self.dq.append(letters)
            time.sleep(1)
    def stop(self):
        self.running = False
        self.join()
        print('Stopped thread')


dev = Device()


messages = list()
# Now get the messages from our 'device'.
while True:
    while dev.dq:
        messages.append(dev.dq.pop() )
    else:
        print(f'found {len(messages)} messages, waiting for more')
        messages.clear()
        # Pretend wer'e processing the messages..
        time.sleep(random.randrange(1, 11))
