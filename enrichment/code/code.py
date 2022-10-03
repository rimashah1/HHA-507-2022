import pandas as pd 

########################
### load in the data 
########################
patients = pd.read_csv('example_data\csv\patients.csv')
patients

medications = pd.read_csv('example_data\csv\medications.csv')

patients.columns
medications.columns

patients['Id']
medications['PATIENT']


########################
### merge examples 
# add medications to patients
########################
patients_simple = patients[['Id', 'SSN']] # only print some columns
medications_simple = medications[['PATIENT', 'DESCRIPTION']]

patients_medications = patients_simple.merge(medications_simple, 
            how='left', 
            left_on='Id', right_on='PATIENT')

print(patients_medications.head(5).to_markdown()) # only print first 5 rows

patients_medications = patients_medications.drop(columns=['PATIENT'])



###### add patient data to medications table
patients_small = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]
print(patients_small.sample(10).to_markdown()) # random sample of 10 rows

medications_small = medications[['PATIENT', 'CODE', 'DESCRIPTION', 'BASE_COST']]
print(medications_small.sample(10).to_markdown()) # random sample of 10 rows
# some editing

# merge datasets. left_on equals name of key (data that is shared in both datasets) in left dataset
combined = medications_small.merge(patients_small, how='left', left_on='PATIENT', right_on='Id')



################
####### merging 3 datasets together
#################

payers = pd.read_csv('example_data\csv\payers.csv')
payers.shape
payers.head


med = medications[['PATIENT', 'PAYER']]
pay = payers[['Id', 'CITY']]
pay.rename(columns={'CITY':'CITY_PAYER'}, inplace=True)

patient = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]

##### first merge
med_pay = med.merge(pay, how='left', left_on='PAYER', right_on='Id')
med_pay = med_pay.drop(columns=('Id')) #drop duplicate

#drop duplicate rows based on patient
med_pay_nodups = med_pay.drop_duplicates(subset=['PATIENT'])
med_pay_nodups = med_pay_nodups.drop(columns=(['CODE']))

#add to patient dataset
final_df = patient.merge(med_pay_nodups, how='left', left_on='Id', right_on='PAYER')

patients_payers = patients_small.merge(payers_small, how='left', left_on='Id', right_on='Id')
# can say on='Id' if the key names are the same

########################
### concat examples 
########################

patient_sample_1 = patients.sample(n=10)
patient_sample_2 = patients.sample(n=10)

patients_s1_s2_concat = pd.concat([patient_sample_1, patient_sample_2])