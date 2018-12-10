import numpy as np
np.set_printoptions(threshold=np.nan)





class Point():
    def __init__(self,x,y,v_x,v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
    def update(self):
        self.x += self.v_x
        self.y += self.v_y
    def distance_to(self, point):
        return abs(point.x-self.x) + abs(point.y-self.y)



#Read in data
def read_data():
    with open('input.txt') as f:
        content = f.readlines()
    points = []
    for line in content:
        x = int(line[10:16])
        y = int(line[18:24])
        v_x = int(line[36:38])
        v_y = int(line[39:42])
        points.append(Point(x,y,v_x,v_y))
    return points

def get_dist_apart(): #Returns number of points which are within 100 of each other
    reference = points[0]
    count = 0
    threshhold = 100
    for i in range(1,len(points)):
        dist = reference.distance_to(points[i])
        if dist < threshhold:
            count += 1
    return count

def create_sky(points):
    #Find range of points
    max_x = 0
    max_y = 0
    min_x = 9999
    min_y = 9999
    for point in points:
        if point.x > max_x:
            max_x = point.x
        if point.y > max_y:
            max_y = point.y
        if point.x < min_x:
            min_x = point.x
        if point.y < min_y:
            min_y = point.y
    x_range = abs(min_x - max_x)
    y_range = abs(min_y - max_y)
    sky = np.zeros((x_range+1, y_range+1))
    for point in points:
        sky[point.x - min_x][point.y - min_y] = 1
    return sky
    
def print_sky(sky):
    for j in range(len(sky[0])):
        for i in range(len(sky)):
            if sky[i][j] == 0:
                print(' ', end='')
            else:
                print('X', end='')
        print()

points = read_data()
too_far_apart = True
count = 0
while True:
    for point in points:
        point.update()
    count += 1
    if count % 10 == 0 or not too_far_apart:
        if get_dist_apart() > 70:
            too_far_apart = False
            sky = create_sky(points)
            print_sky(sky)
            x = input('Press any key to step, press x to exit')
            if x == 'x':
                break
