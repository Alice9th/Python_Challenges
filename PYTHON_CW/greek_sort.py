""" write a comparator for a list of phonetic words for the 
letters of the greek alphabet.

A comparator is:

a custom comparison function of two arguments (iterable elements) 
which should return a negative, zero or positive number depending 
on whether the first argument is considered smaller than, equal to, 
or larger than the second argument"""


def greek_comparator(lhs, rhs):
  greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
  return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)

print(greek_comparator('gamma', 'chi'))

"""
At the beginning I thought it was about comparing the length of the strings...
Well, it was simplier than that, you have to compare POSITIONS, and that's why 
you use the .index() method 

"""

#Using lambda functions:

greek_comparator = lambda lhs, rhs: greek_alphabet.index(lhs) - greek_alphabet.index(rhs)

