#! /usr/bin/env python3
import sys

def imp():
    try:
        import numpy
        import matplotlib.pyplot
    except ModuleNotFoundError:
        install('matplotlib')
        install('numpy')
        
def install(package):
    import subprocess
    import importlib
    subprocess.call([sys.executable, "-m", "pip", "install", package])
    main()
    
def makeGraph(cvs_txt, x_column, y_column, label):
    if (isinstance(cvs_txt, str) and isnum(x_column) and isnum(y_column) and isinstance(label, str)):
        x_c = int(x_column)
        y_c = int(y_column)
        if (x_c >= 0 and y_c >= 0):
            import numpy
            import matplotlib.pyplot as plt
            try :
                per_data=numpy.genfromtxt(r"%s" % cvs_txt,delimiter='\t',names=True)
                y = per_data.dtype.names[y_c]
                x = per_data.dtype.names[x_c]
                plt.plot(per_data[x], per_data[y], label=label)
                plt.legend(loc=0)
                plt.xlabel ('X')
                plt.ylabel ('Y')
                plt.grid()
                plt.show()
            except IOError:
                print("File not found")
                exit()
        else:
            print("Out of table")
            exit()
    else:
        print("Type error")
        exit()

def isnum(value):
    try:
        int(value)
        return True
    except BaseException:
        return False
    
def main():
    inp = sys.argv[1::]
    if(len(inp) == 0):
        print("No argumens")
        exit()
    elif(len(inp) >= 4):
        imp()
        makeGraph(inp[0], inp[1], inp[2], inp[3])
    else:
        print("Not enough argumens")
        exit()

main()
