import os
import pathlib


def get_path(variable):
    try:
        return pathlib.Path(os.environ[variable])
    except KeyError:
        try:
            home = pathlib.Path(os.environ['HOME'])
        except KeyError:
            raise SystemExit('HOME not set')
        defaults = {'XDG_CACHE_HOME': home / '.cache',
                    'XDG_CONFIG_HOME': home / '.config',
                    'XDG_DATA_HOME': home / '.local' / 'share',
                    'XDG_STATE_HOME': home / '.local' / 'state'}
        try:
            return defaults[variable]
        except KeyError:
            raise SystemExit('no default stored for ' + variable)


xdg_cache_home = get_path('XDG_CACHE_HOME')
xdg_config_home = get_path('XDG_CONFIG_HOME')
xdg_data_home = get_path('XDG_DATA_HOME')
xdg_state_home = get_path('XDG_STATE_HOME')


def save_path(base, *resource):
    resource = pathlib.Path(*resource)
    assert not resource.is_absolute()
    path = base / resource
    if not path.is_dir():
        path.mkdir(parents=True)
    return path


def save_cache_path(*resource):
    return save_path(xdg_cache_home, *resource)


def save_config_path(*resource):
    return save_path(xdg_config_home, *resource)


def save_data_path(*resource):
    return save_path(xdg_data_home, *resource)


def save_state_path(*resource):
    return save_path(xdg_state_home, *resource)
