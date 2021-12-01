import numpy as np
from numpy import array, sqrt, square
from PIL import Image

C = "./c1.mp3"
D = "./d1.mp3"
E = "./e1.mp3"
F = "./f1.mp3"
G = "./g1.mp3"

def file_to_array(filename):
    """
    Reads a sound file and converts it to an array.
    """
    f = open(filename, 'rb')
    data = f.read()
    f.close()
    return [x for x in data]

def triple_entries(arr):
    """
    Converts every element  in the array to 
    a tuple of that element tripled.
    """
    #return np.array([((x, x, x)) for x in arr])
    
    """
        Convert the array to a set of arrays
        of size 3 selecting every third element
    """
    return np.array([(arr[i], arr[i+1], arr[i+2]) for i in range(0, len(arr)-3, 3)])

def nearest_square(x):
    """
        Takes in a number and returns
        The largest perfect square < x
    """
    if sqrt(x) % 1 == 0:
        return x
    else:
        return nearest_square(x - 1)

def square_array(arr):
    """
    Makes the array the largest
    possible NxN matrix
    """

    largest_square = sqrt(nearest_square(arr.shape[0]))
    arr = arr[0:int(pow(largest_square,2))]
    return np.reshape(arr, (int(largest_square), int(largest_square), arr.shape[1]))

def average_colors(arr):
    """
        For every tuple in the array,
        average the colors of the three
        elements and return the average
    """
    return np.array([(
        (arr[i][0] + arr[i][1] + arr[i][2]) / 3
    ) for i in range(arr.shape[0] - 3)])

def array_to_image(arr):
    """
    Converts an array to an image
    """
    img = Image.fromarray(arr, 'RGB')
    return img.resize((1024, 1024))

def file_to_image(filename):
    """
    Converts a sound file to an image
    """
    avg = array_to_image(
            square_array( 
                triple_entries(
                    average_colors(
                        triple_entries(
                            file_to_array(
                                filename
                            )
                        )
                    )
                )
            )
        )

    orig = array_to_image(
        square_array(
            triple_entries(
                file_to_array(
                    filename
                )
            )
        )
    )

    o = np.array(orig)
    a = np.array(avg)

    new = o + a
    new = new // 2
    new = Image.fromarray(new)

    return (orig, avg, new)
    