import sys
import re

def remove_header_policy(input_text:str)->str:
    header_policy_pattern = re.compile(r'config global header policy\n.*?end', re.DOTALL)
    # Remove the header policy section
    updated_config = re.sub(header_policy_pattern, '', input_text)
    return updated_config


def main(infile):
    with open(infile,"r") as file:
        input_text = file.read()
        file.close()
    updated = remove_header_policy(input_text=input_text)

    with open(infile,"w") as wfile:
        wfile.write(updated)

    print(updated)

if len(sys.argv) != 1:
    input_file = sys.argv[1]
    main(input_file)