def readOptions():
    with open('options') as f:
        currentOptions = f.readline()
        currentOptions = currentOptions.split(", ")
    return currentOptions