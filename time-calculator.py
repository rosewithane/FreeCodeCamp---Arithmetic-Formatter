def add_time(start, duration, starting_day=None):
  
  nday = ""
  nstart = start.split(":")
  nduration = duration.split(":")
  ap = nstart[1][3:]
  if ap == "PM":
    nstart0 = int(nstart[0]) + 12
  else:
    nstart0 = int(nstart[0])
  nright = int(nstart[1][0:2]) + int(nduration[1][0:2])
  add = nright // 60
  nright = nright % 60
  if nright < 10:
    nright = "0" + str(nright % 60)
  else:
    nright = str(nright)
  nleft = nstart0 + int(nduration[0]) + add
  k = nleft % 24
  if k < 12:
    ampm = "AM"
  else:
    ampm = "PM"
  dayslater = (nleft - nstart0)/24
  if dayslater < 1:
    if nleft < 24:
      dayslater = 0
      dayslaterstr = ""
    else:
      dayslater = 1 
      dayslaterstr = " (next day)"
  elif dayslater == 1:
    if nleft > 24:
      dayslater = 1 
      dayslaterstr = " (next day)"
  else:
    dayslater = (nleft - nstart0)//24
    dayslater += 1
    dayslaterstr = " (" + str(dayslater) + " days later)"
    
  if nleft > 12:
    if nleft % 12 == 0:
      nleft = 12
    else:
      nleft = nleft % 12

      
  if starting_day is not None:
    starting_day = starting_day[0].upper() + starting_day[1:].lower()
    if starting_day.startswith("M"):
      starting_day = 1
    elif starting_day.startswith("Tu"):
      starting_day = 2
    elif starting_day.startswith("W"):
      starting_day = 3
    elif starting_day.startswith("Th"):
      starting_day = 4
    elif starting_day.startswith("F"):
      starting_day = 5
    elif starting_day.startswith("Sa"):
      starting_day = 6
    else:
      starting_day = 7
        
    newday = (starting_day + dayslater) % 7    
    
    if newday == 0:
      nday = ", Sunday"
    elif newday == 1:
      nday = ", Monday"
    elif newday == 2:
      nday = ", Tuesday"
    elif newday == 3:
      nday = ", Wednesday"
    elif newday == 4:
      nday = ", Thursday"
    elif newday == 5:
      nday = ", Friday"
    elif newday == 6:
      nday = ", Saturday"


  return str(nleft) + ":" + nright + " " + ampm + nday + dayslaterstr