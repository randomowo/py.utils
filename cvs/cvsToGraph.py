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
    
def makeGraph(cvs_txt, x_column, y_columns, labels):
    if (isinstance(cvs_txt, str) and isnum(x_column)):
        x_c = int(x_column)
        y_arr = []
        label_arr = []
        for label in labels.split(","):
            if (isinstance(label, str)):
                label_arr.append(label)
            else:
                print("Type Error")
                exit()
        for y in y_columns.split(","):
            if (isnum(y)):
                y_arr.append(int(y))
            else:
                print("Type Error")
                exit()
        if (len(label_arr) != 1 and len(label_arr) != len(y_arr)):
            print("Input error")
            exit()
        elif(len(label_arr) == 1 and len(y_arr) > 1):
            l = label_arr[0]
            label_arr = []
            for i in range(0, len(y_arr)):
                label_arr.append(l+str(i+1))
        for index in range(0, len(y_arr)):
            y_c = y_arr[index]
            label = label_arr[index]
            if (x_c >= 0 and y_c >= 0):
                import numpy
                import matplotlib.pyplot as plt
                try:
                    per_data=numpy.genfromtxt(r"%s" % cvs_txt,delimiter='\t',names=True)
                    y = per_data.dtype.names[y_c]
                    x = per_data.dtype.names[x_c]
                    plt.plot(per_data[x], per_data[y], label=label)
                    plt.legend(loc=0)
                except IOError:
                    print("File not found")
                    exit()
            else:
                print("Out of table")
                exit()
        plt.xlabel ('X')
        plt.ylabel ('Y')
        plt.grid()
        plt.show()
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
