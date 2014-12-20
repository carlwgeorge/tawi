import getpass
import requests
from . import configuration
from . import xdg


class Token():
    def __init__(self, note, github_url, user):
        self.note = note
        self.api = '.'.join(['https://api', github_url])
        self.user = user
        state_path = xdg.save_state_path('github-api-v3', github_url)
        self.token_file = state_path / ('token_' + self.note)
        if self.token_file.exists():
            with self.token_file.open('r') as f:
                    self.token = f.read()
                    self.validate()
        else:
            self.token = self.create()
            with self.token_file.open('w') as f:
                    f.write(self.token)

    def create(self):
        password = getpass.getpass(prompt='password: ')
        endpoint = '/'.join([self.api, 'authorizations'])
        payload = {'scopes': ['repo'], 'note': self.note}
        response = requests.post(endpoint,
                                 json=payload,
                                 auth=(self.user, password))
        if response.ok:
            return response.json().get('token')
        else:
            print(response.json().get('message'))
            print(response.json().get('errors'))
            raise SystemExit(1)

    def validate(self):
        auth = {'Authorization': 'token ' + self.token}
        response = requests.get(self.api, headers=auth)
        if not response.ok:
            raise SystemExit('invalid token')


def entry_point():
    config = configuration.load()
    user = config.get('user')
    github_url = config.get('github_url')
    token = Token('tawi', github_url, user)
    print(token.token)
