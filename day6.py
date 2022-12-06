#!/usr/bin/env python3

from utils import *

inpt = get_input()

PACKET_MARKER_LEN = 4
packet_start = None
for ndx, win in enumerate(windows(inpt, PACKET_MARKER_LEN)):
    if len(win) == len(set(win)):
        packet_start = ndx + PACKET_MARKER_LEN
        break

MESSAGE_MARKER_LEN = 14
message_start = None
for ndx, win in enumerate(windows(inpt, MESSAGE_MARKER_LEN)):
    if len(win) == len(set(win)):
        message_start = ndx + MESSAGE_MARKER_LEN
        break

print(f"part 1: {packet_start}")
print(f"part 2: {message_start}")

if "test" in sys.argv:
    assert packet_start == 7
    assert message_start == 19
