#Soh Myles
#TP061320

#Vaccines allowed for ages above 46
def ageOne():
    print('\nHere are the following available vaccines.')
    print('\t1.AF')
    print('\t2.BV')
    print('\t3.DM')
    print('\t4.EC')   

#Vaccines allowed for ages below 45
def ageTwo():
    print('\nHere are the following available vaccines.')
    print('\t1.AF')
    print('\t2.BV')
    print('\t3.CZ')
    print('\t4.DM')
    print('\t5.EC')

#Patients registering code
def patientsRegistry():
    #Location for vaccination
    try:
        location1=0
        while location1==0:
            print('Here are the two locations to recieve vaccination: VC1/ VC2.')
            location2=int(input('\nEnter which vaccination center you want to go(1/2): '))
            if location2==1 or location2==2:
                location1=location2
                
    except ValueError:
        print('Answer entered is not accepted.')
        print('Please retry again.')
        menu1()
    
    if location1==1:
        location1='VC1'
    elif location1==2:
        location1='VC2'
    
    #Name of patient
    name=input('Enter your name: ')
    
    #Age of patient and determine which vaccine can the patient receive
    try:
        age=int(input('Enter your age: '))
        if age<=12 or age>=99:
            print('You are not eligible for the vaccination.')
            menu1()
        elif age>=46:
            ageOne()
        else:
            ageTwo()
        if age>=46:
            try:
                vaccine1=0
                while vaccine1==0:
                    vaccine2=int(input('Enter which vaccine you would like to receive: '))
                    if vaccine2==1 or vaccine2==2 or vaccine2==3 or vaccine2==4 :
                        vaccine1=vaccine2
                    
                    if vaccine1==1:
                        vaccine1='AF'
                    elif vaccine1==2:
                        vaccine1='BV'
                    elif vaccine1==3:
                        vaccine1='DM'
                    elif vaccine1==4:
                        vaccine1='EC'
            except ValueError:
                print('Answer entered is not a number.')
                print('Please retry again.')
                ageOne()
        else:
            try:
                vaccine1=0
                while vaccine1==0:
                    vaccine2=int(input('Enter which vaccine you would like to receive: '))
                    if vaccine2==1 or vaccine2==2 or vaccine2==3 or vaccine2==4 or vaccine2==5:
                        vaccine1=vaccine2
                   
                    if vaccine1==1:
                        vaccine1='AF'
                    elif vaccine1==2:
                        vaccine1='BV'
                    elif vaccine1==3:
                        vaccine1='CZ'
                    elif vaccine1==4:
                        vaccine1='DM'
                    elif vaccine1==5:
                        vaccine1='EC'
            except ValueError:
                print('Answer entered is not a number.')
                print('Please retry again.')
                ageTwo()
    except ValueError:
        print('Answer entered is not accepted.')
        print('Please retry again.')
        menu1()
    #Which dosage of vaccine has the patient received.
    try:
        status1=0
        while status1==0:
            status2=int(input('Is this the first dosage or the second dosage?(1/2): '))
            if status2==1 or status2==2:
                status1=status2
    except ValueError:
        print('Answer entered is not accepted.')
        print('Please retry again.')
        menu1()
                    
        if status1==1:
            status1='1'
        elif status1==2:
            status1='2'
        
        
    #Patient ID (Identification Number)        
    try:
        ic=int(input('Enter your identification number: '))
    except ValueError:
        print('Answer entered is not a number.')
        print('Please retry again.')
        menu1()

    #Patients phone number
    try:
        phoneNumber=int(input('Enter phone number: '))
    except ValueError:
        print('Answer entered is not a number.')
        print('Please retry again.')
        menu1()

    #Patient Email            
    email=input('Enter Email address: ')

    #Inform patient about vaccine intervals
    if status1==1:
        if vaccine1=='AF':
            print('There will be two doses for the AF vaccine. Each in a 14 day interval.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='BV':
            print('There will be two doses for the BV vaccine. Each in a 21 day interval.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='CZ':
            print('There will be two doses for the CZ vaccine. Each in a 21 day interval.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='DM':
            print('There will be two doses for the DM vaccine. Each in a 28 day interval.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='EC':
            print('There will only be one dose for the EC vaccine.')
            print('You will be notified when there is a vaccination slot as soon as possible.')

    #Inform patients about the dosage left for their vaccines
    if status1==2:
        if vaccine1=='AF':
            print('There will be one more dose for the AF vaccine.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='BV':
            print('There will be one more dose for the BV vaccine.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='CZ':
            print('There will be one more dose for the CZ vaccine.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='DM':
            print('There will be one more dose for the DM vaccine.')
            print('You will be notified when there is a vaccination slot as soon as possible.')
        elif vaccine1=='EC':
            print('There is only one dose for EC, this means you have completed your vaccination.')
            print('Your registery will deleted.')
            exit()
    print('Thank you for registering and stay safe.')

    register=[location1, name, str(age), vaccine1, str(status1), str(ic), str(phoneNumber), email, '\n']
    if status1==1:
        fileHandler=open('patients1.txt','a')
        for alpha in register:
            fileHandler.write(alpha)
            fileHandler.write('\t')
        fileHandler.close
    elif status1==2:
        fileHandler=open('patients2.txt','a')
        for alpha in register:
            fileHandler.write(alpha)
            fileHandler.write('\t')
        fileHandler.close

#Check registered patients information
def checkRegistered():
    try:
        choose1=0
        while choose1==0:
            choose2=int(input('Please input the dosage you have registered for(1/2): '))
            if choose2==1 or choose2==2:
                choose1=choose2
    except ValueError:
        print('Answer entered is not accepted.')
        print('Please retry again.')
        menu2()
    if choose1==1:
        try:
            fhand=open('patients1.txt','r')
        except:
            print('File cannot be opened.')
            exit()
        searchInput=input('Please type in your name: ')
        for line in fhand:
            line=line.rstrip()
            if searchInput.lower() in line.lower():
                print('The following is what has been found.')
                print('---------------')
                print(line)
                print('---------------')
        fhand.close()
        menu2()
    elif choose1==2:
        try:
            fhand=open('patients2.txt','r')
        except:
            print('File cannot be opened.')
            exit()
        searchInput=input('Please type in your name: ')
        for line in fhand:
            line=line.rstrip()
            if searchInput.lower() in line.lower():
                print('The following is what has been found.')
                print('---------------')
                print(line)
                print('---------------')
        fhand.close()
        menu2()

#Secondary menu
def menu2():
    print("\nIs there anything else you want to do?")
    print("\t1.Check")
    print("\t2.Exit")
    try:
        a = int(input('Select number for your choice : '))
    except ValueError:
        print('Answer entered is not accepted.')
        menu2()
    if a==1:
        checkRegistered()
    elif a==2:
        exit()
    else:
        menu2()

#Main menu        
def menu1():
    print("\nWelcome to Covid-19 Vaccination registration system\n")
    print("\t1.Register")
    print("\t2.Check")
    print("\t3.Exit")

    try:
        a = int(input('Select number for your choice : '))
   
    except ValueError:
        print('Answer entered is not accepted.')
        menu1()

    if a==1:
        patientsRegistry()
    elif a==2:
        checkRegistered()
    elif a==3:
        exit()
    else:
        menu1()
menu1()  