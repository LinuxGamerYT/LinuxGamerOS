print("welcome, guest!")
while True:
    enter = input("guest-host$ ")

    if enter == "uname":
        print("linux")   
    if enter == "uname -o":
        print("linuxgamerOS")   
    if enter == "uname -r":
        print("none")   
    if enter == "uname -v":
        print("none")   
    if enter == "uname -m":
        print("x86/x86_64")   
    if enter == "uname -n":
        print("guest")
    if enter == "shutdown":
        print("shutting down...")
        
    if enter == "help":
        print("""
        uname
        help
        shutdown
        """)