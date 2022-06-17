speedLimit = int(input("What is the speed limit in 'miles per hour'? "))
offenderSpeed = int(input("What speed was the offender going in 'miles per hour'? "))
offenderViolations = int(input("How many previous violations does the offender have? "))
costPerMPH = 20.00
courtCost = 74.80


speedViolation = offenderSpeed - speedLimit
print("Offender went " + str(speedViolation) + " miles per hour over the speed limit.")
speedingTicket = speedViolation * costPerMPH
print("Offender will be charged $%6.2f for speeding." % (speedingTicket))
courtCharge = offenderViolations * courtCost
print("Offender will be charged $%6.2f for previous speeding violations." % (courtCharge))
totalCharges = speedingTicket + courtCharge
print("Offender will be charged a total of $%6.2f." % (totalCharges))