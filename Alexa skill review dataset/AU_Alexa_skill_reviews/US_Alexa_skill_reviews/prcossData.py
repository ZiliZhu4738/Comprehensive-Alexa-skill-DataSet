import os
import pandas as pd
import zipfile

# 读取Excel文件
df = pd.read_excel('AU_reviews.xlsx')

# 将数据按照'Asin'列拆分
grouped = df.groupby('Asin')

os.makedirs('output', exist_ok=True)

zip_index = 1
xlsx_files = []

for name, group in grouped:
    filename = f'output/{name}.xlsx'
    group.to_excel(filename, index=False)
    xlsx_files.append(filename)
    
    # 每100个xlsx文件打包成一个zip文件
    if len(xlsx_files) == 100:
        with zipfile.ZipFile(f'REVIEW_{zip_index}.zip', 'w') as zipf:
            for f in xlsx_files:
                zipf.write(f)
        xlsx_files = []
        zip_index += 1

# 处理剩余的xlsx文件
if xlsx_files:
    with zipfile.ZipFile(f'REVIEW_{zip_index}.zip', 'w') as zipf:
        for f in xlsx_files:
            zipf.write(f)
