# JBAppBackend
Backend for JBApp (job board app). This is a Flask server that interfaces with a PostgreSQL db on supabase.

The server is deployed on Azure at https://jbappbackend.azurewebsites.net

There are currently 3 endpoints:
1. POST /jobs -- adds a job to the database
2. GET /jobs -- gets all jobs currently in the database
3. DELETE /jobs -- deletes all jobs currently in the database