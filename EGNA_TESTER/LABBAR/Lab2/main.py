from gamemodel import *
from gamegraphics import *


def graphicInput(game):
    player = game.getCurrentPlayer()
    oldAngle, oldVelocity = player.getAim()
    inputDialog = InputDialog(oldAngle, oldVelocity, game.getCurrentWind())
    output = inputDialog.interact()
    if output == "Fire!":
        newAngle, newVelocity = inputDialog.getValues()
        inputDialog.close()
        return newAngle, newVelocity
    else:
        inputDialog.close()
        return output, output

# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def graphicFinishShot(game, proj):
    gplayer = game.getCurrentPlayer()
    gotherPlayer = game.getOtherPlayer()
    distance = gotherPlayer.projectileDistance(proj)
    if distance == 0.0:
        gplayer.increaseScore()
        game.newRound()
    game.nextPlayer()

def graphicPlay():
    game = Game(10, 2)
    graphics = GraphicGame(game)
    while True:
        angle, vel = graphicInput(graphics)
        if angle == "Quit":
            return
        proj = graphicFire(graphics, angle, vel)
        graphicFinishShot(graphics, proj)

# Run the game with graphical interface
graphicPlay()
