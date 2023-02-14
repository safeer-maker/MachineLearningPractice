#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import numpy as np
import pandas as pd
# from gui_stuff import *
print(" strting of the program ")
l1=['jaundice yellow eyes', 'swelling oedema abdomen', 'fever', 'confused', 'tremors', 'itchy skin', 'History of alcohol abuse', 'abdominal pain - sharp, lower right side', 'nausea', 'diarrhoea', 'wheezing ', 'shortness of breath', 'chest tightness', 'cough', 'history of allergy', 'tested for positive for breath volume and speed', 'headache', 'dizziness', 'exposure to carbon monoxide', 'developmental problems', 'delayed development', 'weakness', 'poor coordination', 'rash', 'itchy red skin', 'papules fluid filled blisters ', 'chronic prolonged cough', 'phlegm sputum', 'history of smoking', 'blue appearance on tongue', 'gets tired easily ', 'runny nose', 'sore throat', 'nose congestion', 'sneezing', 'a season for common cold', 'fast heart beat', 'blue lips and tongue', 'difficulty feeding', 'chest pain', 'poor concentration', 'mood change', 'memory loss', 'fever - acute', 'rash - on face and limbs', 'headache - severe', 'muscle ache pain', 'mild bleeding gums, nose', 'joint pains', 'reduced eyesight', 'diabetes with persistent high blood glucose', 'history of poorly controlled diabetes', 'diarrhoea - waterly stool', 'abdominal pain', 'vomiting', 'cramps', 'muscle spasm', 'low muscle strength', 'bleeding from nose, ears, orifices', 'rash - dry and scaly', 'rash - itchy rash', 'pain on skin', 'fainting', 'urination or self wetting and frothing', 'convulsions', 'loss of consciousness', 'twitches or stiffness', 'heavy periods or vaginal bleeding', 'irregular or prolonged menstruation', 'painful periods', 'abdomal pain - lower abdomen', 'frequent micturation', 'abdominal distention of fullness', 'ingested eaten contaminated food ', 'feeling full quickly', 'low appetite', 'cluster of blisters on genitals or penis', 'painful ulceration wound on genitals', 'fluid filled pimples on genitals', 'history of sexual contact', 'reduced vision', 'pain in eyes', 'red eyes', 'tiredness or fatigue', 'dark urine', 'abdominal pain - right upper quantrant', 'puss filled blisters pimples postules', 'rash - red rash patch on the face', 'blisters with yellow-brown crusts of broken blisters', 'abdominal pain - chronic', 'blood mucus in stool', 'diarrhoea on and off ', 'gas fart', 'weight loss', 'constipation', 'bloating & gas farting', 'fever - intermittent', 'shivering', 'body and joint pains', 'loss of appetite', 'positive malaria test', 'travel to malaria zones', 'breast pains', 'warmth or redness on breast', 'swelling on breast', 'breast warm to touch', 'discharge from breast', 'breast feeding', 'rash - fine generalized rash - maculopapular', 'runny nose and cough', 'light hurts eyes', 'pain in jaw parotid area', 'swelling in the jaw', 'testicular pain', 'joint swelling', 'joint crackles', 'warmth on the joint', 'mucus', 'reduced air entry ', 'low SPO2 below 94%', 'chest indrawing', 'hallucinations or hearing things that are not there', 'delusions or strange beliefs', 'anxiety', 'after delivery', 'high blood pressure', 'oedema or swollen legs', 'protein in urine positive test', 'blurred vision', 'abdominal pain - at epigastria', 'hydrophobia fear of water', 'muscle spasms', 'confusion and aggression', 'mood instability', 'animals bite', 'joint pains and swelling', 'rash - red rash', 'fatigue', 'recurrent chest infections', 'bowed legs', 'delayed sitting', 'delayed crawling', 'delayed standing', 'problems with teeth', 'stunted growth', 'bone pains', 'swollen glands', 'rash - rash between fingers, toes, ampits and genitals', 'scaling of skin', 'poor hygiene', 'delusions', 'hallucinations', 'abnormal thoughts', 'upsetting thoughts', 'recurrent frequent infections', 'anaemia', 'muscle stiffness', 'locked jaw', 'difficulty swallowing', 'inability to suck', 'vomitting', 'back arch and stiffness - episthotomus', 'throat pain ', 'hoarseness of voice', 'swollen tonsils', 'cough more than 2 weeks', 'drenching night sweats', 'contact with TB patient', 'loss of skin colour', 'premature whitening of body hair', 'hypopigmented skin patch', 'alcohol craving', 'insomnia lack of sleep', 'shaking and sweating', 'tremors and slurred speech', 'alcohol dependence', 'forgetfulness', 'depression', 'mental decline', 'social withdrawal', 'mood swings', 'distrust in others', 'irritability and aggressiveness', 'changes in sleeping habits', 'wandering', 'abdominal pain - lower abdomen', 'mucoid or blood stool', 'flatulence', 'pale or whitish skin', 'irregular heartbeats', 'light headedness', 'cold hands and feet', 'low haemoglobin test result - low HB', 'feeling nervous', 'restless', 'tense', 'panic', 'doom feeling', 'increased heart rate', 'breathing rapidly', 'sweating', 'trembling', 'behavioural problems', 'difficulty speaking', 'problems mixing with others', 'pain in ear', 'hearing loss', 'discharge in ear', 'body swelling', 'nausea and vomitting', 'abdominal pain - epigastria', 'chills body shaking', 'stiff neck', 'body pains and stiffness', 'photophobia fear of light', 'projectile vomiting', 'bulging fontanelles', 'fever slight', 'chest discomfort', 'fever - recurrent', 'back pain', 'exposure to raw unpasteurised milk products', 'oral thrush white patches on mouth', 'pain swallowing', 'white patches in mouth', 'itchy skin on genitals', 'vulval burning sensation', 'whitish curdy vaginal discharge', 'flu mild', 'enlarged glands', 'Joint pains', 'genital discharge - clear', 'bleeding after sex', 'diarrhoea - effortless watery diarrhea', 'thirsty and dehydration', 'leg cramps', 'irritability', 'lower limbs legs swelling', 'unable to lie flat', 'easy fatigibility', 'rapid heartbeat - palpitations', 'irregular heartbeat', 'cough - frothy sputum', 'pink blood-tinged mucus', 'rapid weight gain', 'abdominal swelling', 'long standing hypertension', 'loss of taste', 'irritated eyes', 'difficulty breathing', 'frequent urination - polyuria', 'excessive thirst - polydipsia', 'frequent extreme hunger - polyphaghia', 'sudden vision changes - blurred vision', 'tingling', 'numbness ', 'dry skin', 'flattened face', 'bridge nose', 'almond-shaped eyes', 'short neck', 'widely spaced big toe', 'small ears - low set ears', 'mental retardation', 'small hands', 'short stature', 'single palmer crease', 'heartburn', 'epigastric pain - upper abdomen below ribs', 'difficult swallowing', 'regurgitation of food vomiting', 'anterior neck swelling', 'throat tightness', 'fast heart rate', 'hoarse voice', 'heat intolerance', 'visible prominent neck veins', 'pain passing urine', 'abnormal discharge from genitals - yellow / creamy', 'frequent in urination', 'chills body shaking and sweats', 'dry cough', 'difficulty falling asleep', 'waking up too early', 'not feeling well', 'sleepiness', 'difficulty paying attention', 'progressive emaciation', 'anemia', 'enlarged spleen and liver', 'discolored patches of skin with loss of sensation', 'disfigured or missing fingers', 'disfigured or missing toes', 'loss of eyebrows', 'nodules swelling on skin', 'easy bleeding', 'pale skin', 'easy bruising', 'neck swelling', 'delirium', 'shock', 'liver failure', 'massive haemorrhaging', 'sudden chest tightness', 'pressure in the chest', 'acute chest pain on left side', 'abnormal blood pressure', 'chest pain radiating to left jaw or left shoulder', 'cyanosis - bluish skin discolouration', 'flaring of nostrils', 'tachypnea - rapid breathing (> 60breaths/ min)', 'shallow breathing', 'chest indrawing - inward movement of the lower chest wall when the child breathes in', 'reduced urine output', 'grunting while breathing', 'fever - persistant and steadily increasing', 'sudden weakness or floppiness of limbs', 'pain in the arms', 'weakness of limbs', 'limbs wasting', 'pain in the legs', 'progressive muscle weakness', 'tension or anxiety', 'depressed mood', 'hot flushes', 'anger', 'morning joint stiffness', 'unresponsiveness to antibiotics', 'numbness in the leg along the nerve', 'back pain - lower back', 'tingling sensation in the feet and toes', 'abdominal pain - burning pain', 'bloating gas fart?', 'feeling full easily', 'burping', 'acid reflux', 'sudden one sided body numbness', 'weakness on one side of body', 'sudden confusion', 'trouble speaking', 'incoherent speech', 'sudden difficult in walking', 'loss of balance', 'lack of coordination', 'blood in urine', 'malaise - body weakness', 'blood in stool', 'urethral discharge', 'frequent passing urine', 'refusal to feed', 'difficult in breathing', 'severe chest wall indrawing', 'bulging fontanelle - on head (front)', 'diarrhoea and or vomitting', 'weak or absent pulse', 'reduced level of consciousness', 'skin pinch slow - >3 seconds', 'delayed capillary refil >3 seconds', 'sunken eyes', 'skin pinch slow - > or 2 seconds', 'unable to drink or breastfeed', 'skin pinch slow 1-2 seconds', 'consciousness - irritable and restless', 'fast breathing', 'coughing', 'low spo2 <94%', 'lower chest indrawing', 'runny nose and or cough child', 'lack of balance - body weakness', 'floppiness', 'stiffness', 'delayed milestone', 'seizures', 'birth weight 1500-2499 grams', 'birth weight between 1000-1499 grams', 'birth weight less than 1000 grams', 'blood in stool or bloody diarrhoea', 'nose bleeding / epistaxis', 'elevated / high blood pressure', 'increased salivation', 'constricted pupil', 'confusion', 'excessive body secretions ', 'reduced consciousness', 'sores around the mouth or lips', 'cluster blisters around the mouth', 'painful', 'rash - painful red rash', 'rash - segmental distributed rash', 'rash - burning sensation on the rash', 'rash - red rash on the face', 'yellow brown crusts from broken blisters', 'blisters', 'abdominal distention', 'diarrhoea and vomiting', 'jaundice yellow eyes - within two weeks', 'bleeding or hemorrhage']

disease=['Alcohol-related liver disease','Appendicitis', 'Asthma', 'Carbon monoxide poisoning', 'Cerebral palsy', 'Chickenpox', 'Chronic obstructive pulmonary disease (COPD)', 'Common cold', 'Congenital heart disease-Infants', 'Dementia', 'Dengue fever', 'Diabetic retinopathy', 'Diarrhoea', 'Dystonia', 'Ebola virus disease', 'Eczema (atopic)', 'Epilepsy', 'Fibroids', 'Food poisoning', 'Gastroenteritis', 'Genital herpes', 'Glaucoma', 'Hepatitis B', 'Impetigo', 'Inflammatory bowel disease', 'Irritable bowel syndrome (IBS)', 'Malaria', 'Mastitis', 'Measles', 'Migraine', 'Mumps', 'Osteoarthritis', 'Pneumonia', 'Postpartum psychosis (psychosis after childbirth)', 'Pre-eclampsia', 'Rabies', 'Rheumatic fever -Children', 'Rickets and osteomalacia- children', 'Rubella', 'Scabies', 'Scarlet fever', 'Schizophrenia', 'Sickle cell disease (sickle cell anaemia)', 'Tetanus', 'neonatal tetanus - tetanus', 'Tonsillitis', 'Tuberculosis (TB)', 'Vitiligo / leucoderma', 'Alcohol Abuse and Alcoholism', 'Alzheimer', 'Amoebiasis', 'Anaemia', 'Anxiety', 'Autism spectrum disorder (ASD)', 'Ear infection- Otitis media', 'Eclampsia', 'Meningitis', 'Bronchitis', 'Brucellosis', 'Candidiasis -Oral', 'Candidiasis - vaginal', 'Chagas disease', 'Chikungunya Fever', 'Chlamydia', 'Cholera ', 'Congestive heart disease', 'Coronavirus (COVID-19)', 'Diabetes Mellitus', "Down's Syndrome", 'Gastro Eoesophageal Reflux Disorder (Gerd)', 'Goitre', 'Gonorrhea', 'Influenza', 'Insomnia', 'Kala-azar/ Leishmaniasis', 'Leprosy', 'Leukemia', 'Marburg fever', 'Myocardial Infarction (Heart Attack)', 'Neonatal Respiratory Disease Syndrome(NRDS)', 'Paratyphoid fever/ Typhoid', 'poliomyelitis - Acute flaccid paralysis', 'Premenstrual syndrome', 'Rheumatism', 'Rift Valley fever', 'Sciatica ', 'gastritis / Stomach ulcers', 'hypertensive stroke - CVA', 'schistosomiasis / Bilhazia', 'Upper respiratory infection', 'UTI- Urinary tract infection', 'neonatal sepsis and jaundice', 'dehydration shock', 'severe dehydration', 'some dehydration', 'very severe pneumonia', 'severe pneumonia', 'pneumonia ', 'cough or cold', 'cerebral palsy', 'low birth weight', 'very low birth weight', 'extremely low birth weight', 'dysentry', 'hypertension / high blood pressure', 'organophosphate poisoning', 'herpes labialis', 'herpes zoster', 'impetigo', 'helminthiasis / worms', 'yellow fever', 'Zika virus']
print(" done with l1 so that we can go ahead with further changes ")
l2=[]
l_sex=['male','female']
l_adults=['adult','child']
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------                                

df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Alcohol-related liver disease':0, 'Appendicitis':1, 'Asthma':2, 'Carbon monoxide poisoning':3, 'Cerebral palsy':4, 'Chickenpox':5, 'Chronic obstructive pulmonary disease (COPD)':6, 'Common cold':7, 'Congenital heart disease-Infants':8, 'Dementia':9, 'Dengue fever':10, 'Diabetic retinopathy':11, 'Diarrhoea':12, 'Dystonia':13, 'Ebola virus disease':14, 'Eczema (atopic)':15, 'Epilepsy':16, 'Fibroids':17, 'Food poisoning':18, 'Gastroenteritis':19, 'Genital herpes':20, 'Glaucoma':21, 'Hepatitis B':22, 'Impetigo':23, 'Inflammatory bowel disease':24, 'Irritable bowel syndrome (IBS)':25, 'Malaria':26, 'Mastitis':27, 'Measles':28, 'Migraine':29, 'Mumps':30, 'Osteoarthritis':31, 'Pneumonia':32, 'Postpartum psychosis (psychosis after childbirth)':33, 'Pre-eclampsia':34, 'Rabies':35, 'Rheumatic fever -Children':36, 'Rickets and osteomalacia- children':37, 'Rubella':38, 'Scabies':39, 'Scarlet fever':40,}},inplace=True)

# print(df.head())
print(" done with the reading of the Training.csv file  ")
X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
print(" done with the reading of Testing.csv file ")
tr.replace({'prognosis':{'Alcohol-related liver disease':0, 'Appendicitis':1, 'Asthma':2, 'Carbon monoxide poisoning':3, 'Cerebral palsy':4, 'Chickenpox':5, 'Chronic obstructive pulmonary disease (COPD)':6, 'Common cold':7, 'Congenital heart disease-Infants':8, 'Dementia':9, 'Dengue fever':10, 'Diabetic retinopathy':11, 'Diarrhoea':12, 'Dystonia':13, 'Ebola virus disease':14, 'Eczema (atopic)':15, 'Epilepsy':16, 'Fibroids':17, 'Food poisoning':18, 'Gastroenteritis':19, 'Genital herpes':20, 'Glaucoma':21, 'Hepatitis B':22, 'Impetigo':23, 'Inflammatory bowel disease':24, 'Irritable bowel syndrome (IBS)':25, 'Malaria':26, 'Mastitis':27, 'Measles':28, 'Migraine':29, 'Mumps':30, 'Osteoarthritis':31, 'Pneumonia':32, 'Postpartum psychosis (psychosis after childbirth)':33, 'Pre-eclampsia':34, 'Rabies':35, 'Rheumatic fever -Children':36, 'Rickets and osteomalacia- children':37, 'Rubella':38, 'Scabies':39, 'Scarlet fever':40, 'Schizophrenia':41, 'Sickle cell disease (sickle cell anaemia)':42, 'Tetanus':43, 'neonatal tetanus - tetanus':44,}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------
print(" Done with the initial assignment of variables , i hope they are not problematic ")
def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
    print("decision tree function over")

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")
    print("second  function over")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")
    print("Naives bayes function has to get over here ")
# gui_stuff------------------------------------------------------------------------------------

root = Tk()
root.configure(background='white')

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()
Age=StringVar()
Sex=StringVar()
Adult=StringVar()
FamilyHistory=StringVar()
print(" all right till adding symptom variables ")
# Heading
w2 = Label(root, justify=LEFT, text="Disease Prediction", fg="black", bg="white")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)
print(" all right till the w2 grid ")
# labels
NameLb = Label(root, text="Name of the Patient", fg="black", bg="white")
NameLb.grid(row=6, column=0, pady=15, sticky=W)

AgeLb = Label(root, text="Age of the Patient", fg="black", bg="white")
AgeLb.grid(row=8, column=5, pady=15, sticky=W)

SexLb=Label(root, text="Sex of the Patient", fg="black", bg="white")
SexLb.grid(row=6, column=5, pady=15, sticky=W)

AdultLb=Label(root, text="Adult/Child", fg="black", bg="white")
AdultLb.grid(row=7, column=5, pady=15, sticky=W)

S1Lb = Label(root, text="Symptom 1", fg="black", bg="white")
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="black", bg="white")
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="black", bg="white")
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="black", bg="white")
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="black", bg="white")
S5Lb.grid(row=11, column=0, pady=10, sticky=W)


lrLb = Label(root, text="DecisionTree", fg="white", bg="black")
lrLb.grid(row=15, column=0, pady=10,sticky=W)

destreeLb = Label(root, text="RandomForest", fg="white", bg="black")
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="white", bg="black")
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

# entries
OPTIONS = sorted(l1)
Sex_options=sorted(l_sex)
adult_options=sorted(l_adults)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

adult = OptionMenu(root, Adult,*adult_options)
adult.grid(row=7, column=3)

Sex_options = OptionMenu(root, Sex,*Sex_options)
Sex_options.grid(row=6, column=3)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=1)


dst = Button(root, text="DecisionTree", command=DecisionTree,bg="black",fg="white")
dst.grid(row=8, column=3,padx=10)

rnf = Button(root, text="Randomforest", command=randomforest,bg="black",fg="white")
rnf.grid(row=9, column=3,padx=10)

lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="black",fg="white")
lr.grid(row=10, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="white",fg="white")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="white",fg="white")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="white",fg="white")
t3.grid(row=19, column=1 , padx=10)
print(" the problem is not here till t3, maybe time required is much high")
root.mainloop()
print(" i hope the problem is not with the root.mainloop ")


# In[ ]:





# In[ ]:




