#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:13:56 2021

@author: agnish
"""

import numpy as np
import os
from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float
    box_no: int

class Person:
    ideologies = [1, 2, 3]
    nr_of_ideologies = len(ideologies)
    def __init__(self, name: int, pos: Position, rank: int, ideology: int, inbox: list, history):
        self.name = name
        self.pos = pos
        self.rank = rank
        self.ideology = ideology
        self.inbox = inbox
        self.history = history
    """
    A person can receive two types of messages in their inbox
    1) Influence : These nudge the person towards a certain ideology
    2) Death threats : These immediately kill the person i.e. wipes their history and a new person is promoted
                       to the same rank from around the nighbourhood. This entire thing is propagated
                       down through the ranks until we reach the lower ranks where a new person is created.
    A message in the inbox contains 3 attributes:
    1) The ideology of the person sending the message
    2) The type of the message
    3) The weight of the message
    """
    """
    This function consolidates all the messages in the inbox of the person and creates a 2-by-nr_of_ideologies
    matrix "msgs"
    """
    def consolidate_inbox(self):
        L = len(self.inbox)
        msgs = np.zeros((2, self.nr_of_ideologies))
        for i in range(L):
            msg = self.inbox[i]
            msg_ideology = msg[0]
            msg_type = msg[1]
            msg_weight = msg[2]
            msgs[msg_type, msg_ideology] += msg_weight
        return msgs
    
    def update_Person(self, temperature):
        msgs = self.consolidate_inbox()
            

pos = Position(10.0, 11.0, 104)

obj_list = []

for i in range(100):
    obj_list.append(Person(i, pos, i, "A", [1,2,3], np.random.rand(2,3)))



