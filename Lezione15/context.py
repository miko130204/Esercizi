# 1

class FileManager:
    def __init__(self, filename, mode):
        """Inizializza il FileManager con il nome del file e la modalità di apertura."""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Apre il file e ritorna l'oggetto file."""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Chiude il file e gestisce eventuali eccezioni."""
        if self.file:
            self.file.close()
        
        return False


with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')
    
    
# 2

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"time elapsed: {elapsed_time:.5f}")


with Timer():
    time.sleep(1)

