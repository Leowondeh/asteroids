from func.fileManagement import getVersion

def sendGreeting(type):
    # start
    if type == "startgame":
        print(f"""
    ╔═══════════════════════╗
    ║  Asteroids! v{getVersion()} ║
    ║                       ║
    ║      Has started!     ║
    ║ Use WASD to move and  ║
    ║    SPACE to shoot     ║
    ╚═══════════════════════╝""")
    elif type == "startprogram":
        print(f"""
    ╔═══════════════════════╗
    ║  Asteroids! v{getVersion()} ║
    ║                       ║
    ║        Welcome!       ║
    ║                       ║
    ║ s - Start the game    ║
    ║ o - Options menu      ║
    ╚═══════════════════════╝""")

    # exit
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