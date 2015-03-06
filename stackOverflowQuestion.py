__author__ = 'ramon'

temps = []

while True:
    daily = raw_input("Today's Temperature: ")
    if daily == 'q':
        break
    elif daily.isdigit():
        daily = float(daily)
        if daily > 0:
            temps.append(daily)
        elif daily == 0:
            print "Temperature 0 is not allowed."
    else:
        print "Only possitive numbers for temperature please."

temps.sort()
print temps[0]
print temps[-1]

temps = sorted(temps)
print map(float, temps)

maximum = (max(temps))
print "Maximum:", maximum

import heapq

heapq.heapify(temps)
print heapq.nsmallest(1, temps)
print heapq.nlargest(1, temps)