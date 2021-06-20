import math
from contextlib import contextmanager

class Logistics():
  def __init__(self, k = 1):
    self._k = k

  def value(self, z):
    return 1 / (1 + math.exp(-self._k * z))

  def deriv(self, z):
    return self._k * self.value(z)(1 - self.value(z))

  def __call__(self, z):
    return  self.value(z)

  @contextmanager
  def withZ(self, k):
    try:
      self._k = k
      yield
    finally:
      self._k = 1
    
logistic = Logistics(1)

print(logistic(1))

with logistic.withZ(3):
  print(logistic(1))

print(logistic(1))