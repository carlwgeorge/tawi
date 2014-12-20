import configparser
import pathlib
import re


def load():
    cwd = pathlib.Path.cwd()
    git_dir = cwd / '.git'
    if not git_dir.is_dir():
        for parent in cwd.parents:
            git_dir = parent / '.git'
            if git_dir.is_dir():
                break
        else:
            raise SystemExit('fatal: Cannot locate .git directory')
    git_config = git_dir / 'config'
    if git_config.is_file():
        config = configparser.ConfigParser()
        config.read(git_config.as_posix())
        url = config['remote "origin"']['url']
        parts = re.split('[@:/]', url)
        repo = parts.pop()
        user = parts.pop()
        github_url = parts.pop()
    else:
        raise SystemExit('fatal: Cannot locate config file in .git directory')
    return {'repo': repo, 'user': user, 'github_url': github_url}
