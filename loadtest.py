import requests
import random
import string
import threading


def request():
    # randomize the data
    i = 0
    while i < 1000:
        data = {
        "firstName": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100)),
        "lastName": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100)),
        "username": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100)),
        "password": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100)),
        }
        r = requests.post('http://localhost:4000/users/register', data=data)
        print(r.status_code)
        i += 1

if __name__ == '__main__':
    # use threads to make requests
    for i in range(1000):
        t = threading.Thread(target=request)
        t.start()

    # request()
    

