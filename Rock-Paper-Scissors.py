#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
cond=True
countc=0
countp=0
while(cond):
    arr=['Rock','Paper','Scissors']
    u=input("Enter R-Rock, P-Paper, S-Scissors : ")
    x=0
    if(u.upper()=='R' or u.capitalize()=="Rock"):
            x=0
    elif(u.upper()=='P' or u.capitalize()=="Paper"):
            x=1
    elif(u.upper()=='S' or u.capitalize()=="Scissors"):
            x=2
    else:
        print("!!! Invalid choice !!!")
        x=3
    if(x!=3):
        v=random.randint(0,2)
        print("\nYour choice : ",arr[x])        
        print("Computer's choice : ",arr[v])
        if(v==x):
            print("\n***Draw")
        if(v==0 and x==1) or (v==1 and x==2) or (v==2 and x==0):
            print("\n***You win")
            countp+=1
        if(v==0 and x==2) or (v==2 and x==1) or (v==1 and x==0):
            print("\n***Computer win")
            countc+=1
        print("\nYou:",countp,"Pts","\nComputer:",countc,"Pts")
        if countc==5 or countp==5:
            cond=False
    print("---------------------------------------")
if(countp==5):
    print("*** YOU WIN ***")
else:
    print("*** COMPUTER WIN ***")

