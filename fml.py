#! python3
# Takes raw XML from clipboard and prettifies it

# Has dependency on 'lxml'
from bs4 import BeautifulSoup
import pyperclip
import sys
import os

OUTPUT = "output"
OUTPUT_FILE = "fml.txt"


def main():
    if len(sys.argv) > 1:
        print("USAGE: fml.py")
        sys.exit()

    # Read XML string from clipboard
    data = pyperclip.paste()

    # Parse the XML string with BeaytifulSoup
    data = BeautifulSoup(data, "xml")
    
    # Check if user supplied correct XML
    if len(data.contents) == 0:
        print("Application error: No valid XML string was found in clipboard")
        sys.exit()

    # Prettify the parsed XML string
    data = data.prettify()

    # Create directory for output 
    if OUTPUT not in os.listdir():
        path = os.path.dirname(os.path.abspath(__file__))
        os.mkdir(os.path.join(path, OUTPUT))

    # Write parsed XML to file
    with open(os.path.join(OUTPUT, OUTPUT_FILE), "w") as f:
        f.write(data)

    # Open output file
    os.startfile(os.path.join(OUTPUT, OUTPUT_FILE))

    # Copy the parsed XML to clipboard
    pyperclip.copy(data)

    # Finish script gracefully
    print("Format-XML has been successfully executed")


if __name__ == "__main__":
    main()
