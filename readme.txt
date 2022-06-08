The purpose of this application is to use API and run a refresh programmatically.
In my use case, I made an executable out of the application and placed it in the server. It removes dependency on installing Python in the server.
I also included a cmd to show how you can run it.

The account.txt will include the ids and tokens in a separate file.

This application is written using Tableau Server Client (TSC) which is a Python library. 
Python API reference can be found here:
https://tableau.github.io/server-client-python/docs/api-ref

You will need to have Python installed.
Using pip (or any other installer), you will need to install TSC package:
pip install tableauserverclient

Then you can import and use it. 