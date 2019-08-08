'''
Default settings
'''

__all__ = 'ITEMS',

ITEMS = (
    ('bow', (0, 0), 2,
     {'Bow and Arrows': 'bow', 'Bow and Silver Arrows': 'bowandsilvers'},
     {'links': {'silverarrows': (2,)}}),
    ('silverarrows', (), 1, {}, {}),
    ('boomerang', (0, 1), 3,
     {'Boomerang': 'blueboomerang', 'Magical Boomerang': 'redboomerang',
      'Boomerangs': 'bothboomerangs'},
     {'links': {'blueboomerang': (1, 3), 'redboomerang': (2, 3)}}),
    ('blueboomerang', (), 1, {}, {}),
    ('redboomerang', (), 1, {}, {}),
    ('hookshot', (0, 2), 1, {'Hookshot': 'hookshot'}, {}),
    ('bombs', (0, 3), 1, {'Bombs': 'bombs'}, {'default': 1}),
    ('mushroompowder', (0, 4), 3,
     {'Mushroom': 'mushroom', 'Magic Powder': 'powder',
      'Mushroom/Magic Powder': 'mushroompowder'},
     {'links': {'mushroom': (1, 3), 'powder': (2, 3)}}),
    ('mushroom', (), 1, {}, {}),
    ('powder', (), 1, {}, {}),
    ('firerod', (1, 0), 1, {'Fire Rod': 'firerod'}, {}),
    ('icerod', (1, 1), 1, {'Ice Rod': 'icerod'}, {}),
    ('bombos', (1, 2), 1, {'Bombos Medallion': 'bombos'}, {}),
    ('ether', (1, 3), 1, {'Ether Medallion': 'ether'}, {}),
    ('quake', (1, 4), 1, {'Quake Medallion': 'quake'}, {}),
    ('lantern', (2, 0), 1, {'Lantern': 'lantern'}, {}),
    ('hammer', (2, 1), 1, {'Magic Hammer': 'hammer'}, {}),
    ('shovelocarina', (2, 2), 3,
     {'Shovel': 'shovel', 'Ocarina': 'ocarina',
      'Shovel/Ocarina': 'shovelocarina'},
     {'links': {'shovel': (1, 3), 'ocarina': (2, 3)}}),
    ('shovel', (), 1, {}, {}),
    ('ocarina', (), 1, {}, {}),
    ('bugnet', (2, 3), 1, {'Bug-Catching Net': 'bugnet'}, {}),
    ('mudora', (2, 4), 1, {'Book of Mudora': 'mudora'}, {}),
    ('bottle', (3, 0), 1, {'Bottle': 'bottle'}, {}),
    ('somaria', (3, 1), 1, {'Cane of Somaria': 'somaria'}, {}),
    ('byrna', (3, 2), 1, {'Cane of Byrna': 'byrna'}, {}),
    ('cape', (3, 3), 1, {'Magic Cape': 'cape'}, {}),
    ('mirror', (3, 4), 1, {'Magic Mirror': 'mirror'}, {}),

    ('sword', (1, 5), 4,
     {"Fighter's Sword": 'sword0', 'Master Sword': 'sword1',
      'Tempered Sword': 'sword2', 'Golden Sword': 'sword3'},
     {'links': {'mastersword': (2, 3, 4), 'mastersword2': (3, 4)}}),
    ('mastersword', (), 1, {}, {}),
    ('mastersword2', (), 1, {}, {}),
    ('shield', (2, 5), 3,
     {"Fighter's Shield": 'shield1', 'Red Shield': 'shield2',
      'Mirror Shield': 'shield3'},
     {'links': {'mirrorshield': (3,)}}),
    ('mirrorshield', (), 1, {}, {}),
    ('armour', (3, 5), 3,
     {'Green Tunic': 'armour1', 'Blue Mail': 'armour2',
      'Red Mail': 'armour3'},
     {'default': 1, 'links': {'bluemail': (2, 3), 'redmail': (3,)}}),
    ('bluemail', (), 1, {}, {}),
    ('redmail', (), 1, {}, {}),

    ('pegasus', (4, 1), 1, {'Pegasus Shoes': 'pegasus'}, {}),
    ('glove', (4, 2), 2,
     {'Power Gloves': 'glove1', "Titan's Mitts": 'glove2'},
     {'links': {'powerglove': (1, 2), 'titansmitts': (2,)}}),
    ('powerglove', (), 1, {}, {}),
    ('titansmitts', (), 1, {}, {}),
    ('flippers', (4, 3), 1, {"Zora's Flippers": 'flippers'}, {}),
    ('pearl', (4, 4), 1, {'Moon Pearl': 'pearl'}, {}),
    ('halfmagic', (4, 5), 1, {'Half-Magic': 'halfmagic'}, {})
)