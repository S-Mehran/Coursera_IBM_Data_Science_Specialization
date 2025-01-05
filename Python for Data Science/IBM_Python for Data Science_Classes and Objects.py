from matplotlib import pyplot as plt


class Circle(object):
    def __init__(self, radius = 3, color = 'blue'):
        self.radius = radius
        self.color = color


    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)


    def drawcircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle = Circle(10, "red")
print(dir(RedCircle))
print(RedCircle.radius)
print(RedCircle.color)

RedCircle.radius = 1
print(RedCircle.radius)

RedCircle.drawcircle()
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)



