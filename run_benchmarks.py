import glob
import argparse
import os
import sys
# sys.path.append("/code")
from dc import *

def generate_commands(folder_list):
	# print(folder_list)
	for folder in folder_list:
		for file in glob.glob(folder_list + "/*.trace"):
			print(file)
			dcAlgo = RandSplit                  # Random splitting
			window = 64                         # 64 is max traces number in this version
			costfun = [1, 1, 1, 1, 1, 1, 1, 1]  # Costs of (a, ~, &, |, X, F, G, U)
			maxCost = 500                       # A big-enough cost
			RlxUnqChkType = 3                   # 3 = ModifiedMuellerHash
			NegType = 1                         # 2 = negOfChar, 1 = can use negation anywhere
			timeout = 2000                      # 2000 sec

			runDC(file, dcAlgo, window, costfun, maxCost, RlxUnqChkType, NegType, timeout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run VFB on all benchmarks in a list of folders")
    parser.add_argument("folders", nargs="+", help="List of folders")

    args = parser.parse_args()

    generate_commands(args.folders)