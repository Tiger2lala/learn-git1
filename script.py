import matplotlib.pyplot as plt
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from scipy import stats # Hypthesis testing 

data_df = pd.read_csv("datasets/data.csv")

data_df.head().T
#data_df.info()
data_df.diagnosis = data_df.diagnosis.apply(lambda x: 1 if x == 'M' else 0)
#data_df.info()
data_df.shape
data_df.columns
data_df = data_df.dropna(axis = 1)


B, M = data_df.diagnosis.value_counts()
xtickmarks = ['B', 'M']

print(f'Number of Malignant tumours: {M}')
print(f'Number of Benign tumours   : {B}')

def createCountplot():
    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot()

    sns.set_theme(style = 'whitegrid')

    sns.countplot(data = data_df, 
              x = data_df.diagnosis, 
              label = 'Count',
              lw = 4,
              ec = 'black').set(title = 'A count of benign and malignant tumours',
                                  xlabel = 'Diagnosis',
                                  ylabel = 'Count')

    ax.set_xticklabels(xtickmarks)
    plt.show()

createCountplot()

variables_to_omit = ['id', 'diagnosis']
input_data = data_df.drop(variables_to_omit, axis = 1)
r, c = input_data.shape
print(f'Sample size                    : {r}')
print(f'Number of independent variables: {c}')

# Make a new dataframe with only the desired feature for t test  
hypothesis_test_data = pd.DataFrame(data = data_df[['area_worst', 'diagnosis']])
hypothesis_test_data = hypothesis_test_data.set_index(Diagnosis)
t, p = stats.ttest_ind(hypothesis_test_data.loc[0], hypothesis_test_data.loc[1])
print(f'The t-value: {t}')
print(f'The p-value: {p}')
