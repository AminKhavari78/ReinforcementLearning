import pygame
from pygame.locals import *
import numpy as np
import time
import random, math
from enum import Enum
from random_search import Harness, random_search, LinearAgent


def step(action):
    match action:
        case 0:
            return [0, -25]
        case 1:
            return [0, -25]
        case 2:
            return [0, 25]
        case 3:
            return [-25, 0]
        case 4:
            return [25, 0]


def main():

    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()

    # create the display surface object
    # of specific dimension.
    width, height = (29*20, 30*20)
    screen = pygame.display.set_mode((width, height))

    # Add caption in the window
    pygame.display.set_caption('Allelopathic Harvest')

    # Add player sprite
    agent = pygame.image.load('agent/agent.png')
    bot = pygame.image.load('agent/bot.jpeg')

    # Add Berry sprite
    blue_berry_ripe = pygame.image.load('berry/blue_berry_ripe.jpeg')
    blue_berry_unripe = pygame.image.load('berry/blue_berry_unripe.jpeg')

    red_berry_ripe = pygame.image.load('berry/red_berry_ripe.jpeg')
    red_berry_unripe = pygame.image.load('berry/red_berry_unripe.jpeg')

    # move step for (agent, bot)
    move_step = 25

    DEFAULT_IMAGE_SIZE_AGENT = (50, 50)
    DEFAULT_IMAGE_SIZE_BERRY = (20, 20)

    # Scale the image to your needed size
    agent = pygame.transform.scale(agent, DEFAULT_IMAGE_SIZE_AGENT)
    bot = pygame.transform.scale(bot, DEFAULT_IMAGE_SIZE_AGENT)

    blue_berry_ripe = pygame.transform.scale(blue_berry_ripe, DEFAULT_IMAGE_SIZE_BERRY)
    blue_berry_unripe = pygame.transform.scale(blue_berry_unripe, DEFAULT_IMAGE_SIZE_BERRY)

    red_berry_ripe = pygame.transform.scale(red_berry_ripe, DEFAULT_IMAGE_SIZE_BERRY)
    red_berry_unripe = pygame.transform.scale(red_berry_unripe, DEFAULT_IMAGE_SIZE_BERRY)


    # Store the initial and changes
    # coordinates of the player in
    # two variables i.e. x and y.
    current_state_agent_bot = {
        'agent': [400, 400],
        'bot': [150, 75],
    }


    # Create a variable to store the
    # velocity of player's movement
    speed = 10
    container = {}
    for i in range(24):
        for j in range(23):
            selection_list = ['agent', 'bot']
            selected = random.choice(selection_list)
            if selected == "agent":
                agent_code = f"{selected}{i}{j}"
                container[agent_code] = [blue_berry_unripe, j*25, i*25]
            elif selected == "bot":
                bot_code = f"{selected}{i}{j}"
                container[bot_code] = [red_berry_unripe, j*25, i*25]
    #print(len(container.keys()))
    #print(container.values())

    # store ripen rate and (agent,bot) Code
    ledger = {}
    total = len(container)
    counter_blue = 0
    counter_red = 0
    for color in container.values():
        if color[0] == blue_berry_unripe:
            counter_blue += 1
        else:
            counter_red += 1

    ripen_rate_blue = math.floor(total/counter_blue)
    ripen_rate_red = math.floor(total/counter_red)

    for key in list(container.keys()):
        if 'agent' in key:
            ledger[key] = ripen_rate_blue
        else:
            ledger[key] = ripen_rate_red



    # Creating an Infinite loop
    run = True
    while run:

        # Filling the background with
        # white color
        screen.fill((255, 255, 255))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get()
        # method.
        for event in pygame.event.get():

            # Closing the window and program if the
            # type of the event is QUIT
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        # blit all berry
        for color, x, y in container.values():
            screen.blit(color, (x, y))

        # Display the player sprite at x
        # and y coordinates
        screen.blit(agent, (current_state_agent_bot['agent'][0], current_state_agent_bot['agent'][1]))
        screen.blit(bot, (current_state_agent_bot['bot'][0], current_state_agent_bot['bot'][1]))

        random_search()

        pygame.display.update()


main()

