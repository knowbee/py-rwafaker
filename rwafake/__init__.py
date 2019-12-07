from .data import person
from .helpers import (randomizr, shuffler)

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
  def fullName(self, n=0):
    try:
      fpart = randomizr(self.person['name']['first_names'])
      lpart = randomizr(self.person['name']['last_names'])
      if(int(n) and int(n) < 101):
        full = []
        for i in range(n):
          fpart = shuffler(self.person['name']['first_names'])[i]
          lpart = shuffler(self.person['name']['last_names'])[i]
          full.append(f"{fpart} {lpart}")
        return full
      return f"{fpart} {lpart}"
    except ValueError:
      return "failed, wrong input"
  def email(self, n=0):
    try:
      emails = ""
      fpart = randomizr(self.person['name']['first_names']).lower()
      pattern = randomizr(self.patterns)
      mpart = randomizr(self.person['name']['last_names']).lower()
      lpart = randomizr(self.person["email"])
      emails += (f"{fpart}{pattern}{mpart}@{lpart}")
      if(int(n) and int(n) < 101):
        emails = []
        for i in range(n):
          fpart = shuffler(self.person['name']['first_names'])[i].lower()
          pattern = randomizr(self.patterns)
          mpart = shuffler(self.person['name']['last_names'])[i].lower()
          lpart = shuffler(self.person["email"])[i].lower()
          email = f"{fpart}{pattern}{mpart}@{lpart}"
          emails.append(email)
        return emails
      return emails
    except ValueError:
      return "failed, wrong input"
rwafaker = Faker()

