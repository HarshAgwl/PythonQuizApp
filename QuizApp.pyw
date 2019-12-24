import tkinter as tk
from tkinter import ttk as ttk
import os
import uuid
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# Variables to store details for Round 1 
score=0
time=[00,00,00,00]
currentQuestion=0
#questionTexts=["1.Name Apple's first product .", "2.Who surpassed Bill Gates in world's richest person list recently ?", "3.Bitcoin's smallest fraction ", '4.Recent chip used in iPhone X', '5.The recent tradition used by smartphone companies for there flagship smartphones.', '6.According to which company Airtel has fastest internet', '7.Rumour about two carrier operating Indian companies to have a collaboration. ', '8.The company who provided free internet in India.', '9.Company which owns Whatsapp.', "10.World's most expensive smartphone.", '11.Social networking company having bird in its logo.', '12.This logo is of which gaming laptop.', '13.Asimo is created by which company ?', "14.Samsung's latest patent ?", '15.Lightning port is used by which company ?', '16.Sundar Pichai is CEO of which company?', "17.Name Samsung's virtual assistant ?", '18."""Do No Evil"" is tagline of ......"', '19."IC chip used in computer is made up of _______"', '20.Name the supercomputer made by Indian scientist ?', '21.Computer Hard Disk was introduced first in 1956 by ______', '22."Binary system uses the power of ______(in units)"', '23.When a computer stops working it is said to be as _________', '24.What is the maximum size of a word document created ? (MB)', '25.Mac Operating System is developed by which company ?', '26..gif is extension of ______', '27.Computer uses which type of number system to store data ?', '28.Smallest memory size _______', '29.Device used to convert digital to analog signals ?', '30.The place where accessories are connected in the computer is known as _________', '31.Which key is pressed boot to enter in safe mode ?', '32. Linux is example of ________ ', '33.Which browser is developed by Google ?', '34.The main page of website is known as ________', '35.Default page size of a work document is _______', '36.802.11 Describes which Network ?']
#questionAnswers=['Apple1', 'Jeff Bezos', 'Satoshi', 'A11 Bionic ', 'Bezel less Screen', 'Ookla', 'Vodafone & Idea', 'Jio', 'Facebook', 'Black Diamond iPhone', 'Twitter', 'Predator', 'Honda', 'Foldable Phone', 'Apple', 'Google', 'Bixby', 'Google', 'Silicon', 'Param', 'IBM', '2', 'Hang', '32', 'Apple', 'Image', 'Binary', 'Kilobyte', 'Modem', 'Port', 'F8', 'Operating System', 'Chrome', 'Home Page', 'A4', 'Wireless']
attempts=[""]*30

questionTexts=["1. The company who provided free internet in India.","2. Asimo is created by which company?","3. Identify whether following is a MAC address or IP Address '00-14-22-01-23-45'","4. According to which company Airtel has fastest internet","5. This logo is of which gaming laptop.","6. .gif is extension of ______","7. Computer uses which type of number system to store data ?","8. IC chip used in computer is made up of ","9. Which browser is developed by Google ?","10. The main page of website is known as ________ ","11. Sundar Pichai is CEO of which company?","12. Company which owns Whatsapp.","13. Social networking company having bird in its logo.","14. Default page size of a word document is _______","15. The place where accessories are connected in the computer is known as _________","16.  Linux is example of ________ ","17. Computer Hard Disk was introduced first in 1956 by ______","18. Smallest memory size _______","19. Device used to convert digital to analog signals ?","20. Rumour about two carrier operating Indian companies to have a collaboration. ","21. 'Do No Evil' is tagline of ......","22. Name Apple's first product ?","23. Bitcoin's smallest fraction ","24. 802.11 Describes which Network ?","25. Samsung's latest patent ?","26. Name the supercomputer made by Indian scientist ?","27. Mac Operating System is developed by which company ?","28. Name Samsung's virtual assistant ?","29. Who surpassed Bill Gates in world's richest person list recently ?","30. Recent chip used in iPhone X"]
questionAnswers=["Jio","Honda","MAC","Ookla","Predator","Image","Binary","Silicon","Chrome","Home Page","Google","Facebook","Twitter","A4","Port","Operating System","IBM","Kilobyte","Modem","VodafoneandIdea","Google","Apple1","Satoshi","Wireless","PalmScanning","Param","Apple","Bixby","JeffBezos","A11bionic"]

currentRound=0

# Variables to store detials for Round 2
score2=0
time2=[00,00,00,00]
#questionTexts2=["1. What is 1+2.","What is 2+9"]
#questionAnswers2=["3","11"]
attempts2=[""]*10

questionTexts2=["1. grebrekcuz","2. Burj Khalifa","3. ver 5.1.2600 - CODENAME (b.f.c.t.)","4. U.S. Patent #3,821,715 ","5. Find me in front of your eyes","6. SYyMH9GyI6aLNCTffzc9chtXPkkCqQaIUwAqFIKuZwQ=","7. Novell","8. Write the 4 dishes","9. Antminer x11 dash mining","10. CxOak4J2Hxr8K0EWplLm3mu8tWGYO9bnNLsE4JHfvMvcxVwHWCXkUVrieWvWLFUzA9/YGSRyN5wRd6n8iGEdqB8c4ed+vNci4NRpc6ktW2Nf+kyKJMiRNS795opZ0ZwO "]
questionAnswers2=["Mark Zuckerberg","Samsung","Whistler","Intel4004","Dell","HP","Wordperfect","bitsfishchickentreat","hashingalgorithm","Neurohacking"]

def strModify(userString):
    userString = userString.replace(" ","")
    userString = userString.lower()
    return userString

for i in range(len(questionAnswers)):
    questionAnswers[i]=strModify(questionAnswers[i])

for i in range(len(questionAnswers2)):
    questionAnswers2[i]=strModify(questionAnswers2[i])

# Configuring Main Window & The Canvas
mainRoot = tk.Tk()
mainRoot.resizable(width=False, height=False)
mainRoot.geometry('{}x{}'.format(960, 540))
root = tk.Canvas(mainRoot)
root.pack(fill=tk.BOTH,expand=1)




def startQuiz():
    if(classInput.get()!="" and nameInput.get!="" and houseInput.get!=""):
        global navButtons,currentRound
        currentRound=1
        ent1.place(x=400,y=200,width=200,height=40)
        update_time()
        timerLabel.place(x=760,y=90)
        l1.place(x=305,y=100)
        
        nextButton.place(x=445,y=250,width=100)
        nxtButton.place(x=405,y=320,width=200)
        informLabel.place(x=305,y=400)
        roundLabel.place(x=775,y=40)
        roundLabel.configure(text="Round 1")

        classLabel.place_forget()
        nameLabel.place_forget()
        beginButton.place_forget()
        houseInput.place_forget()
        houseLabel.place_forget()
        mainLabel.place_forget()
        nameInput.place_forget()
        classInput.place_forget()
        endRoundBut1.place(x=445,y=500,width=100)


def startQuiz2():
        informLabel.configure(text="")
        ent1.delete(0,tk.END)
        global navButtons,currentQuestion,roundLabel,currentRound
        currentQuestion=0
        currentRound=2
        ent1.place(x=400,y=200,width=200,height=40)
        update_time()
        timerLabel.place(x=760,y=90)
        l1.place(x=305,y=100)
        l1.configure(text=questionTexts2[currentQuestion])
        
        nextButton2.place(x=445,y=250,width=100)
        nxtButton2.place(x=405,y=320,width=200)
        informLabel.place(x=305,y=400)
        endRoundBut2.place(x=445,y=500,width=100)
        beginButton2.place_forget()
        
        roundLabel.configure(text="Round 2")
        roundLabel.place(x=775,y=40)
        classLabel.place_forget()
        nameLabel.place_forget()
        beginButton.place_forget()
        houseInput.place_forget()
        houseLabel.place_forget()
        mainLabel.place_forget()
        nameInput.place_forget()
        classInput.place_forget()

        nextButton2.place(x=445,y=250,width=100)
        nxtButton2.place(x=405,y=320,width=200)

        
def nextQuestion():
    global score,currentQuestion,questionTexts,questionAnswers,attempts
    attempts[currentQuestion]=ent1.get()
    if questionAnswers[currentQuestion]==strModify(attempts[currentQuestion]):
        informLabel.configure(text="Correct Answer.")
    else:
        informLabel.configure(text="Wrong Answer. \nTry Again or Proceed to next question.")
    l1.configure(text=questionTexts[currentQuestion])

def nextQuestion2():
    global score2,currentQuestion,questionTexts2,questionAnswers2,attempts
    attempts2[currentQuestion]=strModify(ent1.get())
    if questionAnswers2[currentQuestion]==strModify(attempts2[currentQuestion]):
        informLabel.configure(text="Correct Answer.")
    else:
        informLabel.configure(text="Wrong Answer. \nTry Again or Proceed to next question.")
    l1.configure(text=questionTexts2[currentQuestion])

imageFileGlobal=tk.PhotoImage(file='schoolLogo.gif')
imageGlobal = root.create_image(25,20,image=imageFileGlobal,anchor=tk.NW)

def finalNext():
    ent1.delete(0,tk.END)
    global currentQuestion,root,img1,imageFileGlobal,imageGlobal
    currentQuestion+=1
    if currentQuestion==4:
        root.tag_lower(img1)
        imageFileGlobal = tk.PhotoImage(file='Predator1.gif')
        imageGlobal = root.create_image(25,200,image=imageFileGlobal,anchor=tk.NW)
        root.image=imageFileGlobal
        root.tag_raise(imageGlobal)
    if currentQuestion==5:
        root.delete(imageGlobal)
        
   
    if(currentQuestion==(len(questionTexts)-1)):
        nxtButton.place_forget()
    l1.configure(text=questionTexts[currentQuestion])
    #ent1.set(text="")
    informLabel.configure(text="")

def finalNext2():
    ent1.delete(0,tk.END)
    global currentQuestion,imageFileGlobal,imageGlobal
    currentQuestion+=1
    if currentQuestion==1:
        root.tag_lower(img1)
        imageFileGlobal = tk.PhotoImage(file='BurjKhalifa4.gif')
        imageGlobal = root.create_image(25,200,image=imageFileGlobal,anchor=tk.NW)
        root.image=imageFileGlobal
        root.tag_raise(imageGlobal)
    elif currentQuestion==2:
        root.tag_lower(img1)
        imageFileGlobal = tk.PhotoImage(file='WindowsXP5.gif')
        imageGlobal = root.create_image(25,200,image=imageFileGlobal,anchor=tk.NW)
        root.image=imageFileGlobal
        root.tag_raise(imageGlobal)
    elif currentQuestion==4:
        root.tag_lower(img1)
        imageFileGlobal = tk.PhotoImage(file='Dell6.gif')
        imageGlobal = root.create_image(25,200,image=imageFileGlobal,anchor=tk.NW)
        root.image=imageFileGlobal
        root.tag_raise(imageGlobal)
    elif currentQuestion==6:
        root.tag_lower(img1)
        imageFileGlobal = tk.PhotoImage(file='BillGates2.gif')
        imageGlobal = root.create_image(25,200,image=imageFileGlobal,anchor=tk.NW)
        root.image=imageFileGlobal
        root.tag_raise(imageGlobal)
    elif currentQuestion==7:
        root.tag_lower(img1)
        imageFileGlobal = tk.PhotoImage(file='Nougat3.gif')
        imageGlobal = root.create_image(25,200,image=imageFileGlobal,anchor=tk.NW)
        root.image=imageFileGlobal
        root.tag_raise(imageGlobal)
    else:
        root.delete(imageGlobal)
    
    if(currentQuestion==(len(questionTexts2)-1)):
        nxtButton2.place_forget()
    l1.configure(text=questionTexts2[currentQuestion])
    #ent1.set(text="")
    informLabel.configure(text="")
    
def change(index):
    global currentQuestion
    currentQuestion=index
    l1.configure(text=questionTexts[currentQuestion])

submitted=0

timeFinalRound1=""
timeFinalRound2=""
timerReset=False

filename = str(uuid.uuid4())

def result():
    global time,score,submitted,score2,timeFinalRound1,timeFinalRound2
    if submitted==0:
        submitted=1
        
        nxtButton.place_forget()
        nextButton.place_forget()
        endBut.place_forget()
        informLabel.place_forget()
        timerLabel.place_forget()
        l1.place(x=305,y=100)

        ent1.place_forget()

        l1.configure(text="Thank you for participating " + nameInput.get() + "\n" + "Round 1 Score: " + str(score) + "\n" + "Round 2 Score: " + str(score2) + "\n" + "Total Score: " + str(score+score2) + "\n" + "Round 1 Time: " + timeFinalRound1 + "\n" + "Round 2 Time: " + timeFinalRound2)
        try:
            filename = nameInput.get()+"_"+classInput.get()+"_"+houseInput.get()+"_"+randomword(4)
            file = open(r"\\server-pc\Data\decrypt\student"+str(zz+1)+".txt","w")
            file.write("Name: "+nameInput.get()+"\n"+"Class: "+classInput.get()+ "\n" + "House: "+ houseInput.get() + "\n" + "Round 1 Score: " + str(score) + "\n" + "Round 2 Score: " + str(score2) + "\n" + "Total Score: " + str(score+score2) + "\n" + "Round 1 Time: " + timeFinalRound1 + "\n" + "Round 2 Time: " + timeFinalRound2)
            file.close()
        except:
            pass


def update_time():
    global time,timerLabel,timerReset
    if(timerReset==True):
        time=[00,00,00,00]
        timerReset=False
    mainRoot.after(1,update_time)
    timer_text=str(time[0])+str(":")+str(time[1])+str(":")+str(time[2])+":"+str(time[3])
    timerLabel.configure(text=timer_text)
    time[3]+=1
    if(time[3]==1000):
        time[3]-=1000
        time[2]+=1
    if(time[2]==60):
        time[2]-=60
        time[1]+=1
    if(time[1]==60):
        time[1]-=60
        time[0]+=1
    pass

def endRound1():
        global timerReset,timeFinalRound1
        timeFinalRound1 = str(time[0]) + " hours " + str(time[1]) + " minutes " + str(time[2]) + " seconds"
        nxtButton.place_forget()
        nextButton.place_forget()
        endBut.place_forget()
        endRoundBut1.place_forget()
        informLabel.place_forget()
        timerLabel.place_forget()
        timerReset=True
        beginButton2.place(x=460,y=420,width=100)
        ent1.place_forget()
        l1.place_forget()
    
def endRound2():
        global timeFinalRound2,score,score2
        timeFinalRound2 = str(time[0]) + " hours " + str(time[1]) + " minutes " + str(time[2]) + " seconds"
        nxtButton2.place_forget()
        nextButton2.place_forget()
        endRoundBut2.place_forget()
        informLabel.place_forget()
        timerLabel.place_forget()
        ent1.place_forget()
        l1.place_forget()
        endBut.place(x=445,y=500,width=100)
        for i in range(len(attempts)):
            if(questionAnswers[i]==attempts[i]):
                score+=10
        for i in range(len(attempts2)):
            if(questionAnswers2[i]==attempts2[i]):
                score2+=20


# The Timer Label
timerLabel = tk.Label(root,font="Courier 20 bold",fg="white",bg="black")

# Round Label
roundLabel = tk.Label(root,font="Courier 20 bold",fg="white",bg="black")

# User Deails Labels
mainLabel = tk.Label(root,font="Courier 30 bold",fg="white",bg="black")
mainLabel.configure(text="Enter Details")
mainLabel.place(x=350,y=100)

nameLabel = tk.Label(root,width=20,font="Courier 20 bold",fg="white",bg="black")
nameLabel.configure(text="Your Full Name:")
nameLabel.place(x=345,y=180)
classLabel = tk.Label(root,width=20,font="Courier 20 bold",fg="white",bg="black")
classLabel.configure(text="Your Class:")
classLabel.place(x=345,y=260)
houseLabel = tk.Label(root,width=20,font="Courier 20 bold",fg="white",bg="black")
houseLabel.configure(text="Your House:")
houseLabel.place(x=345,y=340)

nameInput = ttk.Entry(root)
nameInput.place(x=450,y=225)
classInput = ttk.Entry(root)
classInput.place(x=450,y=300)
houseInput = ttk.Entry(root)
houseInput.place(x=450,y=385)

# Applying the Background & School Logo
schoolLogo=tk.PhotoImage(file='schoolLogo.gif')
img2 = root.create_image(25,20,image=schoolLogo,anchor=tk.NW)
root.tag_raise(img2)
bg = tk.PhotoImage(file='mainBg.gif')
img1=root.create_image(0, 0, image=bg,anchor=tk.NW)
root.tag_lower(img1)


# The Main Heading of the Application
lMain = tk.Label(root,text="DECRYPT HUNT",font="Courier 45 bold",fg="white",bg="black")
lMain.place(x=300,y=20),

# Inform Label
informLabel = tk.Label(root,text="",font="Courier 15",fg="white",bg="black",width=35)
informLabel.configure(wraplength=400)

# Question Label
l1 = tk.Label(root,text="1. The company who provided free internet in India.",font="Courier 10 bold",fg="white",bg="black",width=55)
l1.configure(wraplength=400)

# The Main Question's Answer Entry Box
ent1 = ttk.Entry(root)
ent1.configure(text="asahsjbk")

# Submit Answer Button 1
nextButton = tk.Button(root,text="Submit",fg="white",bg="red",command=nextQuestion)

# Next Question Button 2 
nxtButton = tk.Button(root,text="Move to Next Question",fg="white",bg="blue",command=finalNext)

# Submit Answer Button 2
nextButton2 = tk.Button(root,text="Submit",fg="white",bg="red",command=nextQuestion2)

# Next Question Button 2 
nxtButton2 = tk.Button(root,text="Move to Next Question",fg="white",bg="blue",command=finalNext2)

#Begin Quiz Button
beginButton = tk.Button(root,text="Begin Quiz",command=startQuiz)
beginButton.place(x=460,y=420,width=100)

#Begin Round 2 Button
beginButton2 = tk.Button(root,text="Begin Round 2",command=startQuiz2)
#beginButton2.place(x=460,y=420,width=100)

# End Round button for Round 1 
endRoundBut1 = tk.Button(root,text="End Round",command=endRound1)

# End Round button for Round 2
endRoundBut2 = tk.Button(root,text="End Round",command=endRound2)

# Result Button to end the quiz
endBut = tk.Button(root,text="End Quiz",command=result)

def copy_text_to_clipboard(event):
    if currentRound==1:
        field_value = questionTexts[currentQuestion]
    elif currentRound==2:
        field_value = questionTexts2[currentQuestion]
    mainRoot.clipboard_clear()  # clear clipboard contents
    mainRoot.clipboard_append(field_value)  # append new value to clipbaord

l1.bind("<Button-1>", copy_text_to_clipboard) 

mainRoot.mainloop()
