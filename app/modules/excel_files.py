import pandas as pd
import modules.crud as crud

def createEvlauationsExcel():
    dfs = []
    sheets = []
    for i in range(1, 3):
        dfs.append(crud.getEvaluationsDF(i))
        sheets.append('Evaluación ' + str(i))
    with pd.ExcelWriter('data/Datos Evaluación.xlsx', engine='xlsxwriter') as excelfile:
        for i in range(len(sheets)):
            dfs[i].to_excel(excelfile, sheet_name=sheets[i], index=False)
            columnWidth = [10, 20, 10, 16, 18, 10, 10, 10, 10, 10, 10, 30]
            worksheet = excelfile.sheets[sheets[i]]
            for i in range(len(columnWidth)):
                worksheet.set_column(i, i, columnWidth[i])

def createStudentsExcel():
    df = crud.getStudentsDF()
    with pd.ExcelWriter('data/Datos Practicantes.xlsx', engine='xlsxwriter') as excelfile:
        df.to_excel(excelfile, sheet_name='Practicantes', index=False)
        columnWidth = [22, 20, 14, 5, 8, 15, 38, 12, 55, 35, 30, 18, 32, 31, 12, 47, 47, 34, 38, 21, 14, 29, 29]
        worksheet = excelfile.sheets['Practicantes']
        for i in range(len(columnWidth)):
            worksheet.set_column(i, i, columnWidth[i])

createStudentsExcel()