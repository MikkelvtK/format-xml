#! python3
# Takes raw XML from clipboard and prettifies it

# Has dependency on 'lxml'
from bs4 import BeautifulSoup
import pyperclip
import subprocess
import sys
import os

OUTPUT_DIR = "output"
OUTPUT_FILE = "fml.xml"


def main():
    if len(sys.argv) > 1:
        print("USAGE: fml.py")
        sys.exit(1)

    # Read XML string from clipboard
    data = pyperclip.paste()

    # Parse the XML string with BeaytifulSoup
    data = BeautifulSoup(data, "xml")
    
    # Check if user supplied correct XML
    if len(data.contents) == 0:
        raise_error("no valid XML string was found in clipboard")

    # Prettify the parsed XML string
    data = data.prettify()

    # Get absolute path
    path = os.path.dirname(os.path.abspath(__file__))

    # Create directory for output 
    if OUTPUT_DIR not in os.listdir(path):
        os.mkdir(os.path.join(path, OUTPUT_DIR))

    # Get output file path
    file_path = os.path.join(path, OUTPUT_DIR, OUTPUT_FILE)

    # Write parsed XML to file
    with open(file_path, "w") as f:
        bytes_written = f.write(data)

        if bytes_written == 0:
            raise_error("no output was written to output file")

    # Copy the parsed XML to clipboard
    pyperclip.copy(data)

    # Open output file
    subprocess.run(args=[file_path], shell=True)

    # Finish script gracefully
    print("Format-XML has been successfully executed")
    sys.exit(0)


def raise_error(msg: str):
    print("Application error: " + msg)
    sys.exit(1)
    

if __name__ == "__main__":
    main()
