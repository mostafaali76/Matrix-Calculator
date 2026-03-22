import pandas as pd
#let python read the titanic data set
titanic=pd.read_csv(r"D:\Hello IEEE\Code 2\titanic.csv")

#understanding DataFrame:
#Step 1:Exploring generally  
# the head 
print(titanic.head())
#general info to know the type and more
print(titanic.info())
#General description
print(titanic.describe())
#exploring the end 
print(titanic.tail())
#Since that our heads and tails seem to be a bit biased, so we'll take a random sample
#Random Sample
print(titanic.sample(n=20, random_state=42))
#Data cleaning:
#Firstly, we take a copy of the original titanic DataFrame, so our asdjustments don't affect the original one
titanic1=titanic.copy()
titanic1.info()
#Secondly, we check the data types one by one till we know the proper dtype, then we convert the required types to the correct ones at once cummulatively
print(titanic1.dtypes)
#learning correct dtype for each column:
#1-Age, Fare
#Checking the decimals in the columns: 
print(titanic1[["Age","Fare"]][titanic1[["Age", "Fare"]]%1!=0].describe()) # we have 25 decimal-count for Age and 730 Decimal -count for Fare 
#so we'll keep them as floats, but we'll convert Age and Fare from float64 to float16 to save memory
#2-SibSp, Parch
#we knpow it's int64 but let's check the range (min -max) so we can see a convenience of types
#checking the min and max
print(titanic1[["SibSp", "Parch"]].describe()) #the max is 8 and 6 for SibSp and Parch Respectively
#therefore, they're both discrete and of a range between -128-127 , i.e int8 range
#So, the proper dtype for SibSp and Parch is int8
#3- Survived, Pclass:
#checking the min and max
print(titanic1[["Survived", "Pclass"]].describe()) # The range is between 0 and 3 
#so we'll convert "Survived", "Pclass" to int8
#3-PassengerID:
#Since that PassengerID is an identifier and personally, I don't need it at the moment for math
#Therefore, we'll convert PassengerID into Category
#Same for str dtypes like Name, Sex, Embarked, Ticket, and Cabin to save memory

#converting all the data types for each column all at once
titanic1=titanic1.astype({ "Age":"float16",
                          "Fare":"float16",
                          "SibSp":"int8",
                          "Parch": "int8",
                          "Survived":"int8",
                          "Pclass":"int8",
                          "PassengerId":"category",
                          "Name":"category",
                          "Sex":"category",
                          "Ticket":"category",
                          "Embarked":"category",
                          "Cabin":"category"})
#Check our new dtypes:
titanic1.info()
#Look for troublemakers
#Looking for Duplicated values
print(titanic1.duplicated().sum()) #No Duplicates
#Nulls:
#Check the number of nulls in each column
print(titanic1.isnull().sum())  #{Age:177 , Cabin: 687, Embarked:2} nulls
#EDA:
#1-the avarage of survivers per class:

survived_pclass=titanic1.groupby("Pclass")["Survived"].mean()
print(survived_pclass*100) 
#Set the survived_pclass as a new column:
titanic1["Survival rate per class (%)"]=titanic1["Pclass"].map(survived_pclass*100)

#conclusion: The highest survivers are among the ones who booked the first class(Most Expensive one), which means the survival was kind of a function in one's ability to pay high for a good class

 #Relationship between Survivers and their class:
print(titanic1["Survived"].corr(titanic1["Pclass"])) #Negative relationship . The more the Pclass increases, the less survival probability becomes
#Conclusion:higher Pclass number = cheaper class = lower survival.

# The average of survivers among men and women :
#Groupby
survival_bygender=titanic1.groupby("Sex")["Survived"].mean()*100
#See Average survival_bygender
print(survival_bygender)
#Conclusion:The Average number of survivers among females is much higher the survival rate of males, which proves the movie plot where the males sacrified themselves for their women 
#Getting the standard deviation :
#for "Fare" column to know whether the tickets' prices vary or not 
fare_std=titanic1["Fare"].std()
#See the standard deviation for fare
print(fare_std)   #49.7 
#Conclusion from the std of fare:
#The prices of tickets vary a lot aand they target exremely different financial categories on titanic, which proves how gigantic It is.                                                 

#The relationship between survival and the number of sibling or spouses:
print(titanic1["Survived"].corr(titanic1["SibSp"])) #-0.035322498885735576
#Conclusion from the output: There is an inverse relationship that's EXTREMELY WEAK indicating that the high number of siblings or having a spouse might slightly decrease survival because of sacrifice

#I've noticed the DataFrame is a bit slow, so I'll save more memory by converting the dtype of new column
titanic1["Survival rate per class (%)"]=titanic1["Survival rate per class (%)"].astype("float16") #38KB Memory usage
#(Analysis & Insights)
# QUESTIONS:
#Q.1: what is the ratio of the total number of men to women  on Titanic?
#I tried str.contains(), but i forgot that female has also "male" element in it,
#Therefore, by using the boolean condition:
num_males=(titanic1["Sex"]=="male").sum() #577 Total number of males
num_females=(titanic1["Sex"]=="female").sum() #314 Total Number of females
#See The output
print(f"{num_males} / {num_females} = {num_males/num_females}") #1.8375796178343948
#Q.1 Answer: The ratio of the total number of males to females is 1.84 approximately, greater than 1
#which means the total number of males exceeds the total number of females slightly.
#hence The total number of males is TWO times the total number of females on titanic(by rounding)

#I've not analyzed anything related to  "Embarked" column, so we'll handle it in the following question

#Q.2: What's the embark that has the highest survival rate?
#Step 1:we check the number of nulls firstly in both fatures, so we can get accurate results or clean ones
print(titanic1[["Survived", "Embarked"]].isna().sum()) #Only "Embarked "column has nulls(2 nulls)
#Since that we've a few nulls that can be neglected
#therefore:
#Step 2: Dropping nulls from "Embarked"
titanic1=titanic1.dropna(subset=["Embarked"])
#Step 3:Check the no. of nulls and drop them
print(titanic1["Embarked"].isna().sum()) 

#Step 4: Groupby to split the embarked column
embarked_survived=titanic1.groupby("Embarked")["Survived"].mean()
#Step 5: print the mean number of survivers for each embark in percentage:
print(embarked_survived*100)
#Q.2 Answer: the embark that has the highest survival rate is (C) which has  survivers of 55%

#Q.3:which combination of Pclass and Embarked had the highest survival rate among males under 18 years old(minors)?
#Step 1: Filter
minor_boys=titanic1[(titanic1["Sex"]=="male")&(titanic1["Age"]<18)]
#Step2: Groupby Columns ["Pclass", "Embarked"] with the ["Survived"]column
group=minor_boys.groupby(["Pclass", "Embarked"])["Survived"].agg(total_people="count", sum_survivers="sum")
print(group)
#Step 3: the mean of the combination(survival_rate)
group["Survival_rate(%)"]=group["sum_survivers"]/group["total_people"]
#Step4: select the rows with the highest survival rates(required combination)
print(group.loc[group["Survival_rate(%)"].idxmax()]) #(1, C)

#Q.3 Answer: The highest survival Rate was in The first class for the embarkation at Chenbourg (C)

#Q.4: which combination of Pclass and Embarked had the highest survival rate of the females whose ages are from 21 and 50 and their fare is between 33.0000 and 79.0000?
#Step1: filter
filtered=titanic1[(titanic1["Sex"]=="female")&(titanic1["Age"].between(21,50))&(titanic1["Fare"].between(33.0000,79.0000))]
#Step2: check if the filtered data set exists and was it a an empty dataset, we stop completeing the procedures
print(filtered) #Exists, sp we continue
#Step 3:grouby operations
gr1=filtered.groupby(["Pclass", "Embarked"])["Survived"].agg(total_num="count", add="sum", rate="mean")
#Step 4: setting a new column with the "score" through which we'll use the balanced weight method because It balances tiny groups, which we have in our case 
gr1["Score"]=gr1["rate"]*gr1["total_num"]
#Step 5: sort the maximum survival score on top of the table
gr1=gr1.sort_values(by="Score", ascending=False)
#Select the top of the table
print(gr1.iloc[0]) #(1, C)
#Q.4 Answer: Embarkation Chenbourg and the First Class among the females whose ages are from 21 and 50 and their fare is between 33.0000 and 79.0000
 #saving our new DataFrame
titanic1.to_csv(r"D:\WUDownloadCache\titanic12.csv", index=False)








