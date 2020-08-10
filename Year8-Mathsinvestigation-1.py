import time
yesno = ''
print('Hello! I am Your Personal Camera Settings Calculator (PCSC)!')
while yesno != 'no':
 print("Choose lighting condition: Dusk(D), Sunset/Shade(S/S), Overcast(O), Cloudy(C), Lightly Cloudy(LC), Sunny(S), Snow/Sand(Sn/Sa), Default(De).")
 time.sleep(0.5)
 print('(No need to capitalize)')
 time.sleep(0.5)
 light = " "
 settings = [["Dusk", "50", "1/4000s", "f/22"], ["Sunset/Shade", "100", "1/2000s", "f/16"], ["Overcast", "200", "1/1000s", "f/11"], ["Cloudy", "400", "1/500s", "f/8.0"], ["Lightly Cloudy", "800", "1/250s", "f/5.6"], ["Sunny", "1600", "1/125s", "f/4.0"], ["Snow/Sand", "3200", "1/60s", "f/2.8"], ["Default", "6400", "1/30s", "f/2.0"]]
 dic = {"Dusk": 0, "Sunset/Shade": 1, "Overcast": 2, "Cloudy": 3, "Lightly Cloudy": 4, "Sunny": 5, "Snow/Sand": 6, "Default": 7, "D": 0, "S/S": 1, "O": 2, "C": 3, "LC": 4, "S": 5, "Sn/Sa": 6, "De": 7, "dusk": 0, "sunset/shade": 1, "overcast": 2, "cloudy": 3, "lightly cloudy": 4, "sunny": 5, "snow/sand": 6, "default": 7, "d": 0, "s/s": 1, "o": 2, "c": 3, "lc": 4, "s": 5, "sn/sa": 6, "de": 7}
 while light != "Dusk" and light != "Sunset/Shade" and light != "Overcast" and light != "Cloudy" and light != "Lightly Cloudy" and light != "Sunny" and light != "Snow/Sand" and light != "Default" and light != "D" and light != "S/S" and light != "O" and light != "C" and light != "LC" and light != "S" and light != "Sn/Sa" and light != "De" and light != "dusk" and light != "sunset/shade" and light != "overcast" and light != "cloudy" and light != "lightly cloudy" and light != "sunny" and light != "snow/sand" and light != "default" and light != "d" and light != "s/s" and light != "o" and light != "c" and light != "lc" and light != "s" and light != "sn/sa" and light != "de":
  light = input("What are the current lighting conditions? ")
  time.sleep(1)#User inputs current light conditions
  if light != "Dusk" and light != "Sunset/Shade" and light != "Overcast" and light != "Cloudy" and light != "Lightly Cloudy" and light != "Sunny" and light != "Snow/Sand" and light != "Default" and light != "D" and light != "S/S" and light != "O" and light != "C" and light != "LC" and light != "S" and light != "Sn/Sa" and light != "De" and light != "dusk" and light != "sunset/shade" and light != "overcast" and light != "cloudy" and light != "lightly cloudy" and light != "sunny" and light != "snow/sand" and light != "default" and light != "d" and light != "s/s" and light != "o" and light != "c" and light != "lc" and light != "s" and light != "sn/sa" and light != "de":
   print("Oops! It seems your information was invalid. Please re-enter.")
   time.sleep(0.5)
 b = dic[light]
 c = settings[b]
 p = 0
 j = c[0]
 v = c[1]
 y = c[2]
 w = c[3]
 z = ' '
 x = ' '
 while p != 'ISO' and p != 'Shutter Speed' and p != 'Aperture' and p != 'iso' and p != 'shutter speed' and p != 'aperture' and p != 'Shutter speed' and p != 's' and p != 'S' and p != 'i' and p != 'P' and p != 'a' and p != 'A':
  p = input('Which other value would you like to calculate (ISO(I) or shutter speed(S) or aperture(A)): ')
  time.sleep(1)
  if p != 'ISO' and p != 'Shutter Speed' and p != 'Aperture' and p != 'iso' and p != 'shutter speed' and p != 'aperture' and p != 'Shutter speed' and p != 's' and p != 'S' and p != 'i' and p != 'P' and p != 'a' and p != 'A':
   print("Oops! It seems your information was invalid. Please re-enter.")
   time.sleep(0.5)
 if p == 'ISO' or p == 'iso' or p == 'i' or p == 'I':
  while z != y:
   z = input('What is the Shutter Speed?')
   time.sleep(1)
   if z != y: 
    print(f'Your shutter speed is wrong! It should be {y} ! You should change this setting!')
    time.sleep(0.5)
    z = y
  while x != w:
   x = input('What is the Aperture?')
   time.sleep(1)
   if x != w:
    print(f'Your aperture is wrong! It should be {w} ! You should change this setting!')
    time.sleep(0.5)
    x = w
  time.sleep(0.5)
  print('-----------------------------------------')
  print('Summary of camera settings and lighting condition:')
  print('-----------------------------------------')
  time.sleep(0.5)
  print('Since your lighting condition is ' + j + ':')
  time.sleep(0.5)
  print(' - Your ISO should be ' + v + '.')
  time.sleep(0.5)
  print(' - Your shutter speed should be ' + y + '.')
  time.sleep(0.5)
  print(' - Your aperture should be ' + w + '.')
 if p == 'Shutter Speed' or p == 'Shutter speed' or p == 'shutter speed' or p == 's' or p == 'S':
  while z != v: 
   z = input('What is the ISO?')
   time.sleep(1)
   if z != v:
    print(f'Your ISO is wrong! It should be {v} ! You should change this setting!')
    time.sleeo(0.5)
    z = v
  while x != w: 
   x = input('What is the aperture?')
   time.sleep(1)
   if x != w:
    print(f'Your aperture is wrong! It should be {w} ! You should change this setting!')
    time.sleep(0.5)
    x = w
  time.sleep(0.5)
  print('-----------------------------------------')
  print('Summary of camera settings and lighting condition:')
  print('-----------------------------------------')
  time.sleep(0.5)
  print(f'Since your lighting condition is {j} :')
  time.sleep(0.5)
  print(f' - Your ISO should be {v} .')
  time.sleep(0.5)
  print(f' - Your shutter speed should be {y} .')
  time.sleep(0.5)
  print(f' - Your aperture should be  {w} .')
 if p == 'Aperture' or p == 'aperture' or p == 'a' or p == 'A':
  while z != y:
   z = input('What is the Shutter Speed?')
   time.sleep(1)
   if z != y: 
    print(f'Your shutter speed is wrong! It should be {y} ! You should change this   setting!')
    time.sleep(0.5)
    z = y
  while x != v: 
   x = input('What is the ISO?')
   time.sleep(1)
   if x != v:
    print(f'Your ISO is wrong! It should be {v} ! You should change this setting!')
    time.sleep(0.5)
    x = v
  time.sleep(0.5)
  print('-----------------------------------------')
  print('Summary of camera settings and lighting condition:')
  print('-----------------------------------------')
  time.sleep(0.5)
  print(f'Since your lighting condition is {j} :')
  time.sleep(0.5)
  print(f' - Your ISO should be {v} .')
  time.sleep(0.5)
  print(f' - Your shutter speed should be {y} .')
  time.sleep(0.5)
  print(f' - Your aperture should be  {w} .')
 while yesno != 'yes' and yesno != 'no':
  time.sleep(1)
  print('----------------------------------------------')
  yesno = input('Would you like to run the code again?')
  print("\n")
  if yesno != 'yes' and yesno != 'no':
   time.sleep(1)
   print('Oops! You entered the wrong value!')
   time.sleep(1)