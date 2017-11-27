# myflaskd3

First thing you need to do is create virtual environment.
```sh
virtualenv venv
```
Then run 
```sh
pip3 install -e .
```
Now if you want to run the application type
```sh
myflaskd3_server
```
It's assumed that database contains some graph samples. You can fill it yourself. The model filling you can find in fill_database.py

If your database isn't empty you should see the list of available graphs for presentation at 127.0.0.1/client.
