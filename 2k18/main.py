import dataset
import argparse

#Arguments(use when start script)
parser = argparse.ArgumentParser()
parser.add_argument("input", help="path to input file")
parser.add_argument("output", help="path to output file")
args = parser.parse_args()

<<<<<<< HEAD
dataset.readfile(args.input)
dataset.writefile(args.output)
#Some changes
=======
#test

print(dataset.readfile(args.input))
dataset.writefile(args.output)
>>>>>>> d76ccd626ebd08c17a6f120ccda3ececfd7b085e
