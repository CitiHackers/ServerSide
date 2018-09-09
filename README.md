# Server Side (Backend)
Backend code for citi hackerthon 

# Setup MySQL
1. Install & start mysql local server (assumed on port 3306)
2. Log in mysql local server and create new database called `CITI` by running command: CREATE DATABASE CITI
3. Run SQL script provided under CITI database

# How to run:
1. Download python3.6 at `https://www.python.org/downloads/`
2. Go to the directory of this repo using command `cd backend` in terminal(Mac) /cmd(Windows)
3. Create a virtual environment for this:
    1) type `python3 -m venv venv` to create a python3 virtual environment called `venv`
    2) activate this `venv` using `source venv/bin/activate` for Unix or MacOs or
                                  `venv\Scripts\activate.bat` for Windows
    3) Now you should see `(venv)` before your username. 
    4) Type `pip install flask` and `pip install requests` so that install all requirements
4. run `python run.py` to run server see whether there will be `Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
` appears in cmd or Terminal
5. To run it daemonly, using `nohup python run.py &` command instead
