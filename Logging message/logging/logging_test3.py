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
 output 1:
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
 
 output 2:

   3858 Thread-7 Hi from myfunc
  3859 MainThread Hello from main
  4376 Thread-7 Hi from myfunc
  4612 MainThread Hello from main
  4882 Thread-7 Hi from myfunc
  5368 MainThread Hello from main
  5384 Thread-7 Hi from myfunc
  5892 Thread-7 Hi from myfunc
  6127 MainThread Hello from main
  6395 Thread-7 Hi from myfunc
  6882 MainThread Hello from main
  6898 Thread-7 Hi from myfunc
  7410 Thread-7 Hi from myfunc
  7646 MainThread Hello from main
  7912 Thread-7 Hi from myfunc
  8410 MainThread Hello from main
  8426 Thread-7 Hi from myfunc
  8941 Thread-7 Hi from myfunc
  9175 MainThread Hello from main
  9456 Thread-7 Hi from myfunc
  9939 MainThread Hello from main
  9970 Thread-7 Hi from myfunc
 10475 Thread-7 Hi from myfunc
 10693 MainThread Hello from main
 10989 Thread-7 Hi from myfunc
 11455 MainThread Hello from main
 11502 Thread-7 Hi from myfunc
 12018 Thread-7 Hi from myfunc
 12222 MainThread Hello from main
 12535 Thread-7 Hi from myfunc
 12988 MainThread Hello from main
 13051 Thread-7 Hi from myfunc
 13565 Thread-7 Hi from myfunc
 
 output 3:
 115145 Thread-7 Hi from myfunc
115148 MainThread Hello from main
115654 Thread-7 Hi from myfunc
115902 MainThread Hello from main
116167 Thread-7 Hi from myfunc
116667 MainThread Hello from main
116682 Thread-7 Hi from myfunc
117198 Thread-7 Hi from myfunc
117432 MainThread Hello from main
117712 Thread-7 Hi from myfunc
118196 MainThread Hello from main
118228 Thread-7 Hi from myfunc
118743 Thread-7 Hi from myfunc
118960 MainThread Hello from main
119257 Thread-7 Hi from myfunc
 """
