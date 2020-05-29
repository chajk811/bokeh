## 특정값 추출하기
import pandas as pd
df = pd.DataFrame({'id': ['a', 'b', 'c', 'd', 'e', 'f'], 'var': [1, 2, 3, 4, 5, 6]})
print(df)

# 'id' 칼럼에 'b'나 'e'가 들어있거나, 혹은(OR) 'var' 칼럼에 1이 들어있는 행 가져오기
df_1 = df[df['id'].isin(['b', 'e']) | df['var'].isin([1])]
print(df_1)

df_2 = df[(df['id'] == 'b') | (df['id'] == 'e') | (df['var'] == 1)]
print(df_2)