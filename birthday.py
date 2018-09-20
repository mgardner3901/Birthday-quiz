"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day


a = input("Hello, what is your name? ")
c = str("Hi " + a + ", what was the name of the month you were born in? ") 
b = input(c)
d = int(input("And what year were you born in, " + a + "? "))
e = int(input("And the day? "))


months = ["" , "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ""]
month = months[todaymonth]


if b=="October" and e==31:
    print("You were born on Halloween!")
    
    
elif b==month and e==todaydate:
    print("Happy birthday!")
    
    
elif b in ["December", "January", "February"] and d>=2000:
    print(str(a + ", you are a winter baby of the two thousands."))
elif b in ["March", "April", "May"] and d>=2000: 
    print(str(a + ", you are a spring baby of the two thousands."))
elif b in ["June", "July", "August"] and d>=2000:
    print(str(a +", you are a summer baby of the two thousands."))
elif b in ["September", "October", "November"]  and d>=2000:
    print(str(a + ", you are a fall baby of the two thousands."))
    
    
elif b in ["December", "January", "February"] and d>=1990 and d<= 2000:
    print(str(a + ", you are a winter baby of the nineties."))
elif b in ["March", "April", "May"] and d>=1990 and d<= 2000:
    print(str(a + ", you are a spring baby of the nineties."))
elif b in ["June", "July", "August"] and d>=1990 and d<=2000:
    print(str(a + ", you are a summer baby of the nineties."))
elif b in ["September", "October", "November"]  and d>=1990 and d<=2000:
    print(str(a + ", you are a fall baby of the nineties."))
    
    
elif b in ["December", "January", "February"] and d>=1980 and d<= 1990:
    print(str(a + ", you are a winter baby of the eighties."))
elif b in ["March", "April", "May"] and d>=1980 and d<= 1990:
    print(str(a + ", you are a spring baby of the eighties."))
elif b in ["June", "July", "August"] and d>=1980 and d<=1990:
    print(str(a + ", you are a summer baby of the eighties."))    
elif b in ["September", "October", "November"]  and d>=1980 and d<=1990:
    print(str(a + ", you are a fall baby of the eighties."))
    
    
elif b in ["December", "January", "February"]  and d<=1980:
    print(str(a + ", you are a winter baby of the Stone Age."))
elif b in ["March", "April", "May"] and d<=1980: 
    print(str(a + ", you are a spring baby of the Stone Age."))
elif b in ["June", "July", "August"] and d<=1980:
    print(str(a +", you are a summer baby of the Stone Age."))
elif b in ["September", "October", "November"] and d<=1980:
    print(str(a + ", you are a fall baby of the Stone Age."))

