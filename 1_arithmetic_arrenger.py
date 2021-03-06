def arithmetic_arranger(problems,option=False):
  first_Answer = ""
  operators = ""
  dashlines = ""
  second_Answer = ""
  sumup = ""
  arranged_problems = ""
  sumo = ""

  if(len(problems) > 5):
    #First rule: Checking the amount of problems
    return "Error: Too many problems."

  for problem in problems:
    #Making a list from the strings
    first_Number = problem.split(" ")[0]
    operators = problem.split(" ")[1]
    second_Number = problem.split(" ")[2]

    #Second rule: max 4 digits
    if (len(first_Number) > 4 or len(second_Number) > 4):
      return "Error: Numbers cannot be more than four digits."

    #Third rule: Must have only digits
    if not first_Number.isnumeric() or not second_Number.isnumeric():
      return "Error: Numbers must only contain digits."

    #Forth Rule: correct form of operators
    
    if operators not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    else: 
      if operators == "+": 
        sumo = str(int(first_Number) + int(second_Number))
      if operators == "-":
        sumo = str(int(first_Number) - int(second_Number))
      

    length = max(len(first_Number) , len(second_Number)) + 2
    fisrtline = str(first_Number).rjust(length)
    secondline = operators + str(second_Number.rjust(length - 1))
    sltn = str(sumo.rjust(length))
    
   
    dashline = ""
    for dash in range(length):
      dashline += "-"

    if problem != problems[-1]: 
      first_Answer += fisrtline + '    '
      second_Answer += secondline + '    '
      dashlines += dashline + '    '
      sumup += sltn + '    '
    else: 
      first_Answer += fisrtline
      second_Answer += secondline 
      dashlines += dashline 
      sumup += sltn  

  #Making a choice whether shows the answer or not
  if option: 
    arranged_problems = first_Answer + "\n" + second_Answer + "\n" + dashlines + "\n" + sumup
  else:
    arranged_problems = first_Answer + "\n" + second_Answer + "\n" + dashlines    
  return arranged_problems
