import os
import pandas as pd
import numpy as np
def operation (f1):
    os.chdir("C:\\Users\\Arjun\\Desktop\\PLACEMENTS_ARJUN\\3rd iteration")
    cwd = os.getcwd()
    #set path
    MD=cwd+"\\MASTER DATA\\"
    f1=f1.drop(columns=['Timestamp','Username'])#droptimestamp and mail ID
    l=len(f1.columns)
    a1=f1.iloc[:,3:l]
    a1.set_index(f1.Reg_Number,inplace=True)
    s=f1.Specialization.unique().tolist()
    c=f1.Campus.unique().tolist()
    #print("The campuses applied for the company {0} are {1} :".format(file_name_input,c),'\n')
    ############################################################################
    col=[]
    num=[]
    #dynamic dataframe using dictionary    
    d={elem :pd.DataFrame() for elem in c}
    for i in range(len(c)):
        d[c[i]]=f1[f1.Campus == c[i]]
        col.append(d[c[i]].Specialization.unique())#to get name of unique spl in campus
        num.append(len(d[c[i]].Specialization.unique()))#to get number of unique spl in campus
    #create a data frame to find the #of unique spl in  each campus.
    f2=pd.DataFrame(d.keys())
    f2.columns=['Campus']
    f2.insert(1,'Specialization',col)
    f2.insert(2,'Count',num)
    #finding spl from each
    spl=[]
    for co in range(len(f2)):
        print('\n')
        for x in range(f2.Count[co]):
            slist=f2.Campus[co],d[c[co]].Specialization.unique()[x]
            spl.append(slist)
            #print(f2.Campus[co],d[c[co]].Specialization.unique()[x])
    ############################################################################
    #CORE
    Student_details=pd.DataFrame()
    for i in range(len(s)):
        file_p_f=os.path.join(MD,s[i]+'.xlsx') 
        f3=pd.read_excel(file_p_f,sep='\t',header=0)#read master data
        f3.set_index(f3.Reg_Number,inplace=True)
        f4=f1[f1['Specialization']==s[i]]
        f4.set_index(f4.Reg_Number,inplace=True)
        #df=f3[f4.index.isin(f3.index)]
        df = f3.loc[f3.index & f4.index]
        df = df.loc[np.intersect1d(f3.index, f4.index)]
        df = df.loc[f3.index.intersection(f4.index)]
        #Student_details=pd.DataFrame(df)
        Student_details=Student_details.append(df,ignore_index=True)
    Student_details=Student_details.drop(columns=['SI No'])
    #adding resume and role
    #to add role prefernce according to the input given
    l1=len(a1.columns)
    l2=len(Student_details.columns)
    for i in range(l-4):
        Student_details[i]='' 
    Student_details["Resume"]=''
    if l-3== 2:#for 1 job pref
        for i in range(len(a1)):
            for q in range(len(Student_details)):
                if a1.index[i] == Student_details['Reg_Number'][q]:
                    Student_details.iat[q,l2]=a1.iloc[i,0]
                    Student_details.iat[q,l2+1]=a1.iloc[i,1]
        Student_details=Student_details.rename(columns={0:'Role Preference 1'})
    elif l-3== 3:# for 2 job pref
        for i in range(len(a1)):
            for q in range(len(Student_details)):
                if a1.index[i] == Student_details['Reg_Number'][q]:
                    Student_details.iat[q,l2]=a1.iloc[i,0]
                    Student_details.iat[q,l2+1]=a1.iloc[i,1]
                    Student_details.iat[q,l2+2]=a1.iloc[i,2]
        Student_details=Student_details.rename(columns={0:'Role Preference 1',1:'Role preference 2'})
    elif l-3== 4:#for 3 job pref
        for i in range(len(a1)):
            for q in range(len(Student_details)):
                if a1.index[i] == Student_details['Reg_Number'][q]:
                    Student_details.iat[q,l2]=a1.iloc[i,0]
                    Student_details.iat[q,l2+1]=a1.iloc[i,1]
                    Student_details.iat[q,l2+2]=a1.iloc[i,2]
                    Student_details.iat[q,l2+3]=a1.iloc[i,3]
        Student_details=Student_details.rename(columns={0:'Role Preference 1',1:'Role preference 2'
                                                    ,2:'Role Preference 3'})
    else:
        print("Can't operate for roles more than 3")
    print(spl)
    print(Student_details)
    ht=Student_details.to_html()
    os.chdir(cwd+"\\templates")
    text_file = open("index1.html", "w")
    text_file.write(ht)
    text_file.close()
    
    
    
    
    
    
    
