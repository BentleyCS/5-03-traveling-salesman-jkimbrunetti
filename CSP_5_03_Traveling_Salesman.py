import math
import random

import pygame
import itertools

def getPathDistance(places : list):
    dist = 0
    for i in range(len(places) - 1):
        dist += getDistance(places[i], places[i + 1])
    dist += getDistance(places[-1], places[0])
    return dist

def full_TSP(places : list):
    bestRoute = []
    bestDistance = float('inf')
    calculations = 0

    allPermutations = generatePermutations(places)

    for perm in allPermutations:
        route = list(perm)
        dist = getPathDistance(route)
        calculations += 1
        if dist < bestDistance:
            bestDistance = dist
            bestRoute = route

    print(f"there were {calculations} calculations for full TSP")
    return bestRoute

def hueristic_TSP(places : list):
    calculations = 0
    unvisited = places.copy()
    path = []

    current = unvisited.pop(0)
    path.append(current)

    while unvisited:
        bestDist = float('inf')
        bestIndex = -1

        for i, node in enumerate(unvisited):
            dist = getDistance(current, node)
            calculations += 1
            if dist < bestDist:
                bestDist = dist
                bestNode = node
                bestIndex = i

        current = unvisited.pop(bestIndex)
        path.append(current)

    print(f"there were {calculations} calculations for hueristic TSP")
    return path

def generatePermutations(places : list):
    # a function that given a list will return all possible permutations of the list.
    return list(itertools.permutations(places))


def getDistance(spot1, spot2):
    dist = math.sqrt((spot1[0] - spot2[0]) ** 2 + (spot1[1] - spot2[1]) ** 2)
    return dist


def generate_RandomCoordinates(n):
    #Creates a list of random coordinates
    newPlaces = []
    for i in range(n):
        newPlaces.append([random.randint(10,790),random.randint(10,590)])
    return newPlaces

places = [[80,75],[100,520],[530,300],[280,200],[350,150],[700,120],[400,500]]


def DrawExample(places):
    return

DrawExample(places)
