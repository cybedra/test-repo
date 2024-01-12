import sys

def print_hello_world():
    print("Hello World!")

def print_sys_props():
    print(sys.version)
    print(sys.executable)
    print(sys.path)
    
def main():
    print("Hello World!")
    
    print_hello_world()
    print_sys_props()
    
main()