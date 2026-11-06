import time

class Timer():
	def __init__(self):
		self.time = self.reset()
		
	def reset(self):
		return int(round(time.time() * 1000))
		
	def get(self):
		return int(round(time.time() * 1000)) - self.time