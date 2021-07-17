Install the requirements:


```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

```
After the email id are scrapped they are stored in .csv files.
The .csv file of scrapped emails has not been added as added because of privacy concerns.
Currenly, 3 .csv files are added which are placed in the "core" folder.
the 1st line of .csv file will be "fname,lname,mail"
and below this line will be the details of all users.

In settings.py set the path of all the .csv files so that thet get linked to the project.
Also at line no. 55 and 56 of settings.py add the emailid and password from which the mails are to be sent.

For ex:

fname,lname,mail
abcd,xyz,abcd@gmail.com

```

