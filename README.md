# JBAppBackend
Backend for JBApp (job board app). This is a Flask server that interfaces with a PostgreSQL db on supabase.

The server is deployed on Azure at https://jbappbackend.azurewebsites.net

However, because the server is running as a free instance, it spins down with inactivity. As a result, when a request is made to the API when it has spun down, it takes an extra minute or so to spin up and provide that first response. This is NOT a bug or malfunction. The app is fully functional via the Vercel deployment, and can be used/tested. However, if you would like to avoid the startup time of the backend server and/or just run it locally for whatever reason, you can follow the instructions below to do so.

More info about deployed frontend React app: https://github.com/ihemmige/JBAppFrontend

There are currently 3 endpoints:
1. POST /jobs -- adds a job to the database
2. GET /jobs -- gets all jobs currently in the database
3. DELETE /jobs -- deletes all jobs currently in the database

To run locally:
1. From the root directory navigate into the 'backend' directory. 
2. Create a python3 virtual env (python3 -m venv venv) and activate it (source venv/bin/activate). 
3. Then, install the requirements in the venv (pip install -r requirements.txt).
4. Finally, the server should run with command 'flask run' on localhost:5000.