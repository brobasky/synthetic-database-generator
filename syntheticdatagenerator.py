#takes cities.csv and names.csv as input
#outputs csv files for each relation that can be loaded into sql with load data
#NOTE: running this script will overwrite small sample data files with the full length data-files


import random
import pandas as pd

def PickNames(namelist,listsize):
    randomnames=[]
    for i in range(listsize):
        index = random.randint(0,len(namelist)-1)
        randomnames.append(namelist[index])
    return randomnames

def uniqueNdigitstrings(listsize,digits,existingIDs=[]):
    IDlist=[]
    while len(IDlist)<listsize:
        number=''
        for j in range(digits):
            number = number + str(random.randint(0,9))
        if number in IDlist or number in existingIDs:
            continue
        else:
            IDlist.append(number)
    return IDlist

def GenerateAvailibility(listsize,maxdaynum):
    weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    AvailibilityList=[]
    for i in range(listsize):
        NumberOfDays= random.randint(1,maxdaynum)
        PossibleIndicies=list(range(7))
        Availibility=[]
        for i in range(NumberOfDays):
            Index=PossibleIndicies[random.randint(0,len(PossibleIndicies)-1)]
            Availibility.append(weekdays[Index])
            PossibleIndicies.remove(Index)
        AvailibilityList.append(Availibility)
    return AvailibilityList

def GenerateDollarAmounts(listsize,high,low):
    MoneyList = []
    for i in range(listsize):
        MoneyList.append(round(random.uniform(low,high),2))
    return MoneyList

def GenerateInstruments(listsize):
    InstrumentChoices=['Guitar','Bass','Drums','Piano','Woodwinds','Brass','Violin','Cello']
    Instruments= []
    for i in range(listsize):
        Instruments.append(InstrumentChoices[random.randint(0,7)])
    return Instruments

def GenerateBrands(listsize):
    BrandChoices=['Fender','Gibson','Yamaha','Kawai','Martin','Ibanez','PRS','Steinway']
    Brands= []
    for i in range(listsize):
        Brands.append(BrandChoices[random.randint(0,7)])
    return Brands

#this won't make realistic data because the model isnt specific to instrument type, but the assignment said gibberish was ok
def GenerateModels(listsize):
    ModelChoices=['Stratocaster','Les Paul','ES-335','Explorer','Telecaster','Thunderbird']
    Models= []
    for i in range(listsize):
        Models.append(ModelChoices[random.randint(0,5)])
    return Models

def GeneratePaymentStatus(listsize,weight1,weight2):
    options=['paid','unpaid']
    statuslist=random.choices(options,weights=(weight1,weight2),k=listsize)
    return statuslist


def main():
    #names csv file copied from https://github.com/aruljohn/popular-baby-names/commit/32d06c30e4f904fc8ee7e923178362f9a82d03af#diff-1fbb4196c9de298e6f78620294421b042c0d0305b53cc1a22464d10183c41373
    namesdf= pd.read_csv('names.csv')
    #cleaning csv file and turning it into a list of names to pick from
    nameslist = namesdf['Girl Name'].tolist()
    boynamelist = namesdf['Boy Name'].tolist()
    nameslist = nameslist+boynamelist
    citiesdf=pd.read_csv('cities.csv')
    citieslist=citiesdf['City'].tolist()

    random.seed(12345)
    #generating data for teachers table
    TeacherNames=PickNames(nameslist,5000)
    TeacherPhoneNumbers = uniqueNdigitstrings(5000,10)
    Availibilities = GenerateAvailibility(5000,1)
    #monthly revenue - dollar amount somewhere between 100 and 700
    TeacherMonthlyRevenues = GenerateDollarAmounts(5000,100.00,700.00)
    TeacherInstrumentList = GenerateInstruments(5000)
    TeacherIDnumbers = uniqueNdigitstrings(5000,5)
    teacherdf=pd.DataFrame(list(zip(TeacherIDnumbers,TeacherNames,TeacherMonthlyRevenues,Availibilities,TeacherPhoneNumbers,TeacherInstrumentList)))
    teacherdf.to_csv('teacherdata.csv',index=False)

    #generating data for employees table
    EmployeeIDnumbers=uniqueNdigitstrings(3000,5,TeacherIDnumbers)
    EmployeeNames=PickNames(nameslist,3000)
    EmployeeSalaries=GenerateDollarAmounts(3000,2000.00,4000.00)
    EmployeeSales=GenerateDollarAmounts(3000,2000.00,20000.00)
    EmployeePhoneNumbers=uniqueNdigitstrings(3000,10,TeacherPhoneNumbers)
    employeedf=pd.DataFrame(list(zip(EmployeeIDnumbers,EmployeeNames,EmployeeSales,EmployeeSalaries,EmployeePhoneNumbers)))
    employeedf.to_csv('employeedata.csv',index=False)

    #generating data for instruments table
    SerialNumbers=uniqueNdigitstrings(30000,15)
    InstrumentType=GenerateInstruments(30000)
    InstrumentBrands=GenerateBrands(30000)
    InstrumentModels=GenerateModels(30000)
    InstrumentPrices=GenerateDollarAmounts(30000,100.00,5000.00)
    instrumentdf=pd.DataFrame(list(zip(SerialNumbers,InstrumentType,InstrumentBrands,InstrumentModels,InstrumentPrices)))
    instrumentdf.to_csv('instrumentdata.csv',index=False)

    #generating data for stores relation
    address=uniqueNdigitstrings(200,3) #just using random numbers for addresses for the sake of time
    storenumber=uniqueNdigitstrings(200,4)
    storecities=PickNames(citieslist,200)
    storecost=GenerateDollarAmounts(200,50000.00,100000.00)
    storesdf=pd.DataFrame(list(zip(address,storenumber,storecities,storecost,storecost)))
    storesdf.to_csv('storesdata.csv',index=False)

    #generating data for students relation
    studentphonenumbers=uniqueNdigitstrings(20000,10,EmployeePhoneNumbers+TeacherPhoneNumbers)
    studentnames=PickNames(nameslist,20000)
    studentinstruments=GenerateInstruments(20000)
    lessondates=GenerateAvailibility(20000,1)
    paymentstatuses=GeneratePaymentStatus(20000,70,30)
    studentdf=pd.DataFrame(list(zip(studentphonenumbers,studentnames,studentinstruments,lessondates,paymentstatuses)))
    studentdf.to_csv('studentdata.csv',index=False)

    #combining data for sells relation
    sellserial=SerialNumbers
    sellstore=[]
    for i in range(30000):
        index=random.randint(0,199)
        sellstore.append(storenumber[index])
    sellsdf=pd.DataFrame(list(zip(sellstore,sellserial)))
    sellsdf.to_csv('sellsdata.csv',index=False)

    #combining data for employs relation
    R_employsID=EmployeeIDnumbers
    R_employsStore=[]
    for i in range(3000):
        index=random.randint(0,199)
        R_employsStore.append(storenumber[index])
    employsdf=pd.DataFrame(list(zip(R_employsStore,R_employsID)))
    employsdf.to_csv('R_employsData.csv',index=False)

    #combining data for have relation
    havephone=studentphonenumbers
    haveIDs=[]
    for i in range(20000):
        index=random.randint(0,4999)
        haveIDs.append(TeacherIDnumbers[index])
    havedf=pd.DataFrame(list(zip(haveIDs,havephone)))
    havedf.to_csv('havedata.csv',index=False)

if __name__ == '__main__':
    main()
