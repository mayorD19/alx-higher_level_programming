#!/usr/bin/python3
def uniq_add(my_list=[]):
  new_nos = []
  unique_numbers = set(my_list)
  for x in unique_numbers:
    new_nos.append(x)
  return sum(new_nos)
