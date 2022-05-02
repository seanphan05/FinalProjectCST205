cd %CD% & :: Changing the directory to the current directory
set FLASK_APP=mainpage.py & :: Specifying the app we are going to run $env:FLASK_APP = "mainpage.py"
set FLASK_DEBUG=1 & :: Putting flask in to debug mode $env:FLASK_DEBUG = 1
flask run 