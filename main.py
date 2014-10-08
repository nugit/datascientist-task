#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import io

# Sample function to read a csv file. 
# Feel free to modify
def load_csv(infile):
  with open(infile, 'rU') as f:
    return [row for row in csv.reader(f)]

def sectionA():
  pass

def sectionB():
  pass

def sectionC():
  pass

if __name__ == '__main__':
  # To run: python main.py
  print load_csv('data/SEM_SEO-sampledata1.csv')