from data import person
from helpers import (randomizr, shuffler)

class Faker:
  def __init__(self):
    self.person = person
    self.patterns = [".", "_"]
    self.n = None
  def firstName(self, n=0):
    try:
      if(int(n) and int(n) < 101):
        return shuffler(self.person["name"]["first_names"])[0:n]
      return randomizr(self.person["name"]["first_names"])
    except ValueError:
      return "failed, wrong input"
  def lastName(self, n=0):
    try:
      if(int(n) and int(n) < 101):
        return shuffler(self.person["name"]["last_names"])[0:n]
      return randomizr(self.person["name"]["last_names"])
    except ValueError:
      return "failed, wrong input"

rwafaker = Faker()

