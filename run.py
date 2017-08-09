import sys
import depsearch.directory_tree

def main():
	path = sys.argv[1]
	tree = depsearch.directory_tree.DirectoryTree(path)

if __name__ == "__main__":
	main()