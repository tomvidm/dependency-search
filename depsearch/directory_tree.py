import os

class DirectoryTree:
	def __init__(self, dir):
		self.rootDir = dir
		self.directoryMap = dict()
		self.map()

	def map(self, ignoreHiddenFiles = True):
		for root, dirs, files in os.walk(self.rootDir):
			if not ignoreHiddenFiles:
				files = [f for f in files if not f[0] == '.']
    			dirs[:] = [d for d in dirs if not d[0] == '.']
			print(root)
		