
def printer(naam, leeftijd):
    print('Hello ' + naam + ' Je leeftijd is ' + leeftijd)

a = 0
while a < 1:
    input1 = input("Vul je naam in: ")
    if input1  == 'stop':
        break
    input2 = input("Vul je leeftijd in: ")
    if input2  == 'stop':
        break

    
    orginalnaam = input1
    orginalleeftijd = input2

printer(orginalnaam, orginalleeftijd)