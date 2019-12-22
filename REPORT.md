# PYTHON PROJECT REPORT

### WHAT IS OUR PROJECT ? IT’S GOAL & FEATURES
The goal of the project was to use many different aspects of Python programing that we did not know into one single project. <br>
The project’s main task was to demonstrate the extent to which a Python script could interact with a Spotify account using Web API. 
We used a quiz as a proof of concept and to add features around this app. <br>
The goal was not to have as many questions as possible because the code would have been mostly the same after the few questions 
we included.
 
### THE CHOICES WE HAD TO MAKE
_Personal API vs Public API?_
- When we were still thinking of what we could do with Spotify’s API we had to choose between 
going with a project using personal listening data or public data. Both had advantages. <br>
Using public data added the possibility of using “big” data or at least bigger amounts of data. But we decided to go with personal data. 
This choice was motivated by the fact that this makes our app unique with every user. <br>

_Keeping code that is not 100% reliable or not?_
- For example, initially, the music playback feature was not the most reliable. In order to work it depended on many conditions to be met. 
Some of which seemed to be random. Hence, after hesitatation we included a different way to insert this feature. <br>

_Console vs Flask?_
- We describe this decision in more detail in the section about the contribution of each member. But in a few words, 
we used a console app to build our quiz and add our features. It was only once we were satisfied with our app that we decided 
to put it in the form of a Flask web app. <br>

### WHAT WE TRIED BUT FAILED AT ?
We thought of posting our app on a web server (web hosting), but due to time constraints we decided to go against this idea. 
 
### OUR RESULTS
Functional code, with some exception handling to avoid frequent crashes
 
### THE CONTRIBUTION OF EACH MEMBER / HOW WE BUILD OUR PROJECT
We kept a team of two as it seemed more manageable to split the workload. <br>
Our coding background: <br> <br>
_Rodolphe:_ <br>
I already did a Python course and a computer programming class to implement algorithms such as gradient descent or simulated annealing. 
During a machine learning course and through internships I improved my “Python for data science” skills. Hence I consider myself 
proficient with Python. But of course this is only a part of what can be done with this programming language. This is part of the 
reason our project uses skills such as Flask and dealing with API. Something that I had never done before. At the end of this project 
I can say that I have discovered and developed new Python skills. <br> <br>

_Armand:_  <br>
I did not have a lot of experience in programming: <br>
I had several projects in R, but there were focused on Statistics. This project really helped me in my quest to learn how to 
master Python. <br>
It was quite challenging at first, but I now feel more confident when using Pandas, using APIs, ... <br>
Moreover, by working on the browser with Flask, I learned a bit of HTML and CSS (and very little JS). I therefore had a great time 
working on this project.    
         <br>

<br>
The project was conducted in an iterative way. We wanted to build our code step by step and not making the mistake of trying to 
build a too hard feature from the start and being left with nothing. <br> <br>
We started with a general idea: that it would be interesting to have a Python code interacting with the internet. It is a way to 
demonstrate that a Python script does not only interact with your own computer but also with the outside world (the internet and in 
our case your Spotify account). <br> <br>
The first step was making sure our project was feasible (with the skills we had and the time constraint). Rodolphe build a small 
script with an authorization flow that connected to his Spotify account and could retrieve various information thanks to the API.
Once this was working, we could move forward with all the features we had in mind. <br> <br>
Since the very beginning we wanted to have a web browser interface. But at first, we decided to go with a console interface. 
By doing this we focused on adding features instead of making our web app look fancy. As you will see it is only at the very last 
step that Armand implemented our code in a Flask web app. <br><br>
The authorization flow was done by Rodolphe as he had already worked on it in the first step. Armand focused on building the 
database that we would need to run our quiz. Once we had those two elements, we could actually start building the quiz. We came 
up with various candidate questions we could include, and both coded an equal amount each on our side before putting everything 
together. <br> <br>
At this point we had a functioning app that could run in the console. This is when we started adding other features. <br>
Armand focused on putting this code inside a Flask web app and Rodolphe added some features to the app. In order to not be a 
“read only” app, Rodolphe added a feature that can create a playlist of the top 50 played tracks on the user’s account. 
An option to export some data as a CSV was added along with a feature that plays 10 seconds of the correct answer track / artist 
after each question. To take the explanation from the beginning of this section, these features are here to make the code more 
“connected” to the outside world. <br> 
 
### SOME PYTHON SKILLS THAT WE USED:
- Pandas dataframe handling, with joins
- String matching to avoid having a mistake because of a capitalized letter
- JSON handling:The results of the API calls from Spotify were returned as JSON. We iterated through them to retrieve only the needed data and put it as a pandas dataframe.
- Exception Handling: some parts are the code are very dependent on the user setup, this is the case for the music playback functionality. Hence, because it is not a necessary feature for the code to run, we added an exception that simply does not run the function if it would crash.
