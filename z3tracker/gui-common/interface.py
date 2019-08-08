'''
Program GUI
'''

import json
import os.path

from ..config import CONFIG, CONFIGDIRECTORY
from .. import world

__all__ = 'load_window_cache', 'save_window_cache', 'world_tracker'


def load_window_cache() -> dict:
    '''
    Load window layout info.

    Returns:
        layout: window layout following format {window name: (x, y)}
    '''

    try:
        fid = open(
            os.path.join(CONFIGDIRECTORY, CONFIG['window_layout']), 'r')
    except FileNotFoundError:
        layout = {}
    else:
        try:
            layout = json.load(fid)
        except json.JSONDecodeError:
            layout = {}
        finally:
            fid.close()
    return layout


def save_window_cache(layout: dict) -> None:
    '''
    Save window layout to file.

    Returns:
        layout: window layout following format {window name: (x, y)}
    '''

    with open(
            os.path.join(CONFIGDIRECTORY, CONFIG['window_layout']), 'w') as fid:
        json.dump(layout, fid)


def world_tracker() -> object:
    '''
    Return new world tracker object.

    Returns:
        WorldTracker: new world tracker object
    '''

    return world.Tracker()
