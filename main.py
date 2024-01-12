import sys

def print_sys_props():
    print(sys.version)
    print(sys.executable)
    print(sys.path)
    

def main():
    print("Hello World!")
    print_sys_props()
    
main()