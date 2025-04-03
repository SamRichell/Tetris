import pygame

class Square:
    def __init__(self, length, screen, x, y):
        self.__screen = screen
        self.__length = length
        self.__x = x
        self.__y = y

    def render(self):    # Draw 4 lines representing the edge of each square
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y], [self.__x, self.__y + self.__length])
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y], [self.__x + self.__length, self.__y])
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y + self.__length], [self.__x + self.__length, self.__y + self.__length])
        pygame.draw.line(self.__screen, "white", [self.__x + self.__length, self.__y], [self.__x + self.__length, self.__y + self.__length])

class Container:
    def __init__(self, screen, width, height, square_length):
        self.__screen = screen
        self.__width = width * square_length
        self.__height = height * square_length
        self.__squares = []
        self.__centre()
        self.__initiate_squares(square_length)

    def __initiate_squares(self, square_length):    # Initiate squares array
        start_x = self.__x
        y = self.__y
        x = start_x
        for i in range (0, (self.__width * self.__height)):
            print(f"x: {x}\ny: {y}\n\n")
            self.__squares.append(Square(self.__square_length, self.__screen, x, y))
            if x < (self.__width):
                x += square_length
            else:
                x = start_x
                y += square_length

    def __centre(self):    # Find pixel position of top left of container
        self.__x = (self.__screen.get_width() // 2) - (self.__width)
        self.__y = (self.__screen.get_height() // 2) - (self.__height)

    def render(self):    # Render box then squares
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y], [self.__x, self.__y + self.__height])
        pygame.draw.line(self.__screen, "white", [self.__x, self.__y + self.__height], [self.__x + self.__height, self.__y + self.__height])
        pygame.draw.line(self.__screen, "white", [self.__x + self.__height, self.__y], [self.__x + self.__height, self.__y + self.__height])
        for square in self.__squares:
            square.render()