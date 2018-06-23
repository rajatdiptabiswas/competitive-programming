#!/usr/bin/env python3

import math


def inside_polygon(x, y, points):
    """
    Return True if a coordinate (x, y) is inside a polygon defined by
    a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].
    """
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def main():
    t = int(input())

    for testcase in range(t):
        valid = []

        points_number = int(input())

        points = []
        min_x = math.inf
        min_y = math.inf
        max_x = -1 * math.inf
        max_y = -1 * math.inf

        for i in range(points_number):
            xy = [int(x) for x in input().split()]

            if xy[0] < min_x:
                min_x = xy[0]
            if xy[0] > max_x:
                max_x = xy[0]
            if xy[1] < min_y:
                min_y = xy[1]
            if xy[1] > max_y:
                max_y = xy[1]

            points.append(xy)

        center = [(min_x + max_x)//2, (min_y + max_y)//2]

        if inside_polygon(center[0], center[1], points):
            valid.append(center)

        


if __name__ == '__main__':
    main()