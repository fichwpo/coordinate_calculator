import json

# some JSON:
x = '[{"dimension": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}]'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:

print(y[0]['corners'])
print(type(y[0]['corners'][0][0]) == int)
