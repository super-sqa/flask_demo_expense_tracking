# Flask Demo Expense Tracking
Just a simple flask app that is used to track expenses. 
Stores each expenses in json files. It creates a directory for the output if the directory does not exist.

## How to run without Docker

```bash
git clone git@github.com:super-sqa/flask_demo_expense_tracking.git
cd flask_demo_expense_tracking
python3 run.py
```


## How to run with Docker
##### First build the image
```bash
git clone git@github.com:super-sqa/flask_demo_expense_tracking.git
cd flask_demo_expense_tracking
docker build -t <image_name_you_want_to_use> .
```

##### Then start the container
```bash
git clone git@github.com:super-sqa/flask_demo_expense_tracking.git
cd flask_demo_expense_tracking
docker run -v </full path>/flask_demo_expense_tracking/app:/my_flask_app/app -p <port on your host>:8889 -d <image name>
```
- "</full path>/flask_demo_expense_tracking/app" is so you can mount your local directory to the directory in the container.
- "\<port on your host>" is the port you want to access the app with

#### To access the app
```bash
localhost:<port on your host>
```

##### Example
```bash
docker build my_expense_app .
docker run -v /Users/admas/project/expense/app:/my_flask_app/app -p 8585:8889 -d my_expense_app
```

##### Home Page Preview
![Alt text](/home_page.jpg?raw=true "Home Page Preview")