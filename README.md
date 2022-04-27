# coordinate_calculator
This is part of my application to Fetch Rewards.

# How to Run Flask App
Per the assignment requirements only the service.py file in the frontend folder is necessary. The two ways to download this are either to clone the repository or to just copy and paste code from the file into a local python file. You might need to install dependencies before running server by using pip3 (eg. pip3 install flask). Execute the file in a terminal with the command 'python3 service.py' to start the server.

Now that the server is running you can start making requests.

# Making Requests to Flask App
The server runs on http://localhost:5000

http://localhost:5000/calculate : will calculate coordinate points from json body
http://localhost:5000/example/single :  will provide an example JSON body for a single object request
http://localhost:5000/example/list : will provide an example JSON body for a list of objects request
http://localhost:5000/mock/single : will provide the response for the single object example request
http://localhost:5000/mock/list : will provide the response for the list of objects example request


To test the server you need to make requests. This is easiest done through software like Postman or Insomnia. Tere are two ways to make a request either as a single or a list - both are post methods. The payload will be placed in the body as raw json, so the request will need the "Content-Type" header set to be set to "application/json". Postman does this automatically if you select raw JSON as the type for the body. To send a single request structure the body as an object with two fields: "dimensions" and "corners". Both of these fields are arrays of arrays of size 2.

ex. single request body: {"dimensions": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}

The response of this will be an array of points.

To send a list of JSON objects add a "Body-Type" header to the request with a value of "list". Then structure the raw json as follows.

ex list request body: {"list":[{"dimensions": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}, {"dimensions": [3,2],"corners":[[1,1],[1,3],[6,1],[6,3]]}]}

The response will be list of stringified arrays of solutions or error messages if the JSON Body is malformed.


