import os

class Directory:
	def __init__(self, dirname):
		self.parentDir = str()
		self.dir = dirname
		self.subdirs = list()

		self.files = list()

		self.depth = int()


class DirectoryTree:
	def __init__(self, dir):
		self.rootDir = dir
		self.directoryMap = dict()

		self.mapDirectories()
		self.assignDepth(self.rootDir, 0)

		self.printInfo()

	def mapDirectories(self, ignoreHiddenFiles = True):
		for root, subdirs, files in os.walk(self.rootDir):
			if not ignoreHiddenFiles:
				files = [f for f in files if not f[0] == '.']
    			subdirs[:] = [d for d in subdirs if not d[0] == '.']
			directory = Directory(root)
			for file in files:
				directory.files.append(file)
			for subdir in subdirs:
				directory.subdirs.append(subdir)
			self.directoryMap[root] = directory

	def assignDepth(self, directory, currentDepth):
		self.directoryMap[directory].depth = currentDepth
		for subdir in self.directoryMap[directory].subdirs:
			self.assignDepth(os.path.join(directory, subdir), currentDepth + 1)

	def printInfo(self):
		queue = [self.rootDir]
		while not len(queue) == 0:
			current = queue.pop()
			currentDepth = self.directoryMap[current].depth
			print '  '*currentDepth, self.directoryMap[current].dir
			for subdir in self.directoryMap[current].subdirs:
				queue.append(os.path.join(current, subdir))
			for file in self.directoryMap[current].files:
				print '  '*currentDepth, file


			
		