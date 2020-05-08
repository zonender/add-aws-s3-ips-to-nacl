# add-aws-s3-ips-to-nacl
This python/ansible script adds NACL rules to allow access to and from AWS S3 IP ranges

I am running this code from within a virtual env, you need to install pipenv or just use python's built in venv to create a virtual env, this os 


I'm running this code on Centos 7.


After cloning it:

1. from the root project directory run:

```bash
pipenv --python 3.7
```

2. To activate run

```bash
pipenv shell
```

3. Install boto3, botocore and json:

```bash
pipenv install 
```

