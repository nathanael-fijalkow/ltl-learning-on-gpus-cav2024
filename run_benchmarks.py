import glob
import argparse
import os
import sys
import csv
import time

sys.path.append("/code")
from dc import *

dcAlgo = RandSplit  # Random splitting
window = 64	# 64 is max traces number in this version
costfun = [1, 1, 1, 1, 1, 1, 1, 1]  # Costs of (a, ~, &, |, X, F, G, U)
maxCost = 500	# A big-enough cost
RlxUnqChkType = 3	# 3 = ModifiedMuellerHash
NegType = 1	# 2 = negOfChar, 1 = can use negation anywhere
timeout = 2000 # 2000 sec

def generate_commands(folder_list):
	# print(folder_list)
	for folder in folder_list:
		for file in glob.glob(folder + "/*.trace"):
			print(file)

			# runDC(file, dcAlgo, window, costfun, maxCost, RlxUnqChkType, NegType, timeout)

			with open(file, 'r') as f:
				content = f.read()

			pos = content.split("\n")[:content.split("\n").index("---")]
			neg = content.split("\n")[content.split("\n").index("---")+1:-4]
			alphabet = content.split("\n")[-1]

			start_time = time.time()
			res = runWithTimeout(dcAlgo, [window, pos, neg, alphabet, costfun, maxCost, RlxUnqChkTyp, NegTyp], timeout=timeout)
			end_time = time.time()

			fieldnames = ['file', 'time', 'formula']
			filename = "results_VFB.csv"
			file_exists = os.path.exists(filename)

			experiment_data = {"file": file, "time": round(end_time - start_time, 3), "formula": res}
			with open(filename, 'a', newline='') as csvfile:
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				if not file_exists:
					writer.writeheader()  # Write header only if the file is new
				writer.writerow(experiment_data)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Run VFB on all benchmarks in a list of folders")
	parser.add_argument("folders", nargs="+", help="List of folders")

	args = parser.parse_args()

	generate_commands(args.folders)