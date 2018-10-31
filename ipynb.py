#!/usr/bin/env python
# coding: utf-8

# In[62]:


age_meriem=27


# In[63]:


age_manu=32


# In[64]:


age_hamza=age_manu-14


# In[65]:


age_hamza


# In[66]:


print(age_hamza)


# In[67]:


age_meriem


# In[68]:


age_manu


# In[69]:


print(age_meriem)


# In[70]:


print(age_manu)


# In[71]:


age_hamza=age_manu-age_meriem+13


# In[72]:


print("age_meriem=", "et age_manu=", "et age_hamza=")


# In[73]:


print("age_meriem=", age_meriem, "et age_manu=", age_manu, "et age_hamza=", age_hamza)


# In[74]:


print("age meriem+ age manu+ age hamza =", age_meriem+age_manu+age_hamza)


# In[75]:


#ceci est un premier exemple de condition
a=24
if a>22: # si a est supérieur à 22
  print ("a est supérieur à 22")


# In[76]:


if age_meriem<age_manu: 
    print("manu est plus agé que meriem")


# In[77]:


if age_meriem<age_manu:
    print("meriem est plus petite que manu!")
    if age_meriem>age_manu:
        print("meriem est plus grande que manu!")
       


# In[78]:


a=9
b=12
if a>5:
    b+=1
    print("a=", a, "et b=", b)


# In[79]:


annee=2018
age_meriem=27
age_manu=32
if annee>2017:
    age_meriem+=1
    age_manu+=1
    age_hamza+=1
    print("age meriem =", age_meriem, "et age manu =", age_manu, "et age hamza =", age_hamza)


# In[83]:


if age_meriem>=18:
    print("meriem est majeure son age est", age_meriem)
else:
    print("meriem est mineure sont age est", age_meriem)


# In[84]:


if age_meriem>18:
    print("meriem est plus grande que son frere hamza")
elif age_meriem<18:
    print("meriem est plus petite que son frere hamza")
else:
    print("meriem a le meme age que son frere hamza")


# In[92]:


age_hamza=18
if age_meriem>18:
    print("meriem est plus grande que hamza elle a", age_hamza+1, "ans ou plus")
elif age_meriem<18:
    print("meriem est plus petite que hamza elle a", age_hamza-1, "ans ou moins")
else:
    print("meriem a le meme age que hamza", age_hamza, "ans")


# In[93]:


age_meriem==6


# In[94]:


age_meriem<32


# In[95]:


age_meriem<age_manu


# In[96]:


age_meriem!=36


# In[98]:


age_manu!=32


# In[101]:


age_meriem=27
age_manu=32


# In[102]:


age_manu!=32


# In[107]:


age=21
majeur=False
if age>=18:
    majeur=True


# In[108]:


age_meriem==majeur


# In[116]:


age_meriem=27
majeur=True
if age_meriem<=18:
    majeur=False


# In[124]:


if age_meriem>=0:
    if age_meriem<19:
        print("meriem est née dans les années 2000, donc meriem a", age_meriem, "ans" )
       
if age_meriem>=19:
    if age_meriem<29:
        print("meriem est née dans les années 90', donc meriem a", age_meriem, "ans")
       
if age_meriem>=29:
    if age_meriem<39:
        print("meriem est née dans les années 80', donc meriem a", age_meriem, "ans")


# In[125]:


a=5
if a>=2:
    if a<=9:
        print(" a est dans l'intervalle allant de 2 à 9 inclus")
    else:
        print("a n'est pas dans l'intervalle allant de 2 à 9 inclus")


# In[127]:


if age_meriem>=0 and age_meriem<=27:
    print("meriem a vecu 27 ans") 
else:
    print("meriem n'a pas vecu 27 ans")


# In[128]:


if age_meriem==age_manu:
    print("meriem et manu ont le meme age")
else:
    print("meriem et manu n'ont pas le meme age")


# In[129]:


if age_meriem==age_hamza and age_manu==age_meriem:
    print("meriem hamza et manu ont le meme age")
if age_meriem>age_hamza and age_manu>age_meriem:
    print("meriem est plus agée que hamza et manu est plus agé que meriem")
if age_meriem>age_hamza and age_manu<age_meriem:
    print("meriem est plus grande que hamza et manu")


# In[134]:


if age_meriem>=0 and age_meriem<=35:
 if age_manu>=0 and age_manu<=35:
  if age_hamza>=0 and age_hamza<=30:
                print("meriem manu et hamza ont vécu la meme époque")
else:
    print("meriem manu et hamza n'ont pas vécu la meme époque")


# In[136]:


if age_meriem<20 or age_meriem>29:
    print("meriem n'a pas la vaingtaine")
else:
    print("meriem a la vaingtaine")


# In[137]:


majeur


# In[139]:


majeur=False
majeur


# In[140]:


majeur=False
if majeur is not True:
    print("vous n'etes pas encore majeur")


# In[145]:


meriem="femme"
manu="homme"


# In[148]:


if meriem is not False:
    print("meriem est un homme")
else:
    print("meriem est une femme")
    
    #mdrrrrrrrr


# In[149]:


majeur=True
if majeur is False:
    print("vous n'etes pas majeur")
else:
    print("vous etes majeur")


# In[150]:


annee=2018


# In[152]:


#test de la fonction input
annee=input("saisissez une année:")
print(annee)


# In[154]:


type(annee)


# In[158]:


annee=int(annee)
type(annee)


# In[159]:


print(annee)


# In[179]:


# tp tester si une année est bissextile
annee=input("saisissez une année")
annee=int(annee)
bissextile=False
if annee/400==0:
    bissextile=True
elif annee/100==0:
    bissextile=False
elif annee/4==0:
    bissextile=True
else:
    bissextile=False
    
if bissextile:
    print("l'année est bissextile")
else:
    print("l'année n'est pas bissextile")

    


# In[ ]:


annee=input("saisissez une année")
annee=int(annee)
bissextile=False

if annee/400==0:
    bissextile=True
elif annee/4==0 and annee/100!=0:
    bissextile=True
    else:
        bissextile=False
else:
        bissextile=True


# In[1]:


annee=input("saisissez une année")
annee=int(annee)
bissextile=False

if annee/400==0:
    bissextile=True
elif annee/4==0:
    if annee/100!=0:
      bissextile=True
    else:
        bissextile=False
else:
    bissextile=True
        
if bissextile:
    print("l'année est bissextile")
else:
    print("l'année n'est pas bissextile")


# In[5]:


annee=input("saisissez une année:")


# In[3]:


annee=int(annee)


# In[8]:


annee=input("saisissez une année:")
annee=int(annee)
bissextile=False

if annee/400==0:
    bissextile=True
elif annee/4==0:
    if annee/100!=0:
      bissextile=True
    else:
        bissextile=False
        
if bissextile:
    print("l'année est bissextile")
else:
    print("l'année n'est pas bissextile")


# In[1]:


annee=input("saisissez une année:")
annee=int(annee)
bissextile=False

if annee/400==0:
    bissextile=True
elif annee/100==0:
    bissextile=False
elif annee/4==0:
    bissextile=True
else:
    bissextile=False
    
if bissextile:
    print("l'année est bissextile.")
else:
    print("l'année n'est pas bissextile.")


# In[4]:


annee=input("entrer une année:")
annee=int(annee)
bissextile=True

if annee%400==0:  # (% le modulo permet de connaitre le reste de la division)( // permet de connaitre la partie entiere )
    bissextile=True
elif annee%4==0 and annee%100!=0:
    bissextile=True
else:
    bissextile=False
if bissextile:
    print("l'année", annee, "est bissextile")
else:
    print("l'annee", annee, "n'est pas bissextile")


# In[10]:


annee=input("entrer l'année:")
annee=int(annee)
if annee%400==0 or (annee%4==0 and annee%100!=0):
    print("l'année", annee, "est bissextile.")
else:
    print("l'année", annee, "n'est pas bissextile.")

