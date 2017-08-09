import sys
import depsearch.directory_tree
import depsearch.cpp.include

def main():
	path = sys.argv[1]
	tree = depsearch.directory_tree.DirectoryTree(path)

	depsearch.cpp.include.listIncludes("depsearch/cpp/DELETE_test.txt")

if __name__ == "__main__":
	main()