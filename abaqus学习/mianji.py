from shapely.geometry import Polygon

# file = open("coordinates_springback.txt", "r")
# for txt in file.readline():
#     print(txt)


coords  = [(-1, 0), (-1, 1), (0, 0.5), (1, 1), (1, 0), (-1, 0)]



def polygon_area(points):
    """返回多边形面积

    """
    area = 0
    q = points[-1]
    for p in points:
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return abs(area / 2)


# polygon = Polygon(coords)
mianji = polygon_area(coords)
print(mianji)
# print(polygon.area)