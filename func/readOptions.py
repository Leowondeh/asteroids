import logging
from fileManagement import createFileWrite

def readOptions():
    try:
        with open('options') as f:
            currentOptions = f.readline()
            currentOptions = currentOptions.split(", ")
        return currentOptions
    except FileNotFoundError:
        logging.info("Options file not found, creating using defaults")
        createFileWrite()