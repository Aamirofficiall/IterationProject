# Iteration App

This app allows the user to create a new Iteration. Each Iteration has a group of Questions and multiple choice answers. The user is able to give a name to each iteration. After the user finishes the Iteration, all the results will be in the "Interations Overview" button.

This is a project created Django Rest Framework backend and a React frontend.

## How to install
1. In the Comand-line Interface (Termnial) navigate to the folder where you want the clone of the repository.<br>
2. Run "git clone https://github.com/deyi83/IterationProject.git"
3. Run "pip install -r requirements.txt"
4. Run "python manage.py migrate"
5. Run "python manage.py runserver"

## How to install virtual environment (django)
In your Terminal
1. Run "python3 -m pip install --user virtualenv" (for Mac)
2. Run "python3 -m venv env" (for Mac)
3. Run "source env/bin/activate"

## To Run Your App
From your Terminal run the folowing command:
- Run "python manage.py runserver"

## API-END points
- /api/q  --> to see the questions
- /api/i  --> to see te iteratons <br>
Note: There is a maximum of three questions per Iteration.

