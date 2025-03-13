#Data cleaning 
df.isna().sum()
df[‘City/Town’].fillna(df[‘City/Town’]mode[0],inplace=True)
df[‘State/Province/Region Name’].fillna(df[‘State/Province/Region’].mode()[0],inplace=True)
df[‘State/Province/Region Code’].fillna(df[‘State/Province/Region Code’].mode()[0],inplace=True)
df[‘Business Size’].fillna(df[‘Business Size’].interpolate(),inplace=True)
#to check for any missing values
df[df.isna().any(axis=1)]
s=df[df[‘Region Name’]==‘AFRICA’]
s[(s[‘Guarantee Country Name’]==‘Africa Region Funded Activities’) | (s[‘Guarantee Country Name ‘]==‘Worldwide’)].value_country(‘State/Province/Region Country Name’)
s.loc[s[‘State/Province/Region Country Name’]== ‘Zambia’,‘Guarantee Country Name’]=‘Zambia’ s[(s[‘Guarantee Country Name’]==‘Africa Region Funded Activities’) | (s[‘Guarantee Country Name’]==‘Worldwide’)]=m.value_counts(‘State/Province/RegionCountry Name’)

#Country vs Amount 
Ken=s.groupby(‘Guarantee Country Name’)[‘Amount (USD)’].sum().sort_values(ascending=False).reset_index().head(10)
Ken.plot(kind=‘bad’,figsize=(10,6))
Plt.title (‘country vs amount’)
Plt.xlabel(‘Amount’) 
Plt.ylabel(‘country’) 
Plt.show()
#business sector with most amount 
s.groupby(‘Business Sector’)[‘Amount (USD)’].sum().sort_values(ascending=False).reset_index()
#days in between disbursement and end date 
s[‘Disbursement date’]=pd.to_datetime(s[‘Disbursement Date’])
s[‘End date’]=pd.to_datetime(s[‘End date’])
s[‘days_between’]=(s[‘End Date’]-s[‘Disbursement Date’]).dt.days 
s[‘days_between’].describe().reset_index()
do=s[s[‘Guarantee Country Name’]=‘Nigeria’]
ik.plot(kind=‘bar’,color=‘Orange’,figsize=(10,6))
plt.title(‘gender gap’)
plt.xlabel(‘gender’)
plt.ylabel(‘frequency’)
plt.show()

#first time borrowers 
cu=plot(kind=‘bar’, color=‘Green’,figsize=(10,6))
plt.title(‘first time borrowers’)
plt.xlabel(‘yes or no’) 
plt.ylabel(‘frequency’)
plt.show()

#correlation between business size and days_between 
business_size_cats=pd.categorical(s[‘Business Size’],categories=[‘1–5’, ‘6–10’,11–50,’51–100’,’>100’],ordered=True)
s[‘business_size_code’]=business_size_cats.codes 
correlation=s[‘business_size_code’].corr(s[‘days_between’])
print(correlation) 