### IMPORTS
import numpy as np
import pandas as pd
import argparse

### TERMINAL
import colorama as clr
clr.init()

### ENUMERATION
slr_cfg = [
    '8-5-4-10-4-5', 
    '9-10-10-3-8-3', 
    '7-8-3-4-9-12', 
    '1-2-6-10-12-11', 
    '12-10-6-5-1-1', 
    '1-7-9-5-10-6', 
    '6-7-4-1-1-11', 
    '8-10-7-9-4-8', 
    '9-11-7-2-8-9', 
    '7-8-1-9-6-5', 
    '11-2-8-2-9-2', 
    '4-6-9-2-10-8', 
    '1-7-2-8-5-6', 
    '3-5-2-4-9-12', 
    '9-7-3-5-2-8', 
    '1-10-5-2-2-4',
    '10-3-8-4-9-12', 
    '12-7-11-7-1-12', 
    '5-11-7-2-7-6', 
    '1-11-6-4-6-10', 
    '11-9-11-4-9-3', 
    '7-11-1-9-7-9', 
    '4-8-2-6-5-5', 
    '11-11-8-7-1-12',
    '7-12-6-5-2-2', 
    '8-11-4-12-10-10', 
    '12-1-3-10-12-10', 
    '7-4-3-7-3-8', 
    '10-5-6-12-3-12', 
    '10-6-5-2-5-7', 
    '9-6-1-6-9-8',
    '1-3-7-7-4-12', 
    '10-10-2-6-12-8', 
    '5-11-3-12-1-8', 
    '9-4-10-9-7-2', 
    '9-10-11-11-8-7', 
    '9-11-3-10-9-5', 
    '8-7-4-8-8-10', 
    '2-11-1-6-6-10', 
    '8-12-11-7-3-1', 
    '2-11-12-8-9-1', 
    '11-4-4-6-12-5', 
    '6-11-12-8-5-11', 
    '2-6-8-9-6-8', 
    '9-10-3-3-11-6', 
    '5-10-10-1-4-8',
    '2-10-7-1-1-7', 
    '5-6-1-7-8-9', 
    '6-8-10-7-11-9'
]
slr_pth = ('\n  ').join(['  '+'^    ','#    ','# ###','### #','    #',' ####',' #   ',' ^   '])
arc_cfg = [
    '10-11-3-2-8-7',
    '2-9-4-3-2-11',
    '2-4-12-10-8-6',
    '12-12-1-6-4-1',
    '10-12-8-4-12-4',
    '4-12-2-7-2-10',
    '8-9-9-12-11-1',
    '6-3-10-3-7-3',
    '11-1-2-10-7-1',
    '10-12-9-6-5-7',
    '4-5-9-7-1-6',
    '4-8-8-7-4-8',
    '11-11-9-11-3-6',
    '8-12-6-4-12-6',
    '4-12-5-6-4-4',
    '9-10-11-4-7-11',
    '9-1-12-4-11-4',
    '3-8-1-8-3-7',
    '7-9-5-12-10-4',
    '10-11-9-3-4-9',
    '1-6-11-3-5-1',
    '5-9-1-1-5-11',
    '8-1-11-2-7-4',
    '10-8-11-6-4-2',
    '5-9-6-8-2-2',
    '5-4-5-2-8-5',
    '1-4-5-7-6-7',
    '5-8-3-2-2-11',
    '4-4-10-3-4-1',
    '3-5-7-6-4-12',
    '7-3-2-9-9-5',
    '8-11-7-9-9-5',
    '4-9-1-1-11-5',
    '12-5-11-4-5-1',
    '5-4-11-8-9-8',
    '6-5-2-12-7-3',
    '12-8-1-8-8-3',
    '6-2-12-5-9-3',
    '9-11-12-6-3-7',
    '4-7-3-5-5-1',
    '10-9-3-7-7-12',
    '9-11-1-3-7-11',
    '9-12-7-6-4-9',
    '4-6-6-12-9-8',
    '12-7-1-8-5-7',
    '9-6-5-3-8-7',
    '6-2-1-7-7-5',
    '2-9-5-9-1-8',
    '8-3-4-9-5-9'
]
arc_pth = ('\n  ').join(['  '+'^    ','#    ','# ###','# # #','# # #','### #','    #','    ^'])
voi_cfg = [
    '4-3-2-4-2-9',
    '2-4-1-6-3-10',
    '9-3-12-7-12-12',
    '10-3-2-3-7-11',
    '7-4-2-7-7-9',
    '10-12-11-5-8-12',
    '3-3-1-3-6-8',
    '1-1-2-12-8-10',
    '10-2-3-8-9-3',
    '8-6-2-9-2-10',
    '12-5-7-1-5-7',
    '4-8-12-8-9-3',
    '7-2-8-3-3-12',
    '6-9-12-10-8-5',
    '4-9-9-4-5-5',
    '2-5-11-2-3-5',
    '1-7-12-3-8-4',
    '7-9-6-5-5-12',
    '8-6-9-2-12-12',
    '2-7-2-11-9-10',
    '11-4-4-11-12-3',
    '1-2-1-4-11-4',
    '1-1-4-5-6-5',
    '8-10-5-6-11-11',
    '11-4-5-4-7-6',
    '5-6-7-3-7-10',
    '1-10-7-11-3-12',
    '11-6-12-8-11-11',
    '2-6-5-4-10-3',
    '8-4-5-8-9-4',
    '1-12-1-1-5-4',
    '6-11-11-4-12-4',
    '12-2-11-4-10-2',
    '8-12-5-9-9-4',
    '8-5-11-8-11-11',
    '12-5-12-11-4-4',
    '10-5-11-2-3-1',
    '11-11-7-3-8-11',
    '4-6-5-6-5-12',
    '7-12-1-2-5-4',
    '11-1-5-7-10-2',
    '11-4-2-8-4-8',
    '6-5-6-10-1-1',
    '9-9-8-10-8-6',
    '11-7-6-3-12-5',
    '9-7-7-8-12-7',
    '2-9-12-3-10-2',
    '4-3-2-11-4-7',
    '5-9-11-7-12-10'
]
voi_pth = ('\n  ').join(['  '+'   ^ ','   # ','   ##','### #','# ###','##   ',' #   ',' ^   '])
cfg = {'arc': {'cfg': arc_cfg, 'path': arc_pth}, 'solar': {'cfg': slr_cfg, 'path': slr_pth}, 'void': {'cfg': voi_cfg, 'path': voi_pth}}
rooms = ['Green', 'White', 'Yellow', 'Red', 'Cyan', 'Blue', 'Purple']
nodes = [1, 2, 3, 4, 5, 6, 7]
terminals = [str(room) + str(node) for room in rooms for node in nodes]
idx_map = {0:'T1L', 1:'T1R', 2:'T2L', 3:'T2R', 4:'T3L', 5:'T3R'}

### ARGPARSER
parser = argparse.ArgumentParser(description='zero_hour.py element')
parser.add_argument('element', choices=['arc', 'solar', 'void'], metavar='element', help='{arc|solar|void}')
args = parser.parse_args()

### INITIALISE
# Choose appropriate elemental configuration.
active = cfg[args.element]

# Print vault path.
print '\nVAULT_PATH'
print clr.Style.BRIGHT + active['path'] + clr.Style.RESET_ALL

# Create encoding data structure.
df = pd.DataFrame({'TERMINAL': terminals, 'COMBINATION': active['cfg']})
df = df.merge(df['COMBINATION'].str.split(pat='-', expand=True).astype(int), how='inner', left_index=True, right_index=True)

# Store search key.
idx = 0
key = []

# Exit condition.
rct = 0
lim = 3

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
            print clr.Fore.CYAN + 'RESETTING' + clr.Style.RESET_ALL
            idx = 0
            key = []
            continue
        else:
            print clr.Fore.MAGENTA + 'EXITING\n' + clr.Style.RESET_ALL
            continue
        
    # Store value in key.
    idx += 1
    key.append(val)
    rct = 0
    
    # Try to find the combination.
    x = df.loc[df['COMBINATION'].str.contains('^' + ('-').join(key)), ['TERMINAL', 'COMBINATION']]
    
    # Check result.
    if x.empty:
        # Reset to a try a new key.
        print clr.Fore.RED + 'COMBINATION_NOT_FOUND' + clr.Style.RESET_ALL
        idx = 0
        key = []
    elif x.shape[0] == 1:
        # Print solution and ready new key.
        print clr.Fore.GREEN + 'SOLUTION_FOUND' + clr.Style.RESET_ALL
        print x
        idx = 0
        key = []
    else:
        # Continue train.
        print clr.Fore.YELLOW + 'POSSIBLE_KEYS' + clr.Style.RESET_ALL
        print x
