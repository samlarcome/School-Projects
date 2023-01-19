# -*- coding: utf-8 -*-
import random
import math
import sys

# Given function for distance formula 
def d(p, q):
    return (p[0] - q[0])*(p[0] - q[0]) + (p[1] - q[1])*(p[1] - q[1])

# Naive way to find closest points, taken from naive-pair.py
def Naive_pair(P):
    min_d = d(P[0], P[1])
    min_i = 0
    min_j = 1
    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            cur_d = d(P[i], P[j])
            if cur_d < min_d:
                min_d = cur_d
                min_i = i
                min_j = j
    return P[min_i], P[min_j]

def Closest_Pair(P):
    Px = sorted(P, key=lambda tup: tup[0])
    Py = sorted(P, key=lambda tup: tup[1])
    P0_star, P1_star = Closest_Pair_Rec(Px, Py)
    return P0_star, P1_star

def Closest_Pair_Rec(Px, Py):
    length = len(Px)

    #if |P| ≤ 3:
    #   find closest pair by measuring all pairwise distances 
    if length <= 3:
        return Naive_pair(Px)

    # Q = set of points in the first ceil(n/2) points in Px ("left half")
    # R = set of points in the final floor(n/2) points in Py ("Right half")
    mid = length//2

    # SETTING UP RECURSION
    # Construct Qx, Qy, Rx, Ry in O(n) time
    #Qx = []                                -> Qx = consisting of the points in Q sorted by increasing xcoordinate
    Qx = Px[:mid]
    #Qy = []                                -> Qy = consisting of the points in Q sorted by increasing y-coordinate
    Qy = sorted(Qx, key=lambda tup: tup[1])
    #Rx = []                                -> Rx = consisting of the points in R sorted by increasing x-coordinate
    Rx = Px[mid:]
    #Ry = []                                -> Ry = consisting of the points in R sorted by increasing y-coordinate
    Ry = sorted(Rx, key=lambda tup: tup[1])

    # (q*0, q*1) = Closest-Pair-Rec(Qx, Qy)
    qstar0, qstar1 = Closest_Pair_Rec(Qx, Qy)
    # (r*0, r*1) = Closest-Pair-Rec(Rx, Ry)
    rstar0, rstar1 = Closest_Pair_Rec(Rx, Ry)

    #COMBINING THE SOLUTIONS   
    dqstar = math.sqrt(d(qstar0, qstar1))               # distance between qstar0 and qstar1 for later use
    drstar = math.sqrt(d(rstar0, rstar1))               # distance between rstar0 and rstar1 for later use

    # delta = min(d(q*0, q*1), d(r*0, r*1))
    delta = min(dqstar, drstar)

    # xstar = max x-coordinate of a point in set Q
    # L is vertical line described by x = xstar
    L = xstar = Qx[-1][0]                               # max x-coordinate in set Q is stored as rightmost value in Qx

    # S = set of points in P within distance delta of L (xstar)
    S = set()
    for i in range(length):                 # For each pount in Px, add it to the set S if - 
        if abs(L - Px[i][0]) < delta:       # - it is within distance delta of the line L
            S.add(Px[i])

    # Construct Sy in O(n) time
    Sy = list()
    for point in Py:                    # Add every point (to Sy) that is in Py which is also in -
        if point in S:                  # - the set S
            Sy.append(point)

    smallest_distance = 10000000000     # make smallest distance a large enough number to begin with
    smallest_pair = tuple()             # smallest pair is empty to begin

    # For each point s in Sy:
    #   compute distance from s to each of next 15 points in Sy
    #   Let (s, s') be the pair achieving min of these distances
    #   O(n) time
    for i in range(len(Sy)):                            # For each point in Sy
        for j in range(1, 16):                              # For j = 1,2,...,15
            try:                                                # try
                dis = math.sqrt(d(Sy[i], Sy[i+j]))                  # find distance between s and next jth point
                if dis < smallest_distance:                         # Logic to update if it is the smallest distance
                    smallest_distance = dis
                    smallest_pair = (Sy[i], Sy[i+j])    
            except IndexError:                             
                break                                     # break if there is an index out of bound error (i.e. we are w/in 15 points of the end of Sy)

    # if d(s, s') < delta
    #   Return (s, s')
    # else if d(q0*, q1*) < d(r0*, r1*)
    #   Return (q0*, q1*)
    # else
    #   return (r0*, r1*)

    if smallest_distance < delta:       # Logic to return the smallest pair found
        return smallest_pair
    elif dqstar < drstar:
        return (qstar0, qstar1)
    else:
        return (rstar0, rstar1)


# do not change the code below
random.seed(12345)
P = []
for i in range(int(sys.argv[1])):
    P.append((random.random(), random.random()))

p1, p2 = Closest_Pair(P)
print(p1, p2, math.sqrt(d(p1, p2)))