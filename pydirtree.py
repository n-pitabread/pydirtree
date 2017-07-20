import os
import sys

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print '{}|-{}/'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print '{}|-{}'.format(subindent, f)



if __name__ == '__main__':
    if len(sys.argv) >= 2:
        dir_path = sys.argv[1]
        print "#Path is: " + dir_path
    else:
        print "No arguments - Closing"
        sys.exit()
    if os.path.isdir(dir_path):
        list_files(dir_path)
    elif os.path.exists(dir_path):
        print "Wrong path - path is not found."
    else:
        print "This is not a directory path."


        
    
