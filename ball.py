import pygame

"""
    This is a simple Ball class for respresenting a ball 
    in the game. 
"""
class Ball(object):
    def __init__ (self, screen, radius,x,y):
        self.__screen = screen
        self._radius = radius
        self._xLoc = x
        self._yLoc = y
        self.__xVel = 1
        self.__yVel = 0
        self.gravity = 0.5
        w, h = pygame.display.get_surface().get_size()
        self.__width = w
        self.__height = h

        self.colision_flag = False

    def draw(self, camera_offset):
        """
            draws the ball onto screen.
        """
        pygame.draw.circle(self.__screen,(255, 0, 0) , (self._xLoc - camera_offset[0],self._yLoc - camera_offset[1]), self._radius)

    def update(self, group):
        """
            moves the ball at the screen.
            contains some collision detection.
        """
        self._xLoc += self.__xVel

        self.__yVel += self.gravity

        self._yLoc += self.__yVel


        # for bouncing off the bricks.
        if group.collide(self):
            if  not self.colision_flag:      
                self.__yVel *= -0.8
                self.colision_flag = True
        else:
            self.colision_flag = False

    def getPosition(self):
        return [self._xLoc, self._yLoc]
