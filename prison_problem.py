import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--prisoners", type=int)
parser.add_argument("-s", "--simulations", type=int)

args = parser.parse_args()
PRISONERS = args.prisoners
SIMULATIONS = args.simulations

if PRISONERS == None or SIMULATIONS == None:
    print("[ERROR] Please specify the number of prisoners and simulations to run using the `-p` and `-s` flags (example: `-p 100 -s 1000`). For more help, use the `--help` flag.")
    exit(1)
OPENABLE = PRISONERS / 2

successful = 0
failed = 0

for simulationNumber in range(1, SIMULATIONS + 1):
    # Generate numbers, prisoners and pairs
    numbers = [m for m in range(1, PRISONERS + 1)]
    prisoners = [n for n in range(1, PRISONERS + 1)]
    pairs = []

    for j in range(PRISONERS):
        insideBox = random.choice(numbers)
        numbers.remove(insideBox)

        pairs.append((j + 1, insideBox))
    # Sort
    pairs.sort()
    # Run sim
    count = 0
    prisonerNum = 0
    print("--------------")
    for i in range(len(prisoners)):

        prisonerNum = prisoners[i]  # 1

        peek = pairs[prisonerNum - 1][1]
        # print("[" + str(simulationNumber) + "] " + "Prisoner #" + str(prisonerNum) + " is attempting to find their number.")
        count += 1

        while peek != prisonerNum:
            count += 1
            peek = pairs[peek - 1][1]
            # print("[" + str(simulationNumber) + "] " + "On try #" + str(count) + " prisoner #" + str(prisonerNum) + " has found number " + str(peek) + "." )

        if count > OPENABLE:
            break
        count = 0

    if prisonerNum == len(prisoners):
        successful += 1
        print("[" + str(simulationNumber) + "] " +
              "All prisoners found their number successfully.")
    else:
        failed += 1
        print("[" + str(simulationNumber) + "] " + "Prisoner #" +
              str(prisonerNum) + " has not escaped and the simulation has failed.")

# Result
print("--------------")
print("After " + str(SIMULATIONS) + " runs, the " + str(PRISONERS) + " prisoners escaped " + str(successful) + " times and got killed " +
      str(failed) + " times, or " + str(round((successful / SIMULATIONS), 2)) + "% of time.")
