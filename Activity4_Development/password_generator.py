#Validates if variable is integer subroutine
def intValidator(num, highNum, lowNum):
    try:
        int(num)
    except ValueError:
        return False
    else:
        if int(num) > highNum or int(num) < lowNum:
            return False
        else:
            return True
#Basic inputs and validation for inputs
parcelCosts = []
name = input('Please input the name: ')
address = input('Please input the adress: ')
phoneNumber = input('Please input your phone number: ')
phoneNumberV = intValidator(phoneNumber, 99999999999, 0)
while phoneNumberV == False:
    phoneNumber = input('Error! Please re-input the phone number, since it is invalid: ')
    phoneNumberV = intValidator(phoneNumber, 99999999999, 0)
phoneNumberV = int(phoneNumber)
phoneNumber = phoneNumberV
parcelsAmount = input('How many parcels are being collected: ')
parcelsAmountV = intValidator(parcelsAmount, 6, 1)
while parcelsAmountV == False:
    parcelsAmount = input('Error! Please re-enter the amount of parcels, since it is invalid: ')
    parcelsAmountV = intValidator(parcelsAmount, 6, 1)
parcelsAmountV = int(parcelsAmount)
parcelsAmount = parcelsAmountV
#Information inputs and calculation for each parcel
for i in range(parcelsAmount):
    cost = 0
    height = input('Parcel ' + str(i) + ' height: ')
    heightV = intValidator(height, 99999, 0)
    while heightV == False:
        height = input('Error! The height you input is invalid: ')
        heightV = intValidator(height, 99999, 0)
    heightV = int(height)
    height = heightV
    length = input('Parcel ' + str(i) + ' length: ')
    lengthV = intValidator(length, 99999, 0)
    while lengthV == False:
        length = input('Error! The length you input is invalid: ')
        lengthV = intValidator(length, 99999, 0)
    lengthV = int(length)
    length = lengthV
    width = input('Parcel ' + str(i) + ' width: ')
    widthV = intValidator(width, 99999, 0)
    while widthV == False:
        width = input('Error! The width you input is invalid: ')
        widthV = intValidator(width, 99999, 0)
    widthV = int(width)
    width = widthV
    size = height + length + width
    weight = input('Parcel ' + str(i) + ' weight: ')
    weightV = intValidator(weight, 30, 0)
    while weightV == False:
        weight = input('Error! The height you input is invalid: ')
        weightV = intValidator(weight, 30, 0)
    weightV = int(weight)
    weight = weightV
    signature = input('Would you like parcel ' + str(i) + ' to have a signature? (type yes or no): ')
    while signature.lower() != 'yes' and signature.lower() != 'no':
        signature = input('Error! Please enter either yes or no for having a signature on this parcel: ')
    tracking = input('Would you like parcel ' + str(i) + ' to have tracking? (type yes or no): ')
    while tracking.lower() != 'yes' and tracking.lower() != 'no':
        tracking = input('Error! Please enter either yes or no for having tracking on this parcel: ')
    if size < 95:
        priceS = 5
    elif size >= 95 and size <= 150:
        priceS = 20
    elif size >= 151 and size <=450:
        priceS = 30
    else:
        print('Sorry, this parcel will not be collected as it exceeds the maximum/minimum size (0cm to 450cm)')
        priceS = 0
    if weight > 0 and weight <= 2:
        priceW = 5
    elif weight > 2 and weight <= 15:
        priceW = 20
    elif weight > 15 and weight <= 30:
        priceW = 30
    else:
        print('Sorry, this parcel will not be collected as it exceeds the maximum/minimum weight (0 kg to 30kg)')
        priceW = 0
    if priceW == 0 or priceS == 0:
        cost = 0
    else:
        if priceW > priceS:
            cost += priceW
        else:
            cost += priceS
        if signature.lower() == 'yes':
            cost += 2
        if signature.lower() == 'yes':
            cost += 5
        parcelCosts.append(cost)
#Basic outputs
print('Name: ' + name + '\nAddress: ' + address + '\nPhone Number: ' + str(phoneNumber) + '\nParcels to collect: ' + str(len(parcelCosts)))
finalTotal = 0
#Outputs price of each parcel
for i in range(len(parcelCosts)):
    print('Parcel ' + str(i) + ': £' + str(parcelCosts[i]))
    finalTotal += parcelCosts[i]
#Outputs total price of call parcels
print('Total: £' + str(finalTotal))
        
