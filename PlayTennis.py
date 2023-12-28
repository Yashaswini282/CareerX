import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create a DataFrame with the given data
data = {
    'Day': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'],
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Initialize LabelEncoders for each categorical column
label_encoders = {}
for column in ['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Print the encoded DataFrame
print(df)
df=pd.read_csv("Downloads\playtennis.csv")
df.head()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df.Day=df.fit_transform(df.Day)
df.Outlook=df.fit_transform(df.Outlook)
df.Temperature=df.fit_transform(df.Temperature)
df.Humidity=df.fit_transform(df.Humidity)
df.Wind=df.fit_transform(df.Wind)
df.PlayTennis=df.fit_transform(df.PlayTennis)
df.head()
df.describe()
df.dtypes
df['Day'].unique()
df['Outlook'].unique()
df['Temperature'].unique()
df['Humidity'].unique()
df['Wind'].unique()
df['PlayTennis'].unique()
df.head()