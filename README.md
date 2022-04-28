# coordinate calculator
This is part of my application to Fetch Rewards.

# How to Run Flask App
Per the assignment requirements, only the service.py file in the frontend folder is necessary. The two ways to download this are either to clone the repository or to just copy and paste code from the file into a local python file. You might need to install dependencies before running server by using pip3 (eg. pip3 install flask). Execute the file in a terminal with the command 'python3 service.py' to start the server.

Now that the server is running you can start making requests.

# Making Requests to Flask App
The server runs on http://localhost:5000

http://localhost:5000/calculate : will calculate coordinate points from json body

http://localhost:5000/example/single :  will provide an example JSON body for a single object request

http://localhost:5000/example/list : will provide an example JSON body for a list of objects request

http://localhost:5000/mock/single : will provide the response for the single object example request

http://localhost:5000/mock/list : will provide the response for the list of objects example request


To test the server you need to make requests. This is easiest done through software like Postman or Insomnia. There are two ways to make a request either as a single or a list - both are post methods. The payload will be placed in the body as raw json, so the request will need the "Content-Type" header set to be set to "application/json". Postman does this automatically if you select raw JSON as the type for the body. To send a single request structure the body as an object with two fields: "dimensions" and "corners". Both of these fields are arrays of arrays of size 2.

ex. single request body: {"dimensions": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}

The response of this will be an array of points.

To send a list of JSON objects add a "Body-Type" header to the request with a value of "list". Then structure the raw json as follows.

ex list request body: {"list":[{"dimensions": [3,3],"corners":[[1,1],[1,3],[3,1],[3,3]]}, {"dimensions": [3,2],"corners":[[1,1],[1,3],[6,1],[6,3]]}]}

The response will be list of stringified arrays of solutions or error messages if the JSON Body is malformed.

# Using the Angular UI to make requests
Makes sure you have python3, Angular 13, and node installed(I use version 14.19.1). Clone the repository then navigate into the frontend directory in the terminal and run npm install. Also run pip3 install on the imports in the service.py file (eg. pip3 install flask). Then run npm start. This will start both the server and client. However, if you would like to run them seperately in seperate terminals just run ng serve for the client and python3 service.py for the server. I figured it's a lot more work to run the whole application - so I uploaded a screenshot of the UI so you can see it without downloading it. It generates valid JSON that you could paste into the body-field of Postman, then displays the response. All requests sent from the UI are sent as a list of JSON objects.


<img width="1433" alt="Screen Shot 2022-04-27 at 9 47 30 PM" src="https://user-images.githubusercontent.com/103947024/165659924-2e7647e7-ca2c-4621-8f8e-37c81b2fb519.png">


# Reflection

This section is just a quick reflection of what went right and what went wrong.

This was my first time using flask and was really impressed by how little code it took to set up a server. That being said Im sure a lot was going on behind the scenes. Also, I enjoyed learning about Docker and Containerization, even though I didnt get the chance to implement it. Angular Developement went well and I am starting to get pretty comfortable with Tailwindcss which, for me, makes frontend developement pretty fun.

I did run into several problems. I intially had trouble with flask because I kept trying to pass in a list of object like [{},{},{}]. I wanted to explore testing frameworks for unit testing in python but I never got around to it. Also on the Angular side I originally wanted to have the service in an external service class but I kept getting errors - so for the sake of time I abandoned that idea. I also probably spent too much time on styling the front end. Finally something that took me by surprise was the application not building properly and not running on production mode correctly. I think it was a problem with the tailwind configuration. This was the reason why I couldnt use Docker. I also didn't save enough time for testing, even though I probably should have done that first.

Overall the assignment was a great learning experience, and it showed me I still have a lot to learn. I would really like the chance to have a 1:1 mentorship with an experienced engineer who could help accelerate my learning journey and teach me the best practices.


