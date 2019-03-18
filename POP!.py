# program by Shirley Zhang
# ICS2O
# June 15 2018
# Jeff Radulovic
# Ics Culminating 2018
# POP! is a game where the player plays as a hot air balloon. The objective is to avoid the incoming seagulls.

import pygame
import random

pygame.init()


# move up function with window collisions
def moveUp():
    if balloc[1] < windowy - balloonheight and balloc[1] > 0:
        balloc[1] -= up


# move down function with window collisions
def moveDown():
    if balloc[1] <= windowy - balloonheight - 3 and balloc[1] >= -3:
        balloc[1] += down


# adds new seagull
def addSeagull():
    if refreshes % 120 == 0:
        sgheight = random.randint(0, windowy - seagullimgheight)
        # appends seagull with random height, and the index of the image for the animation in the sganimate list
        sgloc.append([[windowx, sgheight], 0])
        global seagull
        seagull += 1


# updates continuously moving background
def updateBG():
    # two images are used to create a continuously moving background effect
    # if the first image goes off the screen, the second is shown tailing it
    window.blit(bg, bgloc)
    window.blit(bg, sndbgloc)

    if bgloc[0] == -(bgimglen - windowx):
        sndbgloc[0] = windowx

    if bgloc[0] < -(bgimglen - windowx):
        sndbgloc[0] -= 1

    if sndbgloc[0] == -(bgimglen - windowx):
        bgloc[0] = windowx

    if sndbgloc[0] < -(bgimglen - windowx):
        bgloc[0] -= 1

    if balloc[0] == balcenterloc:
        bgloc[0] -= 1


def updateClouds():
    # two images are used to create a continuously moving background effect
    # if the first image goes off the screen, the second is shown tailing it
    window.blit(cloud, cloudloc)
    window.blit(cloud, sndcloudloc)

    if cloudloc[0] < 1 and cloudloc[0] > -(bgimglen - windowx):
        cloudloc[0] -= 0.5

    if cloudloc[0] == -(bgimglen - windowx):
        sndcloudloc[0] = windowx

    elif cloudloc[0] < -(bgimglen - windowx):
        sndcloudloc[0] -= 0.5

    if sndcloudloc[0] == -(bgimglen - windowx):
        cloudloc[0] = windowx

    elif sndcloudloc[0] < -(bgimglen - windowx):
        cloudloc[0] -= 0.5


# displays score during gameplay
def blitscore():
    global score
    if seagull > 0:
        score = seagull - 1
    else:
        score = 0
    # render text
    scoretext = font.render(str(score), False, white)
    # blits the score on the screen
    window.blit(scoretext, scoretextloc)


# executed when the replay button is clicked, resets gameplay
def replay():
    global balloc
    balloc = [0, 250]  # balloon location
    global sgloc
    sgloc = []  # seagull locations
    global bgloc
    bgloc = [0, 0]  # background location
    global sndbgloc
    sndbgloc = [windowx, 0]  # second background location for continuously moving background
    global cloudloc
    cloudloc = [0, 25]  # clouds image location
    global sndcloudloc
    sndcloudloc = [windowx, 25]  # second clouds image location for continuously moving background
    global seagull
    seagull = 0  # number of seagulls that has been displayed on the screen, used for tracking the score
    global up
    up = 0  # moving up
    global down
    down = 0  # moving down
    global refreshes
    refreshes = 0  # clears the refreshes variable
    global gamelost
    gamelost = False


# window dimensions
windowx = 792
windowy = 612
# initiates window
window = pygame.display.set_mode((windowx, windowy))
pygame.display.set_caption('POP!')

# initiates variables
white = (255, 255, 255)
balloc = [0, 250]  # balloon location
sgloc = []  # seagull locations
gamebeginterface = True
gamelost = False
bgloc = [0, 0]  # background image location
sndbgloc = [windowx, 0]
cloudloc = [0, 25]  # cloud image location
sndcloudloc = [windowx, 25]

# locations of text
playtextloc = [360, 280]
playtextbiggerloc = [350, 275]
replaytextloc = [335, 280]
replaytextbiggerloc = [320, 275]
scoretextloc = [windowx / 2, 30]
highscoreloc = [280, 340]

# button boundaries for replay and play buttons
leftbound = 360
rightbound = 480
upbound = 280
downbound = 340

bigtext = False  # becomes true when the mouse hovers over the play button
bigreplaytext = False

# dimensions of images in pixels
bgimglen = 2374  # length of the background image
balloonwidth = 148
balloonheight = 208
seagullimgwidth = 85
seagullimgheight = 47

gameoverloc = [220, 179]
up = 0
down = 0
refreshes = 0
time = 0
seagull = 0
score = 0
highscore = 0
balcenterloc = (windowx / 2) - (balloonwidth / 2)  # the location of the balloon when it is at the center of the screen

# fonts
font = pygame.font.SysFont("Impact", 45)
biggerfont = pygame.font.SysFont("Impact", 55)

# rendered text
playtext = font.render('PLAY', False, white)
playtextbigger = biggerfont.render('PLAY', False, white)
replaytext = font.render('REPLAY', False, white)
replaytextbigger = biggerfont.render('REPLAY', False, white)

# loaded images
beginterface = pygame.image.load("beginning interface actual ics .png")  # image of the beginning interface
balimg = pygame.image.load("balloon.png")  # hot air balloon
cloud = pygame.image.load("Clouds for ics .png")  # clouds in the background
bg = pygame.image.load("background-long-image-ics.png")  # long background image
gameover = pygame.image.load("game over.png")  # game over image

# frame by frame animation of the seagull
s1 = pygame.image.load("seagull 1.png")
s2 = pygame.image.load("seagull 2.png")
s3 = pygame.image.load("seagull 3.png")
s4 = pygame.image.load("seagull 4.png")
s5 = pygame.image.load("seagull 5.png")
s6 = pygame.image.load("seagull 6.png")
s7 = pygame.image.load("seagull 7.png")
s8 = pygame.image.load("seagull 8.png")
s9 = pygame.image.load("seagull 9.png")
s10 = pygame.image.load("seagull 10.png")
s11 = pygame.image.load("seagull 11.png")
s12 = pygame.image.load("seagull 12.png")
# list of images for the animation of the seagull
# two lists were made on separate lines then concatenated due to the character limit
sganimate1 = [s1, s1, s2, s2, s3, s3, s4, s4, s5, s5, s6, s6, s7, s7, s8, s8, s9, s9, s10, s10, s11, s11, s12]
sganimate2 = [s12, s11, s11, s10, s10, s9, s9, s8, s8, s7, s7, s6, s6, s5, s5, s4, s4, s3, s3, s2, s2, s1]
sganimate = sganimate1 + sganimate2

clock = pygame.time.Clock()
quit = False

while not quit:
    # event loop
    for event in pygame.event.get():

        # if user wants to exit
        if event.type == pygame.QUIT:
            quit = True

        # if the game is at the beginning interface
        if gamebeginterface:
            mpos = pygame.mouse.get_pos()  # gets mouse position

            # if the mouse hovers over the play button, displays the bigger text
            if mpos[0] > leftbound and mpos[0] < rightbound and mpos[1] > upbound and mpos[1] < downbound:
                bigtext = True
            else:
                bigtext = False

            # if the play button is pressed, begin the game
            if pygame.mouse.get_pressed()[0]:
                if mpos[0] > leftbound and mpos[0] < rightbound and mpos[1] > upbound and mpos[1] < downbound:
                    gamebeginterface = False
                    refreshes = 0

        # interface displayed when the user loses the game
        elif gamelost:
            mpos = pygame.mouse.get_pos()

            # if the mouse hovers over the replay button, display the bigger text
            if mpos[0] > leftbound and mpos[0] < rightbound and mpos[1] > upbound and mpos[1] < downbound:
                bigreplaytext = True

            else:
                bigreplaytext = False

            # if the replay button is click, replay function is called
            if pygame.mouse.get_pressed()[0]:
                if mpos[0] > leftbound and mpos[0] < rightbound and mpos[1] > upbound and mpos[1] < downbound:
                    replay()

        else:
            # if the up or down keys are pressed, move up or down respectively
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = 3

                elif event.key == pygame.K_DOWN:
                    down = 3

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = 0

                elif event.key == pygame.K_DOWN:
                    down = 0

    # displays the beginning interface
    if gamebeginterface:
        window.blit(beginterface, [0, 0])
        updateClouds()

        # if the mouse is hovering over the play button, display bigger play button
        if bigtext:
            window.blit(playtextbigger, playtextbiggerloc)
        else:
            window.blit(playtext, playtextloc)

    # displays game over interface
    elif gamelost:
        window.blit(gameover, gameoverloc)  # game over image
        # blits the high score
        highscoretext = font.render("High Score: {}".format(highscore), False, white)
        window.blit(highscoretext, highscoreloc)

        # if the mouse is hovering over the replay button, display bigger replay button
        if bigreplaytext == True:
            window.blit(replaytextbigger, replaytextbiggerloc)
        else:
            window.blit(replaytext, replaytextloc)

    # displays gameplay interface
    else:
        updateBG()  # update background
        updateClouds()  # update clouds

        window.blit(balimg, balloc)  # blits balloon
        # at the beginning, when the balloon starts on the edge of the screen, it is moved to the center
        if balloc[0] < balcenterloc:
            balloc[0] += 1

        moveUp()  # balloon is moved up
        moveDown()  # balloon is moved down
        addSeagull()  # a seagull is added every two seconds

        # goes through list containing seagull location, and the frame that the animation is on
        # enumerate gets the index as well as values in for loop
        for index, sg in enumerate(sgloc):
            # if the seagull is off the screen, remove its location from the seagulllocations list
            # this makes the collision detection more efficient
            if sg[0][0] < -seagullimgwidth:
                sgloc.pop(index)
                pass

            # blit the seagull
            window.blit(sganimate[sg[1]], sg[0])
            sg[1] += 1  # animation frame is incremented to the next frame
            # if the animation frames are exhausted, reset animation frame to the first frame
            if sg[1] == len(sganimate):
                sg[1] = 0

            else:
                sg[1] += 1
            sg[0][0] -= 3

        # implements collisions
        sgonscreen = []

        # appends the location of the sg to list to be tested for collision
        for sg in sgloc:
            sgonscreen.append(sg[0])

        # creates rectangle object around the balloon
        balrec = pygame.Rect(balloc[0], balloc[1], balloonwidth, balloonheight)

        # checks for collisions
        for sg in sgonscreen:
            # creates rectangle object around seagull
            sgrec = pygame.Rect(sg[0], sg[1], seagullimgwidth, seagullimgheight)
            # pygame.Rect.colliderect sees if the seagull rectangle and the balloon retangle are colliding
            if pygame.Rect.colliderect(sgrec, balrec):
                gamelost = True

        blitscore()  # blits the current score on the screen
        if score > highscore:
            highscore = score

    refreshes += 1
    pygame.display.update()
    clock.tick(60)

pygame.quit()
