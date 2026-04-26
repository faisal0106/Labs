import pandas as pd
import matplotlib.pyplot as plt
data = {
	'Marks' : [60,70,80,90,100],
	'Students' : [12,9,7,6,3]
}
df = pd.DataFrame(data)
print(df)
print(df.describe())
plt.bar(df['Marks'],df['Students'])
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.title("Marks Distribution")
plt.show()
