from math import sin,cos,radians
import random

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        self.csize = cannonSize
        self.bsize = ballSize 
        self.p0 = Player(self, "blue", -90)
        self.p1 = Player(self, "red", 90)
        self.wind = 0
        self.currentPlayer = self.p0

    """ A list containing both players """
    def getPlayers(self):
        return [self.p0, self.p1]

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.csize

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.bsize

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.currentPlayer

    """ The opponent of the current player """
    def getOtherPlayer(self):
        if self.getCurrentPlayer() is self.p0:
            return self.p1
        else:
            return self.p0
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        if self.getCurrentPlayer() is self.p0:
            return 0 
        else:
            return 1
    
    """ Switch active player """
    def nextPlayer(self):
        self.currentPlayer = self.getOtherPlayer()

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.wind = wind     

    def getCurrentWind(self):
        return self.wind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.wind = random.random() * 20 - 10


""" Models a player """
class Player:
    def __init__(self, game, color, position):
        self.game = game
        self.pos = position
        self.color = color
        self.score = 0
        self.lastProjAngle = 45
        self.lastProjVelocity = 40

    """ Create and return a projectile starting at the centre of this players cannon. 
        Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        self.lastProjVelocity = velocity
        self.lastProjAngle = angle
        if self is self.game.p1:
            self.projectile = Projectile(180 - self.lastProjAngle, self.lastProjVelocity, self.game.getCurrentWind(), self.getX(), self.game.csize/2, -110, 110)
        else:
            self.projectile = Projectile(self.lastProjAngle, self.lastProjVelocity, self.game.getCurrentWind(), self.getX(), self.game.csize/2, -110, 110)
        return self.projectile

    """ Gives the x-distance from this players cannon to a projectile. 
        If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon 
        and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        if proj.getY() == 0.0:
            ballRight = proj.getX() + self.game.getBallSize()
            ballLeft = proj.getX() - self.game.getBallSize()
            cannonLeft = self.getX() - self.game.getCannonSize()/2
            cannonRight = self.getX() + self.game.getCannonSize()/2
            dist1 = ballRight - cannonLeft 
            dist2 = ballLeft - cannonRight
            
            if dist1 < 0 and dist2 < 0:
                distance = max(dist1, dist2)
            else:
                distance = min(dist1, dist2)
            if  cannonLeft <= ballRight <= cannonRight or cannonLeft <= ballLeft <= cannonRight:
                distance = 0
            return distance

    """ The current score of this player """
    def getScore(self):
        return self.score

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.score += 1

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.pos

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return (self.lastProjAngle, self.lastProjVelocity)

""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind

    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
        for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos