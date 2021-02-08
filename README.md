# Exercise Tracker 💪
Exercise Tracker is a web application made for people with the need to keep track of their daily exercises and their goals.

Users can add the name of the exercise they completed that day, with the duration, distance, or the number of reps/sets they did (for example 'running: 5 miles' or 'pull-ups: 10 reps'). They can also add goals they want to set for each exercise.

## Contributor 
Serin Jeon 

<hr>

## Contents
1. Brief
2. Kanban board
3. ERD
4. Continuos Integration
5. Testing
6. Risk assessment
7. Evaluation
<hr>

## 1. Brief
This project is made with the objective to create a CRUD application with different tools, methodologies and technologies.

To complete this project objective I used: 

- A Trello board.

- MySQL database.

- Python programming.

- Flask framework, Jinja2 for HTML and Bootstrap to create web application's front end.

- Unit testing with Pytest.

- Git and Github for version control.

- Jenkins for CI(Continuous Integration).

- A AWS Cloud server hosted MySQL and Jenkins.

- Risk assessment.



## 2. Kanban board
I used the Trello board to keep track of my project.

<img width="420" alt="trello1" src="https://user-images.githubusercontent.com/64602280/107161418-8dcc8800-6994-11eb-978f-3486f26f63b6.PNG">
<img width="631" alt="trello2" src="https://user-images.githubusercontent.com/64602280/107161420-8f964b80-6994-11eb-9591-39c30021c4a6.PNG">

As you can see in the above images, I created user stories of what users wanted to able to do in the web application. A user story is the end goal of the project expressed from the user's perspective.

I also created acceptance criteria to consider for the software project's requirement to be done. 

The rest of the board is divided into three different parts. To do, Doing and Done.
In this project, as you can see, I have completed the essential tasks to achieve the project goals except for the login and out functionality.

To see the details: https://trello.com/b/qug0WVWj

## 3. ERD
ERD is a type of structural diagram for use in database design. Below is this project's ERD that consists of two tables with a one to many relationships. 
<img width="703" alt="dbdb" src="https://user-images.githubusercontent.com/64602280/107161826-32e86000-6997-11eb-8da6-e87372861d9f.PNG">


The database design consists of two exercise tables and one goals table. The exercise tables consist of an exercise id as the primary key, exercise name, exercise done, and exercise date. Exercise can be anything so in the exercise done section I put 100 string limitation so that users can create data more freely. 
Goals table consist of id, goal name, goal set date, goal finish date, goal success. Users can bring any exercise data and connect with their goal as exercise id is a foreign key in the goals table to connect two data tables.


## 4. Continuos Integration
The general workflow for my project is to start with the Trello board where I designed my project. I have followed my board to write the code on VScode. Tested the code to catch any errors and to fix them. The application will be running on the Jenkins server that I have created on the cloud instance. Each time I push the code to my repo on Github, Jenkins will automatically run the commands that I pre-wrote. If the test is passed, my project will be deployed with Gunicorn.


## 5. Testing
After I finished making the CRUD web application I started to write code for the unit test with Pytest. To check my data is working as I intended, I created 4 different unit tests.
The first test case is to see if the user can access the page without an error and the second to fourth tests are to check that CRUD functionality is working without any errors.

Below is my test coverage which covers 100% of the unit test.

<img width="550" alt="test" src="https://user-images.githubusercontent.com/64602280/107162152-3b419a80-6999-11eb-9e78-f30ee72131f2.PNG">

## 6. Risk assessment

I am sure that there would be a lot of risks in this project as this project focus functioning web application with CRUD database but below is the risk that I can assume. I would like to update the risk assessment as my knowledge of it gets better.

|Description|Assessment|Risk|Impact|Response|  
|---|---|---|---|---|
|Data validation|In this application there is no validation checker|High|High|Implement validator in form input and show the error message to user|
|SQL database security|This project does not have login and logout functionality and anyone can mutate DB.|High|High|Add login and out functionality to DB|
|AWS instance failure|If AWS instance failure, the entire application would not function.|Low|High|Create spare instance|
|Traffic overload|As I only tested 2 worker in Gunicorn server could faile with high traffic. |High|High|Test with Gunicorn with more workers |

## 7. Evaluation
 - Issues that I solved: 
    - AWS Instance<br>
    I was planning to use a Google cloud service instance for this project and I have had a VM instance set up. As soon as I installed MySQL and Jenkins on my instance, the server froze and wouldn't work. After putting some time to figure this out, I noted it was a matter of the size of my instance. I then had to create a new instance with AWS which had a bigger capacity with a better processor. But still, I was not able to download every package that I need for the project as the first instance crashed again. So in the second instance, I pulled the git repository and check everything works after when I sure that everything works fine manually I create another instance only with Jenkins and MySQL and integrate continuous integration in Jenkins with the code that I ran manually with the second instance in AWS.

    - MySQL configure<br>
    I had to configure MySQL differently depending on where I am developing which I never had a problem with before. I did not understand at first but later I was able to fix the MySQL configuration problem by setting different MySQL URI.

- Future improvements
    There are so much more features that I want to add to this project. These are :
    - Visualize exercise progress.
    - Log in and out functionality.
    - Goal tick box if user accomplishes their goals.
    - Visualize when user's goals are achieved to motivate them.
    - Deploy with the domain name 
  
