'''
Item display
'''

import configparser
import os.path

from ..config import CONFIG, CONFIGDIRECTORY
from ..version import __version__ as version

__all__ = 'NoConfig', 'load_items', 'load_dungeons', 'new_item', 'new_dungeons'


class NoConfig(Exception):
    '''
    Raised when item layout config is not available.
    '''

    pass


def load_items() -> dict:
    '''
    Load item layout.

    Returns:
        dict: layout in format {identifier: (column, row)}
    '''

    return _load('Items')


def load_dungeons() -> dict:
    '''
    Load dungeon layout.

    Returns:
        dict: layout in format {identifier: (column, row)}
    '''

    return _load('Dungeons')


def _load(ltype: str) -> dict:
    '''
    Load item/dungeon layout.

    Args:
        ltype: 'Items' or 'Dungeons'
    Returns:
        dict: layout in format {identifier: (column, row)}
    Raise:
        NoConfig, configparser.Error: if no item layout is available
    '''
    
    inp = configparser.ConfigParser(allow_no_value=True)
    try:
        fid = open(os.path.join(CONFIGDIRECTORY, CONFIG['button_layout']), 'r')
    except FileNotFoundError as err:
        raise NoConfig() from err
    try:
        inp.read_file(fid)
    finally:
        fid.close()
    if ltype not in inp:
        raise NoConfig()
    try:
        if inp['version']['version'] != version:
            raise NoConfig()
    except (KeyError, configparser.NoSectionError,
            configparser.NoOptionError) as err:
        raise NoConfig() from err

    layout = {}
    for item in inp[ltype]:
        if not inp[ltype][item]:
            continue
        try:
            sep = tuple(int(c) for c in inp[ltype][item].split(','))
        except ValueError as err:
            raise NoConfig() from err
        if len(sep) != 2:
            raise NoConfig()
        layout[item] = sep

    return layout


def new_item(layout: dict) -> None:
    '''
    Store given item icon layout.

    Args:
        layout: layout in format {identifier: (column, row)}
    '''

    _new(layout, 'Items')


def new_dungeon(layout: dict) -> None:
    '''
    Store given dungeon icon layout.

    Args:
        layout: layout in format {identifier: (column, row)}
    '''

    _new(layout, 'Dungeons')


def _new(layout: dict, ltype: str) -> None:
    '''
    Store given icon layout.

    Args:
        layout: layout in format {identifier: (column, row)}
        ltype: 'Items' or 'Dungeons'
    '''

    assert ltype in ('Items', 'Dungeons')
    if ltype == 'Items':
        other = 'Dungeons'
    else:
        other = 'Items'
    try:
        existing = _load(other)
    except (NoConfig, configparser.Error):
        existing = {}

    out = configparser.ConfigParser(allow_no_value=True)
    out.add_section(ltype)
    for item in layout:
        out[ltype][item] = ', '.join(str(c) for c in layout[item])
    out.add_section(other)
    for item in existing:
        out[other][item] = ', '.join(str(c) for c in existing[item])
    out.add_section('version')
    out['version']['version'] = version

    with open(os.path.join(
            CONFIGDIRECTORY, CONFIG['button_layout']), 'w') as fid:
        out.write(fid)
