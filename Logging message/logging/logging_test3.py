import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

if __name__ == '__main__':
    main()
 """
 63182 Thread-7 Hi from myfunc
 63183 MainThread Hello from main
 63699 Thread-7 Hi from myfunc
 63949 MainThread Hello from main
 64213 Thread-7 Hi from myfunc
 64711 MainThread Hello from main
 64726 Thread-7 Hi from myfunc
 65241 Thread-7 Hi from myfunc
 65471 MainThread Hello from main
 65752 Thread-7 Hi from myfunc
 66237 MainThread Hello from main
 66268 Thread-7 Hi from myfunc
 66784 Thread-7 Hi from myfunc
 """
