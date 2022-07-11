import csv, ast, psycopg2
TableDict = {'d_billing_cycle':'billing_cycle',
             'd_customer_account_barring_status':'cust_acct_barring_stat',
             'd_customer_account_barring_status':'cust_acct_barring_stat',
             'd_customer_account_status':'cust_acct_stat',
             'd_customer_account_status_reason':'cust_acct_stat_rsn',
             'd_workforce_category':'workforce_cat',
             'd_workforce_status':'workforce_stat',
             'd_bill_format':'bill_format',
             'd_credit_rating':'credit_rating',
             'd_portfolio':'portfolio',
             'd_partner':'partner',
             'd_organization':'organization',
             'd_payment_method':'pymt_meth',
             'd_workforce_assignment':'workforce',
             'd_tax_rate':'tax_rate',
             'd_customer':'cust'
}

DUMMY_KEY = "to_hex(sha256('*NA'))"
DUMMY_VALUE = '*NA'
PROJECT_ID = 'project-id'
EIM_INTEG_DB = 'data-set-name'
DUMMY_START_DATE ='1900-01-01'
DUMMY_END_DATE='9999-12-31'
END_DTTM='23:59:59'
MIGRATION_CUTOFF_DATE='2021-11-14'
PROCESING_DATE='2021-11-14'
MIGRATION_ID='HDM-10001-00'
DUMMY_VALUE_LIST = ['Manager','Team']

f = open("insert_dummy_record.sql", "w")

for key in TableDict:
    print('#'+key,'-->', TableDict[key])
    if ( key in ['d_portfolio','d_workforce_category']):
        for DV in DUMMY_VALUE_LIST:
            print("###########DUMMY_VALUE###############"+DV)
            delete_query = f"""delete from {PROJECT_ID}.{EIM_INTEG_DB}.{key} where insert_load_id='{MIGRATION_ID}';"""
            f.write(delete_query)
            f.write('\n')
            insert_query = f"""insert into {PROJECT_ID}.{EIM_INTEG_DB}.{key}(dw_unit_{TableDict[key]},dw_{TableDict[key]}_id,
                            {TableDict[key]}_ss_cd,{TableDict[key]}_ss_name,ss_cd,start_dttm,end_dttm,{TableDict[key]}_cd,{TableDict[key]}_name,extraction_dttm,
                            load_dttm,update_dttm,insert_load_id,update_load_id)
                            values(to_hex(sha256('{DV}'||'||'||cast('{DUMMY_START_DATE}' as timestamp))),to_hex(sha256('{DV}')),
                            '{DV}','{DV}','{DV}',cast('{DUMMY_START_DATE}' as timestamp),
                            cast('{DUMMY_END_DATE}'||' '||'{END_DTTM}' as timestamp),
                            '{DV}','{DV}',cast('{MIGRATION_CUTOFF_DATE}' as TIMESTAMP),
                            cast('{PROCESING_DATE}' as TIMESTAMP),
                            cast('{PROCESING_DATE}' as TIMESTAMP),
                            '{MIGRATION_ID}',
                            '{MIGRATION_ID}');"""
            f.write(insert_query)
            f.write('\n')
        continue
    elif(key=='d_tax_rate'):

            delete_query = f"""delete from {PROJECT_ID}.{EIM_INTEG_DB}.{key} where insert_load_id='{MIGRATION_ID}';"""
            f.write(delete_query)
            f.write('\n')
            insert_query = f"""insert into {PROJECT_ID}.{EIM_INTEG_DB}.{key}(dw_unit_{TableDict[key]},dw_{TableDict[key]}_id,
                {TableDict[key]}_ss_cd,{TableDict[key]}_ss_name,tax_rate,ss_cd,start_dttm,end_dttm,{TableDict[key]}_cd,{TableDict[key]}_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('{DUMMY_VALUE}'||'||'||cast('{DUMMY_START_DATE}' as timestamp))),{DUMMY_KEY},
                '{DUMMY_VALUE}','{DUMMY_VALUE}','{DUMMY_VALUE}',cast('{DUMMY_START_DATE}' as timestamp),
                cast('{DUMMY_END_DATE}'||' '||'{END_DTTM}' as timestamp),
                '{DUMMY_VALUE}','{DUMMY_VALUE}',20,cast('{MIGRATION_CUTOFF_DATE}' as TIMESTAMP),
                cast('{PROCESING_DATE}' as TIMESTAMP),
                cast('{PROCESING_DATE}' as TIMESTAMP),
                '{MIGRATION_ID}',
                '{MIGRATION_ID}');"""
    else:
            delete_query = f"""delete from {PROJECT_ID}.{EIM_INTEG_DB}.{key} where insert_load_id='{MIGRATION_ID}';"""
            f.write(delete_query)
            f.write('\n')
            insert_query = f"""insert into {PROJECT_ID}.{EIM_INTEG_DB}.{key}(dw_unit_{TableDict[key]},dw_{TableDict[key]}_id,
                {TableDict[key]}_ss_cd,{TableDict[key]}_ss_name,ss_cd,start_dttm,end_dttm,{TableDict[key]}_cd,{TableDict[key]}_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('{DUMMY_VALUE}'||'||'||cast('{DUMMY_START_DATE}' as timestamp))),{DUMMY_KEY},
                '{DUMMY_VALUE}','{DUMMY_VALUE}','{DUMMY_VALUE}',cast('{DUMMY_START_DATE}' as timestamp),
                cast('{DUMMY_END_DATE}'||' '||'{END_DTTM}' as timestamp),
                '{DUMMY_VALUE}','{DUMMY_VALUE}',cast('{MIGRATION_CUTOFF_DATE}' as TIMESTAMP),
                cast('{PROCESING_DATE}' as TIMESTAMP),
                cast('{PROCESING_DATE}' as TIMESTAMP),
                '{MIGRATION_ID}',
                '{MIGRATION_ID}');"""
    f.write(insert_query)
    f.write('\n')
f.close()



