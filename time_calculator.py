def add_time(start, duration, day = ""):
  # Separate Start hour, min and am/pm
  x = start.split()
  y = x[0].split(":")
  startmin = int(y[1])
  starthr = int(y[0])
  #Convert start hr to 24h format
  if x[1] == 'AM':
    if starthr == 12:
      starthr -= 12
  elif x[1] == 'PM':
    if starthr >= 1 and starthr <= 11:
      starthr += 12
  # Separate duration hour, min
  x = duration.split(":")
  durmin = int(x[1])
  durhr = int(x[0])
  #Add minutes and calc carry to hours
  mintot = startmin + durmin
  minres = mintot % 60
  mintohr = int(mintot / 60)
  #Add hours and calc carry to days
  hrtot = starthr + durhr + mintohr
  hrres = hrtot % 24
  hrtoday = int(hrtot/24)
  dayres = hrtoday % 7
  #convert hrs and min to string for display
  minres = str(minres)
  if len(minres) == 1:
    minres = '0' + minres
  if hrres == 0:
    hrres += 12
    ampm = 'AM'
  elif hrres >= 1 and hrres <= 11:
    ampm = 'AM'
  elif hrres == 12:
    ampm = 'PM'
  else:
    hrres -= 12
    ampm = 'PM'   
  hrres = str(hrres)
  #Calculate new_day
  if day != "":
    days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    lowday = day.lower()
    dayposn = days.index(lowday)
    indpos = dayposn + dayres - 7
    new_day = days[indpos]
    new_day = new_day.capitalize()
   #Arrange string for output
  if hrtoday == 0 and day == "":
    new_time = hrres + ':' + minres + ' ' + ampm
  
  elif hrtoday == 1 and day == "":
    new_time = hrres + ':' + minres + ' ' + ampm + ' (next day)'
   
  elif hrtoday > 1 and day == "":
    new_time = hrres + ':' + minres + ' ' + ampm + ' (' + str(hrtoday) + ' days later)'
   
  elif hrtoday == 0 and day != "":
    new_time = hrres + ':' + minres + ' ' + ampm + ', ' + new_day
   
  elif hrtoday == 1 and day != "":
    new_time = hrres + ':' + minres + ' ' + ampm + ', ' + new_day + ' (next day)'
   
  else: #hrtoday > 1 and day != "":
    new_time = hrres + ':' + minres + ' ' + ampm + ', ' + new_day + ' (' + str(hrtoday) + ' days later)'
    
    
 


  return new_time