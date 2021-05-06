import json
import sys
from pathlib import Path

# Returns True if a string is valid JSON,False otherwise
def isValidString(data):
    try:
        jsonDict = json.loads(data)
    except json.decoder.JSONDecodeError:
        print("Invalid JSON object.")
        return False
    except TypeError:
        return False
    return True


# Returns True if a file contains valid JSON data
def isValidJson(fileData):
    try:
        json.load(fileData)
        return True
    except json.decoder.JSONDecodeError:
        print("Invalid JSON object.")
    except AttributeError:
        print("No input file detected.")
    return False


# Returns True if a file exists and is valid JSON, False otherwise
def isValidFile(path):
    try:
        # Check if the file exists
        file = open(path)
        if isValidJson(file):
            return True
    except OSError as e:
        print(e)
    except TypeError:
        pass
    return False


def isValidKey(key):
    try:
        if key == None or key == "" or "." in key:
            raise KeyError
    except KeyError:
        print("The key can neither be an empty string, nor contain a '.'")
        return False
    return True


# Returns the path of the input file if passed as an argument
def getPath():
    try:
        filePath = Path(sys.argv[1])
        return filePath
    except IndexError:
        print("Invalid JSON object.")
        return


# Get data from json file
def getJsonData():
    jsonStr = ""
    for line in sys.stdin:
        jsonStr += line
    return jsonStr


# Load JSON object into a dictionary
def loadData():
    """If the script is executed as standalone, load the data from the file into
    a dictionary. Otherwise, if it is executed as part of a pipe or file redirection, 
    get the data from stdin and load it into a dictionary. If all validations are passed,
    it returns the json object loaded into a dictionary. Returns None otherwise."""

    # If the script is executed as standalone
    if sys.stdin.isatty():
        filePath = getPath()
        # Load the object into a dictionary if the file is validated and return the dictionary
        if isValidFile(filePath):
            filename = open(filePath)
            objDict = json.load(filename)
            return objDict
    # If the script is executed as part of a pipe or file redirection
    else:
        data = getJsonData()
        # If it is a valid JSON string, load the string into a dictionary and return the dictionary
        if isValidString(data):
            objDict = json.loads(data)
            return objDict


resultDict = {}
def flatten(json_obj, fullPath = ""):
    # Base case: the value does not contain any nested key-value pairs so it is a terminal value
    if type(json_obj) != dict:
        resultDict[fullPath[:-1]] = json_obj
    # Call the function recursively to add all keys to the path until it reaches the terminal value
    else:
        for key in json_obj:
            if isValidKey(key):
                flatten(json_obj.get(key), fullPath + key + ".")


# Driver code
def main():
    unflattenedJson = loadData()     # First load the data
    if unflattenedJson != None:      # If there is a valid JSON object proceed further
        flatten(unflattenedJson)     # Populates resultDict with the new key-value pairs
        with open("output.json","w") as outfile:
            json.dump(resultDict, outfile, indent=4)   # Convert dict object into a new valid json object        


if __name__ == '__main__':
    main()
