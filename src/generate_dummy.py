import pandas as pd
import numpy as np

# Gera 50 participantes fictícios
n = 50
data = {
    'Participant_ID': range(1, n+1),
    'Age': np.random.randint(18, 65, n),
    'Gender': np.random.choice(['Male', 'Female', 'Other'], n),
    'Q1_Satisfaction': np.random.randint(1, 6, n), # Nota de 1 a 5
    'Q2_Usability': np.random.randint(1, 6, n),
    'Q3_Recommend': np.random.randint(1, 6, n),
    'Response_Time_Sec': np.random.uniform(15, 250, n) # Tempo em segundos
}

df = pd.DataFrame(data)
df.to_csv('dummy_survey.csv', index=False)
print("✅ Arquivo dummy_survey.csv criado com sucesso!")