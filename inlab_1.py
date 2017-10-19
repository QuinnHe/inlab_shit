#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:05:23 2017

@author: ZIYU
"""

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)