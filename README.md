# The Prisoner Problem (Peter Bro Miltersen, 2003)

Take N prisoners and put each one in a room individually. Each prisoner is labeled with a number M (any number 1-N). The room contains N boxes labeled 1-N, and each box contains a random number 1-N. Each prisoner is allowed to open half of all the boxes in the room. After they leave the room, all the boxes are closed and they can't communicate with the other prisoners.
If all N prisoners draw their number M from the N boxes, they are all free. However, if one prisoner does not draw their number, they are all killed. This repository contains an implementation of the "pair algorithm", which leads to a ~31% chance of survival for all the prisoners. The "pair algorithm" works by making each prisoner open up the box with their assigned number first, and then opening subsequent boxes that are the same number as the number drawn from the previously open box. This makes you go in a loop of "pairs" of numbers, starting at the farthest point from the number you are trying to find.

> Don't understand the problem or the solution? Check out [Veritasium's Video](https://www.youtube.com/watch?v=iSNsgj1OCLA) on the topic or read about it on [Wikipedia](https://en.wikipedia.org/wiki/100_prisoners_problem).

# Usage
**⚠️You must have python installed on your computer to run this script.**

Download the script, then open up a terminal and `cd` into the directory where the `prisoner_problem.py` script is located. Then, type `python prisoner_problem.py -p [NUMBER OF PRISONERS] -s [NUMBER OF SIMULATIONS]`. Replace `[NUMBER OF PRISONERS]` with the number of prisoners you want to have and `[NUMBER OF SIMULATIONS]` with the number of times you wish to simulate the prisoners picking boxes.

**Example:** `python prisoner_problem.py -p 100 -s 1000`
