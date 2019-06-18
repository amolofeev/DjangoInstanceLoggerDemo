**DjangoInstanceLogger demo project**

```bash
$ virtualenv -p python3 .env
$ pip install -r requirements.txt
$ ./manage.py runserver
```

or 

```bash
$ docker build -t dj_demo .
$ docker run --network host dj_demo
```


Open browser and visit [http://localhost:8000/admin/admin_auth/user/1/change/#logs](http://localhost:8000/admin/admin_auth/user/1/change/#logs)
```text
user: admin
password: admin
```
