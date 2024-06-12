import pygame


"""
    This class represents a simple Brick class.
    For representing bricks onto screen.
"""
class Platform (pygame.sprite.Sprite):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h
        self.__isInGroup = False
        self.note = None

    def draw(self, camera_offset):
        """
            draws the brick onto screen.
            color: rgb(56, 177, 237)
        """
        pygame.draw.rect(self.__screen, (56, 177, 237), (self._xLoc - camera_offset[0],self._yLoc - camera_offset[1], self._width,self._height),0)


    def add (self, group):
        """
            adds this brick to a given group.
        """
        group.add(self)
        self.__isInGroup = True


    def remove(self, group):
        """
            removes this brick from the given group.
        """
        group.remove(self)
        self.__isInGroup = False


    def alive(self):
        """
            returns true when this brick is belong to the brick wall.
            otherwise false
        """
        return self.__isInGroup

    def collide(self, ball):
        """
            collision deection between ball and this brick
        """
        platformX = self._xLoc
        platformY = self._yLoc
        platformW = self._width
        platformH = self._height
        ballX = ball._xLoc
        ballY = ball._yLoc
        radius = ball._radius

        if ((ballX + radius) >= platformX and ballX <= (platformX + platformW)) \
        and ((ballY + radius) >= platformY and ballY <= (platformY + platformH)):
            return True

        return False
    


"""
    This is a simple class for representing a 
    brick wall.
"""
class PlatformGroup (pygame.sprite.Group):
    def __init__ (self,screen):
        self.__screen = screen
        self._bricks = []

        
    def add(self, width, height, x, y):
        """
            adds a brick to this BrickWall (group)
        """
        platform = Platform(self.__screen, width, height, x, y)
        self._bricks.append(platform)


    def remove(self,brick):
        """
            removes a brick from this BrickWall (group)
        """
        self._bricks.remove(brick)


    def draw(self, camera_offset):
        """
            draws all bricks onto screen.
        """
        for brick in self._bricks:
            if brick != None:
                brick.draw(camera_offset)


    def update(self, ball):
        """
            checks collision between ball and bricks.
        """
        for i in range(len(self._bricks)):
            if ((self._bricks[i] != None) and self._bricks[i].collide(ball)):
                i # TODO: Play note


    def collide (self, ball):
        """
            check collisions between the ball and 
            any of the bricks.
        """
        for brick in self._bricks:
            if brick.collide(ball):
                return True
        return False