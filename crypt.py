'''Module for Cryptarithm-Solver'''

#define an empty list
list_one = []

def CheckUnique(num):
  """
  Function to get unique digit numbers
  Args:
    num(int) : number
  Returns:
    bool : True or False
  """
  # Start traversing the numbers 
  repeated = [0,0,0,0,0,0,0,0,0,0] 

  # if a digit occcurs more than 1 time then break       
  while (num): 
      if repeated[num % 10] == 1: 
          break
      repeated[num % 10] = 1
      num = (int)(num / 10)

  # num will be 0 only when above loop doesn't break thus its unique 
  if num == 0:
      return True
  return False 

def UniqueSolutions(l,r):
  """"
  Function to get unique solutions
  Args:
    l(int) : Range (first number)
    r(int) : Range (last number) 
  Returns:
    list: A list of unique solutions
  """

  #define empty lists
  fun_list =[]
  bbq_list = []
  range_list = []

  #get list from range provided    
  range_list = list(range(l, r+1))
  
  #loop through the digits and return a unique list
  for i in range_list:
      number = str(i)
      if CheckUnique(i):
        fun_list.append(i)
      if number[0] == number[1] and number[1] != number[2]:
        bbq_list.append(i)
  return [fun_list,bbq_list]

number_list = UniqueSolutions(100,999)
fun_list = number_list[0]
bbq_list = number_list[1]

#mutiply the unique numbers and return unique solutions
for i in fun_list:
    for j in bbq_list:
        solution = str(i*j)
        if solution not in list_one and len(solution) == 6 and solution[2] == solution[3] \
        and solution[0] not in [solution[1], solution[2], solution[4], solution[5]] \
        and solution[1] not  in [solution[2], solution[4], solution[5]] \
        and solution[2] not in [solution[4], solution[5]] \
        and solution[4] !=solution[5]:
            list_one.append(solution)
            input1 = '    '+str(i)
            input2 = 'X   '+str(j)
            output = ' '+ str(solution)
#print the output            
            print(str(input1))
            print(str(input2))
            print(str('-----------'))
            print(str(output))
            print(' ')
count = len(list_one)
print('Total unique solutions', count)
