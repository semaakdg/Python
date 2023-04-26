#When the computer encounters a line that has the word 'return' on it, then it knows that this line is the end of the function.
"""def format_name(f_name, l_name): 
    formated_f_named = f_name.title()
    formated_l_named = l_name.title()
    return f"{formated_f_named} {formated_l_named}"
    print("kmmklwkfmk")
format_stinrg = format_name("seMA nUr", "akDaĞ")
print(format_stinrg)"""
#If I add a line of code after the return keyword, notice what happens when I run this code. It doesn't ever get executed. And this has because the return tells the computer that this is the end of the function and you should now exit the function. You can actually have multiple return keywords within the same function, and you can even have a empty return keyword. So just the return keyword without anything afterwards.

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """What you are writing here is called a 'docstring', and it works as follows: For example, when I write 'days_in_month' in the later parts of the code and open '()' parentheses, it will give me 'year, month' and show what is written here as an explanation. To better understand this, try adding 'days_in_month' under the 'print' function at the bottom and open () parentheses. By doing this, you can understand it better."""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  """EXTRA: 
     You can also use this as a multiline comment."""
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]
 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
