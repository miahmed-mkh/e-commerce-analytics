import pandas as pd
pd.set_option('display.max_columns', None)  
pd.set_option('display.max_rows', None)    
pd.set_option('display.width', None)        
pd.set_option('display.max_colwidth', None)

chemin = r"C:\Users\Master\Desktop\Mohamed\0 ESIS\Projects\Ecommerce_Project\0 ecommerce_transactions.csv"
df = pd.read_csv(chemin)
df['Transaction_Date']=pd.to_datetime(df['Transaction_Date'], errors='coerce')
df['Purchase_Amount'] = pd.to_numeric(df['Purchase_Amount']).astype('float32')


"""print(df.duplicated().sum())
print(df.isna().sum())"""


df['Month_year']=df['Transaction_Date'].dt.strftime('%B %Y') #créer une nouvelle colonne depuis la colonne 'Transaction_Date' qui détermine le mois et l'année de transaction

tranch = [0,18,30,45,60,100]
etiq = ["<18","18-30","30-45","45-60","60+"]
df["Age_Group"] = pd.cut(df["Age"], bins=tranch, labels=etiq, right=False) #créer une colonne 'Age_Group' où on va mentonner chaque client à quelle tranche d'age appartient
#NB : right=False ==> [0-18) ou [18-30) ....
#print(df.head())

CA_total = df["Purchase_Amount"].sum() #Chiffre d'affaire total
#print('CA_total : ', CA_total)

nb_transactions = df["Transaction_ID"].nunique() # Nombre de transactions uniques
#print('Nombre de trans : ', nb_transactions)

panier_moyen = CA_total / nb_transactions # représente la somme moyenne dépensée pour chaque commande  (il s'agit de la moyenne des totaux qu'un client dépense à chaque commande)
#print('panier_moyen : ', panier_moyen)



df['Month'] = df['Transaction_Date'].dt.to_period('M')
CA_month = df.groupby('Month')['Purchase_Amount'].sum().sort_index()
CA_df = CA_month.reset_index()
CA_df['Month'] = CA_df['Month'].dt.strftime('%B %Y')
CA_df.columns = ['Month_year', 'CA_month']
#print(CA_df)


df2= pd.DataFrame({
    'CA_total': [pd.to_numeric(CA_total)],
    'Nombre de transactions': [nb_transactions],
    'Panier moyen': [pd.to_numeric(panier_moyen)]
    
})

"""df2.to_csv("KPI.csv", index=False)

CA_df.to_csv('CA_month.csv', index=False)"""

#df.to_csv("transactions_modifier.csv", index=False)

print(df.info())