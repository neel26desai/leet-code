import threading

class SharedCounter:
	def __init__(self):
		self.value = 0
		self._value_lock = threading.Lock()
	
	def increment(self,delta=1):
		with self._value_lock:
			self.value+=delta
	def get_value(self):
		with self._value_lock:
			return self.value

def worker(counter,nun_iters):
	for _ in range(num_iters):
		counter.increment()

if __name__ =="__main__":
	counter = SharedCounter()
	num_iters = 10000
	num_workers = 5
	threads = [threading.Thread(target=worker,args=(counter,num_iters)) for _ in range(num_workers)]
	for t in threads:
		t.start()
	for t in threads:
		t.join()    
	print(counter.get_value())