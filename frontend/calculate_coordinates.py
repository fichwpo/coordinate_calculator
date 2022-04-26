#import statements
from flask import Flask
import sys
import numpy as np
import json
from numpyencoder import NumpyEncoder
app = Flask(__name__)
@app.route("/calculate/<string:args>")
def calculate(args):
    #get data from argv
    args = args.split('-')

    for i in range(len(args)):
        if i <= 1:
            args[i] = int(args[i])
        else:
            args[i] = float(args[i])

    w = args[0]
    h = args[1]

    p1 = (args[2], args[3])
    p2 = (args[4], args[5])
    p3 = (args[6], args[7])
    p4 = (args[8], args[9])

    dimensions = (w, h)
    corners = [p1,p2,p3,p4]


    #'3 3 1 1 1 3 3 1 3 3'
    ##'3-3-1-1-1-3-3-1-3-3'
    #verify arguments

    #retrieve the top left and bottom right corners that determine the rectangle on the coordinate plane
    corners.sort()
    bottom_left = corners[0]
    top_right = corners[3]


    #calculate values
    def calc_values(pixels, axis, bottom_left, top_right):
        if pixels == 1:
            #return the middle of two coordinates
            return [(top_right[axis] - bottom_left[axis]) / 2]
        elif pixels == 2:
            #return both coordinates
            return [bottom_left[axis], top_right[axis]]
        else:
            #determine length of image along axis
            length = top_right[axis] - bottom_left[axis] + 1
            #determine the space in between pixels along axis
            space = length / pixels
            #add correctly spaced values to the list and return them
            position = float(bottom_left[axis])
            values = [position]
            for i in range(pixels - 2):
                values.append(values[-1] + space)
            values.append(float(top_right[axis]))
            return values

    def build_pixel_matrix(dimensions, corners, bottom_left, top_right):
        #calculate x coordinates
        x_values = calc_values(dimensions[0], 0, bottom_left, top_right)
        y_values = calc_values(dimensions[1], 1, bottom_left, top_right)
        x2d, y2d = np.meshgrid(y_values, x_values)
        pixel_array = np.column_stack((y2d.ravel(), x2d.ravel()))
        return np.array_split(pixel_array, dimensions[0])

    #return answer
    object = build_pixel_matrix(dimensions, corners, bottom_left, top_right)
    return json.dumps(object, cls=NumpyEncoder)

if __name__ == "__main__":
    app.run()
#print(calculate('3-3-1-1-1-3-3-1-3-3'))
