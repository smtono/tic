"""
Uses distance measure to measure the distance between two vectors
"""

def euclidean_distance(value1, value2):
    """
    Calculates the Euclidean Distance between two values
    """
    return ((value1 - value2) ** 2) ** 0.5

def get_distance(vector1, vector2):
    """
    Calculates the distance between two vectors
    """
    distance = 0
    for i in range(len(vector1)):
        distance += euclidean_distance(vector1[i], vector2[i])
    return distance

if __name__ == '__main__':
    print(euclidean_distance(1, 10))
