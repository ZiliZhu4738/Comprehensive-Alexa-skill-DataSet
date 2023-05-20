import pandas as pd

# 定义要检查的列
columns_to_check = ['Invocation_name', 'Developer_privacy_policy', 'Developer_terms_of_use']

# 定义要处理的Excel文件列表
files_to_process = ['AU_market_skills.xlsx', 'US_market_skills.xlsx', 'UK_market_skills.xlsx']

for file in files_to_process:
    # 读取Excel文件
    df = pd.read_excel(file)

    # 替换指定列中的空值
    for column in columns_to_check:
        if column in df.columns:
            df[column] = df[column].fillna('Not Exist')

    # 保存到Excel文件
    df.to_excel(file, index=False)

print('Processing complete!')
