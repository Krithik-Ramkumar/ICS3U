#-----------------------------------------------------------------------------
# Name:        Formal Documentation i.e. docstrings (formalDocumentation_ex4.py)
# Purpose:     Provides an example of how to create docstrings in Python using
#		formal documentation standards.				
#
# Author:      Mr. Seidel
# Created:     22-Aug-2018
# Updated:     24-Nov-2024 (updated to f-strings and quote-style)
#-----------------------------------------------------------------------------

def printEmployee(name, occupation, salary):
  '''
  Prints out the information given about an employee.
	
  Takes in information from the user and then prints out
  a summary of the name, occupation, and salary of the 
  information given.
	
  Parameters
  ----------
  name : str
    The name of the person to be printed
  occupation : str
    The occupation of the person to be printed
  salary : float
    The salary of the person to be printed.

  Returns
  -------
  None
  '''
	
  print(f'Name: {name}')
  print(f'Occupation: {occupation}')
  print(f'Salary: {salary}')

# Program runs starting here.  Above this line, the functions are just defined.
printEmployee(salary=31000, name='January', occupation='Month') # note order
printEmployee(name='February', occupation='Month', salary=28000) # note order
