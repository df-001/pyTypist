#Import Dependencies
from settings import settingsMenu
import pygame
from random import sample
import sys

pygame.display.set_caption("typingProject")

wordCount = settingsMenu()
print(wordCount)

#Loading dictionary.txt values into memory
word_bank = []
with open(r"./typingProject_data/dictionary.txt", "rt") as file:
    for line in file:
        word_bank.append(line.strip())
#Create word list with length
word_list = sample(word_bank, wordCount)

#Define a class to create key presses
class KeyTrigger:
    def __init__(self, key, holdTime):
        self.key = f"pygame.K_{key}"
        self.holdTime = holdTime
    def keyPress(self, keyActive):
        if keyActive[eval(self.key)]:
            if self.holdTime >= 1:
                pass
            else:
                print(self.key, "pressed.")
                self.holdTime += 1
        else:
            self.holdTime = 0
    def nextWord(self, keyActive):
        if keyActive[eval(self.key)]:
            if self.holdTime >= 1:
                pass
            else:
                print(self.key, "pressed.")
                self.holdTime += 1
        else:
            self.holdTime = 0

#Imports all keypress instances and add their name to a list
instanceList = []
with open(r"./typingProject_data/instanceCreator.ext", "rt") as kD:
    for line in kD:
        instanceList.append(line.split()[0])
        exec(line.strip())


#pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1030))
clock = pygame.time.Clock()
running = True
bgcolour = (16,16,32)
dt = 0
current_word, current_word_index, current_location = word_list[0], 0, 0
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(bgcolour)

    #Get currently pressed keys
    activeKeys = pygame.key.get_pressed()
    #Iterate through all active keys to check for and process input
    for i in range(27):
        eval(instanceList[i]).keyPress(activeKeys)
    eval(instanceList[i]).nextWord(activeKeys)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()