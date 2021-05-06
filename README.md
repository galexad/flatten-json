Python3 version: 
Python 3.8.5


Running the file:

1. Standalone by passing the json object as a command line argument to the code

    python3 flatten.py test.json



2. As part of a pipe/file redirection

    cat test.json | python3 flatten.py


The code takes one input argument: a JSON object, and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure.

I have made some additional assumptions that were not specified in the task.

Additional assumptions
- A key is valid even if it contains characters like "," or "*" as long as it does not contain the "." character.
- A key is not valid if the string is empty "".
- An empty file is an invalid json object.
- The flattened version of the object will be written to a new .json file called "output.json".


Total amount of time spent on the task: ~6 hours.

