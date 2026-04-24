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
    bestDistance = float('n')
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
    #Draws the TSP showcase to the screen.
    TSP = full_TSP(places.copy())
    Hueristic = hueristic_TSP(places.copy())
    # Initialize Pygame
    pygame.init()
    print(TSP)
    print(Hueristic)
    # Set up the game window
    screen = pygame.display.set_mode((800, 800))
    # Game loop
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render('Hello, Pygame!', True, (0, 0, 0))
    text_surface.set_colorkey((0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (300, 700)  # Center the text on the screen
    # Arguments: text string, antialias boolean (True for smooth edges), text color, optional background color
    text_surface = font.render('Hello, Pygame!', True, (255, 255, 255))  # White text
    while running:
        screen.fill((255,255,255))
        for i in range(len(TSP)-1):
            pygame.draw.line(screen,(255,0,0),(TSP[i][0],TSP[i][1]),(TSP[i+1][0],TSP[i+1][1]),width = 8)
        if len(TSP) >=1:pygame.draw.line(screen, (255, 0, 0), (TSP[0][0], TSP[0][1]), (TSP[-1][0], TSP[-1][1]),width =8)
        for i in range(len(Hueristic) - 1):
            pygame.draw.line(screen, (0, 0, 255), (Hueristic[i][0], Hueristic[i][1]), (Hueristic[i + 1][0], Hueristic[i + 1][1]), width=4)
        if len(Hueristic) >=1:pygame.draw.line(screen, (0, 0, 255), (Hueristic[0][0], Hueristic[0][1]), (Hueristic[-1][0], Hueristic[-1][1]), width=4)
        for spot in places:
            pygame.draw.circle(screen, (0,0,0),(spot[0],spot[1]), 10)
        text_surface = font.render('Red is full TSP Blue is Heuristic', True, (0, 0, 0))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    # Quit Pygame

DrawExample(places)
#DrawExample(generate_RandomCoordinates(5))# DO NOT run more than 9 or 10
pygame.quit()