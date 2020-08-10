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