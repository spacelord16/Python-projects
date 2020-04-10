import os,sys

tag=sys.argv[1]
help_menu="""
Available tags
-help This menu
-r    Restart
-s    Shutdown
-t    Timer
"""

def update():
    os.system("sudo pacman -Syy")
    os.system("sudo pacman -Su")

def clean():
    os.chdir('/home/majaroo/.local/share/Trash')
    if len(sys.argv) >=2 :
        if sys.argv[1] == '-t' or sys.argv[1] == '-T' :
            os.system("tree ./ ")
        elif sys.argv[1] == '-l' or sys.argv[1] == '-L':
            os.system("ls -al")

    os.system("rm -rf")
    print("Trash Clean")

def shutdown():
    tags=['-help','-r','-s','-t']
    if tag in tags :
        if tag == 'help' :
            print("help_menu")
        elif tag == '-r' :
            print("restart")
        elif tag == '-s' :
            update()
            clean()
            os.system("sudo shutdown -h now")
        elif tag == '-t' :
            time=int(input("Minutes to shutdown"))
            update()
            clean()
            downtime = f"sudo shutdown -h {time}"
            os.system(downtime)
    else:
        print(f"Argument Invalid!{help_menu}")

if __name__ == '__main__':
    shutdown(tag)
