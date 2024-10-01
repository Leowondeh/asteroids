import logging

def getFile(path):
        with open(path) as f:
            contents = f.read()
            return contents

def getVersion():
    try:
        return getFile('version')
    except FileNotFoundError:
        logging.info("Version file not found, creating")
        createFileWrite('version', '1.11.5rel')
        return getFile('version')

def createFileWrite(path, content):
        with open(path, "w") as f:
            f.write(content)