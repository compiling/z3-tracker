'''
Dungeon display
'''

from .items import NoConfig, load_dungeons, new_dungeon

__all__ = 'NoConfig', 'load_dungeons', 'new_dungeon', 'REWARDS'


REWARDS = {
    'unknown': 'reward-unknown',
    'courage': 'reward-courage',
    'powerwisdom': 'reward-powerwisdom',
    'crystal': 'reward-crystal',
    '56crystal': 'reward-56crystal'
}
