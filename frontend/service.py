#import statements
from flask import Flask, request, abort, jsonify
import sys
import numpy as np
import json
from numpyencoder import NumpyEncoder
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=['POST'])
def handle_request():
    if request.headers.get("Content-Type") == "application/json":
        #check if the request is a list of inputs or a single input
        if request.headers.get("Body-Type") == "list":
            #get the list of inputs
            json_array = request.get_json()['list']
            #parse the list (the method also calculates the result)
            results = parse_json_array(json_array)
            #return the solution as a key : list dictionary entry
            response = jsonify({"solutions": results})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
            return response
        else:
            input = request.get_json()
            if(validate(input) == 0):
                return calculate(input["dimensions"], input["corners"])
            else:
                abort(400)
    else:
        abort(400)

#makes sure the json body for a single input is correct (a request may contain
#mulitple inputs)
def validate(json_object):
    #the json must have a dimensions array of size 2 and a corners array of size 4
    if "dimensions" in json_object.keys() and len(json_object["dimensions"]) == 2 and "corners" in json_object.keys() and len(json_object["corners"]) == 4:
        #the dimensions must be integers
        for dim in json_object["dimensions"]:
            if type(dim) != int:
                return 1
        #every corner should have two values of type int or float
        for point in json_object["corners"]:
            if len(point) != 2:
                return 2
            X = type(point[0])
            Y = type(point[1])
            if (X != int and X != float) or (Y != int and Y != float):
                return 3
        return 0
    return 4


#if the request contains multiple input then it must be parsed
def parse_json_array(json_array):
    #there should be a result for every input
    results = [''] * len(json_array)
    for i in range(len(json_array)):
        input = json_array[i]
        #validate the input
        code = validate(input)
        if(code == 0):
            results[i] = calculate(input["dimensions"], input["corners"])
        else:
            #error message
            results[i] = '{"Error":"The input JSON is not structured correctly with code: ' + str(code) + '"}'
    return results


def calculate(dimensions, corners):
    #determine bottom_left and top_right corners
    corners.sort()
    bottom_left = corners[0]
    top_right = corners[3]

    #build pixel matrix and convert to json object to return
    pixel_matrix = build_pixel_matrix(dimensions, corners, bottom_left, top_right)
    return json.dumps(pixel_matrix, cls=NumpyEncoder)


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
    #calculate x and y coordinate values
    x_values = calc_values(dimensions[0], 0, bottom_left, top_right)
    y_values = calc_values(dimensions[1], 1, bottom_left, top_right)
    #use np.meshgrid to create x,y coordinate pairs
    x2d, y2d = np.meshgrid(x_values, y_values)
    #concatenate into single vector of coordinate pairs
    pixel_array = np.column_stack((x2d.ravel(), y2d.ravel()))
    #split into a vector of vectors of coordinate pairs and flip for correct orientation
    return np.flipud(np.array_split(pixel_array, dimensions[1]))

json_list = {"list":[{"dimensions": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}, {"dimensions": [3,2],"corners":[[1,1],[1,3],[6,1],[6,3]]}]}
json_single = {"dimensions": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}

@app.route("/mock/list")
def mock_list():
    return jsonify({"solutions":parse_json_array(json_list["list"])})

@app.route("/mock/single")
def mock_single():
    return calculate(json_single["dimensions"], json_single["corners"])


@app.route("/example/list")
def example_list():
    return json_list

@app.route("/example/single")
def example_single():
    return json_single



if __name__ == "__main__":
    app.run()
