from time import sleep
import os
from func.fileManagement import getVersion

def sendGreeting(type):
    # start
    if type == "start":
        print(f"""
    ╔═══════════════════════╗
    ║  Asteroids! v{getVersion()} ║
    ║                       ║
    ║      Has started!     ║
    ║ Use WASD to move and  ║
    ║    SPACE to shoot     ║
    ╚═══════════════════════╝""")

    # exit (unused, use if need to save)
    elif type == "gameover":
        print("""
    ╔═══════════════════════╗
    ║       Asteroids!      ║
    ║                       ║
    ║       Game over!      ║
    ║ Use r to restart or   ║
    ║       q to exit       ║
    ╚═══════════════════════╝
          """)

    # quick exit
    elif type == 'quickexit':
        print("""
    ╔═══════════════════════╗
    ║       Asteroids!      ║
    ║                       ║
    ║       Exiting...      ║
    ║        Goodbye!       ║
    ╚═══════════════════════╝
          """)
    # else it's an error
    else:
        raise TypeError