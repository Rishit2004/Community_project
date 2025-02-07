import mysql.connector

#Global Variables Declaration

mydb=mysql.connector.connect(host='localhost',user='root',password='ritu12345',database='cbse')


while True:
    print("**************************************************************************************")
    print("                         NGO database management system                               ")
    print("**************************************************************************************")
    print("1.Information about our NGO")
    print('2.To enter donation record')
    print('3.To fetch all donation records')
    print('4.To find total money donated')
    print('5.To delete/clear all the donation records entered till now')
    print('6.Sign up for volunteer work')
    print('7.To clear all data entered for volunteer work')
    print('8.Find information about voluunteers')
    print('9.Print records of all the volunteers')
    print('10.Exit the system')
    print("--------------------------------------------------------------------------------------")
    a=int(input("Enter your choice here from(1,2,3,4,5,6,7,8,9,10):"))

    #option 1
    if(a==1):
        print("What information do you want?:")
        print("1.What is an NGO")
        print("2.What is the objective of our NGO:")
        opt=int(input("Enter your choice:"))
        #choice 1
        if(opt==1):
            print("A non-governmental organization (NGO) is a group that functions independently")
            print("of any government. It is usually non-profit. NGOs, sometimes called civil society")
            print("organizations, are established on community, national, and international levels")
            print("to serve a social or political goal such as a humanitarian cause or the")
            print("protection of the environment.")
        #choice 2
        if(opt==2):
            print("We are trying to help people who cannot get educated due to lack of resources.")
            print("Approximately 74.04% of the Indian population is still illiterate, our objective is to change this")
            print("We are developing and creating schools all over India in different states, till now we have to setup 48 schools across the country")
            print("We are following all the government guidelines for our NGO and also have been affiliated by them.")
            print("--------------------------------------------------------------------------------------")

    #option 2
    elif (a==2):
        mycursor=mydb.cursor()
        mycursor.execute('use cbse')
        srno=int(input('Enter SrNo:'))
        name=input('Enter Name:')
        amount=int(input('Enter Amount Donated:'))
        sql = 'insert into MYNGO (SrNo , Name , AmountDonated) VALUES(%s,%s,%s)'
        val = (srno,name,amount)
        mycursor.execute(sql,val)
        print(mycursor.rowcount,'record inserted')
        mydb.commit()
        if amount>=10:
            print('Thank you for your generous donation')
        else:
            continue
        
    #option 3
    elif(a==3):
        mycursor=mydb.cursor()
        mycursor.execute('use cbse')
        mycursor.execute('select * from MYNGO')
        mydata=mycursor.fetchall()
        rec=mycursor.rowcount
        print('Total number of records fetched are',rec)
        print(mydata)
        
    #option 4
    elif(a==4):
        mycursor=mydb.cursor()
        mycursor.execute('use cbse')
        sum1=mycursor.execute('select SUM(amountdonated) FROM MYNGO')
        sum2=mycursor.fetchall()
        print(sum2)
        
    #option 5
    elif(a==5):
        mycursor=mydb.cursor()
        mycursor.execute('use cbse')
        mycursor.execute('delete from myngo')
        mydb.commit()
        print('All records deleted')
        
    #option 6
    elif(a==6):
        import csv
        def write():
            f=open('record.csv','a',newline='')
            name=input('Enter your name:')
            age=int(input('Enter your age:'))
            add=input('Enter your address:')
            num=int(input('Enter your contact number:'))
            reason=input('Enter reason to join MYNGO:')
            x=csv.writer(f)
            x.writerow([name,age,add,num,reason])
            f.close()
        write()
        
    #option 7
    elif(a==7):
        f=open('record.csv','w')
        f.flush()
        print("All data cleared")
        
    #option 8
    elif(a==8):
        import csv
        def search():
            n=input("Enter name to be searched:")
            f1=open('record.csv','r')
            r=csv.reader(f1)
            for row in r:
                if n==row[0]:
                    print("Name,Age,Address,Mobile number,Reason of joining")
                    print(row)
                else:
                    print("No record found with this name.......")
        search()
        
    #option 9
    elif(a==9):
        import csv
        def read():
            f1=open('record.csv','r')
            r=csv.reader(f1)
            for row in r:
                print(row)
        read()
        
    #option 10
    elif(a==10):
            break
    ch=input('Do you want to enter anything else? yes/no:')
    if(ch=='no'):
        break

