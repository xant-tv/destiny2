### COMPATIBILITY
from __future__ import print_function

### IMPORTS
import numpy as np
import pandas as pd
import argparse

### TERMINAL
import colorama as clr
clr.init()

### ENUMERATION
from elements import solar, arc, void, stasis
cfg = {
    'arc': {
        'cfg': arc.CFG, 
        'path': arc.PATH
    }, 
    'solar': {
        'cfg': solar.CFG, 
        'path': solar.PATH
    }, 
    'void': {
        'cfg': void.CFG, 
        'path': void.PATH
    }
}
rooms = ['Green', 'White', 'Yellow', 'Red', 'Cyan', 'Blue', 'Purple']
nodes = [1, 2, 3, 4, 5, 6, 7]
terminals = [str(room) + str(node) for room in rooms for node in nodes]
idx_map = {0:'T1L', 1:'T1R', 2:'T2L', 3:'T2R', 4:'T3L', 5:'T3R'}

### ARGPARSER
parser = argparse.ArgumentParser(description='zero_hour.py element')
parser.add_argument('element', choices=['arc', 'solar', 'void'], metavar='element', help='{arc|solar|void}')
parser.add_argument('-r', dest='replacement', action='store_true')
args = parser.parse_args()

### INITIALISE
# Choose appropriate elemental configuration.
active = cfg[args.element]

# Print vault path.
print('\nVAULT_PATH')
print(clr.Style.BRIGHT + active['path'] + clr.Style.RESET_ALL)

# Create encoding data structure.
df = pd.DataFrame({'TERMINAL': terminals, 'COMBINATION': active['cfg']})
df = df.merge(df['COMBINATION'].str.split(pat='-', expand=True).astype(int), how='inner', left_index=True, right_index=True)
df['TIMES_USED'] = 0

# Store search key.
idx = 0
key = []

# Exit condition.
rct = 0
lim = 3

# Inherit frame.
x = df

# Provide utility until manual exit.
while(rct < lim):

    # Design prompt.
    if not key:
        prompt = '\nNEW_KEY | Enter {0}: '.format(idx_map[idx])
    else:
        prompt = '\nBUILDING_KEY | {0} | Enter {1}: '.format(('-').join(key), idx_map[idx])
        
    # Ask for input.
    val = raw_input(prompt)
    
    # Reset if input is blank - allows user cancel.
    if not val:
        rct += 1
        if rct < lim:
            print(clr.Fore.CYAN + clr.Style.BRIGHT + 'RESETTING' + clr.Style.RESET_ALL)
            key = []
            idx = 0
            x = df.loc[df['TIMES_USED'] == 0]
            continue
        else:
            print(clr.Fore.MAGENTA + clr.Style.BRIGHT + 'EXITING\n' + clr.Style.RESET_ALL)
            continue
        
    # Store value in key.
    key.append(val)
    
    # Try to find the combination.
    x = x.loc[x[idx].astype(str) == key[idx]]
    
    # Incremental.
    idx += 1
    rct = 0
    
    # Check result.
    if x.empty:
        # Reset to a try a new key.
        print(clr.Fore.RED + clr.Style.BRIGHT + 'COMBINATION_NOT_FOUND' + clr.Style.RESET_ALL)
        key = []
        idx = 0
        x = df
        
        # Force user to pause and read.
        while(True):
            pause = raw_input('')
            if not pause:
                break
                
    elif x.shape[0] == 1:
        # Print solution and ready new key.
        print(clr.Fore.GREEN + clr.Style.BRIGHT + 'SOLUTION_FOUND' + clr.Style.RESET_ALL)
        print(x[['TERMINAL', 'COMBINATION', 'TIMES_USED']])
        if not args.replacement:
            df.loc[x.index, 'TIMES_USED'] += 1
        
        # Check if this solution knocked out any rooms.
        if not args.replacement:
            removed_room = None
            for room in rooms:
                if df.loc[(df['TERMINAL'].str.contains(room)) & (df['TIMES_USED'] == 0)].empty:
                    print(clr.Fore.GREEN + clr.Style.BRIGHT + 'ROOM_COMPLETE' + clr.Style.RESET_ALL)
                    removed_room = room
                    rooms.remove(removed_room)
                    break
        
        # Force user to pause and read.
        while(True):
            pause = raw_input('')
            if not args.replacement and pause == 'UNDO':
                df.loc[x.index, 'TIMES_USED'] -= 1
                if removed_room:
                    rooms.append(removed_room)
                break
            if not pause:
                break
        
        key = []
        idx = 0
        x = df.loc[df['TIMES_USED'] == 0]
                
    else:
        # Continue train.
        print(clr.Fore.YELLOW + clr.Style.BRIGHT + 'POSSIBLE_KEYS' + clr.Style.RESET_ALL)
        print(x[['TERMINAL', 'COMBINATION', 'TIMES_USED']])