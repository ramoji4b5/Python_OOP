# -*- coding: utf-8 -*-
# code/pseudcode for ddl generation

'''
command to run this script: python eim_ddl_generator.py "<project_id>" "<ds_name>" "<table_name>"
Ex: python eim_ddl_generator.py "vf-uk-datahub" "vfuk_dh_edw_eim_hdm_dev_01_s" "d_sim_card_association"
'''
import sys
import pandas as pd

project_id = sys.argv[1]  # "vf-uk-datahub"
dataset_name = sys.argv[2]  # "vfuk_dh_edw_eim_hdm_dev_01_s"
table_name = sys.argv[3]  # "d_sim_card_association"

mapping_doc_local_sys_path = r"D:\ACCENTURE\Vodafone\Vodafone\Account_EDW_EIM_Mapping_v0.6.1.xlsx"
#df_mapping_doc = pd.read_excel(mapping_doc_local_sys_path, sheet_name="EIM")
df_mapping_doc = pd.read_excel('D:\ACCENTURE\Vodafone\Vodafone\Account_EDW_EIM_Mapping_v0.6.1.xlsx', sheet_name="EIM",engine = 'openpyxl')
df_table_specific = df_mapping_doc.loc[
    df_mapping_doc['Parent.Code'] == table_name, ['Code', 'Data Type', 'Mandatory', 'Comment']]
# Datatype mapping info from https://cloud.google.com/bigquery-transfer/docs/teradata-migration-options#teradata_mapping
# All eim datatypes given in 'EIM' mapping sheet are covered here
td_bq_dt_mappings = {"Text": "STRING", \
                     "Date": "DATE", \
                     "Variable characters (100)": "STRING", \
                     "Variable characters (2000)": "STRING", \
                     "Short integer": "INT64", \
                     "Timestamp": "TIMESTAMP", \
                     "Variable characters (4100)": "STRING", \
                     "Variable characters (50)": "STRING", \
                     "Decimal (18,8)": "NUMERIC", \
                     "Decimal (18,4)": "NUMERIC", \
                     "Characters (20)": "STRING", \
                     "Variable characters (256)": "STRING", \
                     "Characters (1)": "STRING", \
                     "Decimal (5,2)": "NUMERIC", \
                     "Integer": "INT64", \
                     "Decimal (9,7)": "NUMERIC", \
                     "Characters (18)": "STRING", \
                     "Characters (6)": "STRING", \
                     "Decimal (12,7)": "NUMERIC", \
                     "Decimal (18,6)": "NUMERIC", \
                     "Characters (15)": "STRING", \
                     "Characters (8)": "STRING", \
                     "Variable characters (6)": "STRING", \
                     "Decimal (22,8)": "NUMERIC", \
                     "Decimal (9,2)": "NUMERIC"}

boolean_mappings = {"1.0": "NOT NULL", "0.0": ""}

ddl_sql_str = f'''CREATE TABLE {project_id}.{dataset_name}.{table_name} ( '''

for index, row in df_table_specific.iterrows():
    # cleansing attribute description
    clean_desc = row['Comment'].replace('\"', '\'').replace('\n', ' ').replace("\'", '')
    ddl_sql_str += f'''\n {row['Code']} {td_bq_dt_mappings.get(row['Data Type'])} {boolean_mappings.get(str(row['Mandatory']))} OPTIONS(description="{clean_desc}"),'''

ddl_sql_str += "\n extraction_dttm TIMESTAMP, \n load_dttm TIMESTAMP, \n update_dttm TIMESTAMP, \n insert_load_id STRING, \n update_load_id STRING );"
# print(ddl_sql_str)
_file = open(f'''hdm_eim_account_{table_name}_ddl.txt''', "w+")
_file.write(ddl_sql_str)

