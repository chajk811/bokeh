import pandas as pd

# matplotlip 참고 : https://bcho.tistory.com/1201
# pandas 참고 : https://3months.tistory.com/292
# 판다스로 불러운 데이터는 Datafram 형식

# 처음 5개 데이터 출력
# print(data.head())

# (x, y) x개의 index, y개의 칼럼
# print(data.shape)

# index 개수 출력
# print(len(data.index))

# print(data.columns)

## Dataframe에서 특정 컬럼이나 로우(인덱스) 선택하기
# 대표적으로 iloc, loc, ix 등을 통해서 할 수 있다.
# df = pd.DataFrame({'a':[1, 4, 7], 'b':[2, 5, 8], 'c':[3, 6, 9]})
# print(df)

# row 를 선택할 때, df.ix[index]
# print(df.ix[0])

# column 을 선택할 때, df['column']
# print(df['a'])

# https://github.com/pandas-dev/pandas/blob/v0.25.3/pandas/plotting/_core.py#L504-L1533
# pandas 0.25.3 DataFrame.plot