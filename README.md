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
pipenv install boto3 botocore json requests
```

4. Locate the path of your virtual environment interpreter by running:

```bash
pipenv --py
```

you will need this path, it will replace the value of the variable: ansible_python_interpreter in the hosts file located on the root of the project directory.

4. To run:

```bash
AWS_PROFILE=myawsprofile ansible-playbook -i hosts -e 'region=us-east-1' main.yml
```

