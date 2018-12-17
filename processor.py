import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="Provide file path of the text file containing an IP or subnet in each line")
parser.add_argument("action", help="nmap,ssl")
parser.add_argument("-o", "--output", help="output file name")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()


if args.action=="nmap":
    print("running nmap on the provided list")
elif args.action=="ssl":
    print("running ssl scan on the provided list")
