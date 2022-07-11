delete from project-id.data-set-name.d_billing_cycle where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_billing_cycle(dw_unit_billing_cycle,dw_billing_cycle_id,
                billing_cycle_ss_cd,billing_cycle_ss_name,ss_cd,start_dttm,end_dttm,billing_cycle_cd,billing_cycle_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_customer_account_barring_status where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_customer_account_barring_status(dw_unit_cust_acct_barring_stat,dw_cust_acct_barring_stat_id,
                cust_acct_barring_stat_ss_cd,cust_acct_barring_stat_ss_name,ss_cd,start_dttm,end_dttm,cust_acct_barring_stat_cd,cust_acct_barring_stat_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_customer_account_status where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_customer_account_status(dw_unit_cust_acct_stat,dw_cust_acct_stat_id,
                cust_acct_stat_ss_cd,cust_acct_stat_ss_name,ss_cd,start_dttm,end_dttm,cust_acct_stat_cd,cust_acct_stat_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_customer_account_status_reason where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_customer_account_status_reason(dw_unit_cust_acct_stat_rsn,dw_cust_acct_stat_rsn_id,
                cust_acct_stat_rsn_ss_cd,cust_acct_stat_rsn_ss_name,ss_cd,start_dttm,end_dttm,cust_acct_stat_rsn_cd,cust_acct_stat_rsn_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_workforce_category where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_workforce_category(dw_unit_workforce_cat,dw_workforce_cat_id,
                            workforce_cat_ss_cd,workforce_cat_ss_name,ss_cd,start_dttm,end_dttm,workforce_cat_cd,workforce_cat_name,extraction_dttm,
                            load_dttm,update_dttm,insert_load_id,update_load_id)
                            values(to_hex(sha256('Manager'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('Manager')),
                            'Manager','Manager','Manager',cast('1900-01-01' as timestamp),
                            cast('9999-12-31'||' '||'23:59:59' as timestamp),
                            'Manager','Manager',cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            'HDM-10001-00',
                            'HDM-10001-00');
delete from project-id.data-set-name.d_workforce_category where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_workforce_category(dw_unit_workforce_cat,dw_workforce_cat_id,
                            workforce_cat_ss_cd,workforce_cat_ss_name,ss_cd,start_dttm,end_dttm,workforce_cat_cd,workforce_cat_name,extraction_dttm,
                            load_dttm,update_dttm,insert_load_id,update_load_id)
                            values(to_hex(sha256('Team'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('Team')),
                            'Team','Team','Team',cast('1900-01-01' as timestamp),
                            cast('9999-12-31'||' '||'23:59:59' as timestamp),
                            'Team','Team',cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            'HDM-10001-00',
                            'HDM-10001-00');
delete from project-id.data-set-name.d_workforce_status where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_workforce_status(dw_unit_workforce_stat,dw_workforce_stat_id,
                workforce_stat_ss_cd,workforce_stat_ss_name,ss_cd,start_dttm,end_dttm,workforce_stat_cd,workforce_stat_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_bill_format where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_bill_format(dw_unit_bill_format,dw_bill_format_id,
                bill_format_ss_cd,bill_format_ss_name,ss_cd,start_dttm,end_dttm,bill_format_cd,bill_format_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_credit_rating where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_credit_rating(dw_unit_credit_rating,dw_credit_rating_id,
                credit_rating_ss_cd,credit_rating_ss_name,ss_cd,start_dttm,end_dttm,credit_rating_cd,credit_rating_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_portfolio where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_portfolio(dw_unit_portfolio,dw_portfolio_id,
                            portfolio_ss_cd,portfolio_ss_name,ss_cd,start_dttm,end_dttm,portfolio_cd,portfolio_name,extraction_dttm,
                            load_dttm,update_dttm,insert_load_id,update_load_id)
                            values(to_hex(sha256('Manager'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('Manager')),
                            'Manager','Manager','Manager',cast('1900-01-01' as timestamp),
                            cast('9999-12-31'||' '||'23:59:59' as timestamp),
                            'Manager','Manager',cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            'HDM-10001-00',
                            'HDM-10001-00');
delete from project-id.data-set-name.d_portfolio where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_portfolio(dw_unit_portfolio,dw_portfolio_id,
                            portfolio_ss_cd,portfolio_ss_name,ss_cd,start_dttm,end_dttm,portfolio_cd,portfolio_name,extraction_dttm,
                            load_dttm,update_dttm,insert_load_id,update_load_id)
                            values(to_hex(sha256('Team'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('Team')),
                            'Team','Team','Team',cast('1900-01-01' as timestamp),
                            cast('9999-12-31'||' '||'23:59:59' as timestamp),
                            'Team','Team',cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            cast('2021-11-14' as TIMESTAMP),
                            'HDM-10001-00',
                            'HDM-10001-00');
delete from project-id.data-set-name.d_partner where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_partner(dw_unit_partner,dw_partner_id,
                partner_ss_cd,partner_ss_name,ss_cd,start_dttm,end_dttm,partner_cd,partner_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_organization where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_organization(dw_unit_organization,dw_organization_id,
                organization_ss_cd,organization_ss_name,ss_cd,start_dttm,end_dttm,organization_cd,organization_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_payment_method where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_payment_method(dw_unit_pymt_meth,dw_pymt_meth_id,
                pymt_meth_ss_cd,pymt_meth_ss_name,ss_cd,start_dttm,end_dttm,pymt_meth_cd,pymt_meth_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_workforce_assignment where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_workforce_assignment(dw_unit_workforce,dw_workforce_id,
                workforce_ss_cd,workforce_ss_name,ss_cd,start_dttm,end_dttm,workforce_cd,workforce_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_tax_rate where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_tax_rate(dw_unit_tax_rate,dw_tax_rate_id,
                tax_rate_ss_cd,tax_rate_ss_name,tax_rate,ss_cd,start_dttm,end_dttm,tax_rate_cd,tax_rate_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',20,cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
delete from project-id.data-set-name.d_customer where insert_load_id='HDM-10001-00';
insert into project-id.data-set-name.d_customer(dw_unit_cust,dw_cust_id,
                cust_ss_cd,cust_ss_name,ss_cd,start_dttm,end_dttm,cust_cd,cust_name,extraction_dttm,
                load_dttm,update_dttm,insert_load_id,update_load_id)
                values(to_hex(sha256('*NA'||'||'||cast('1900-01-01' as timestamp))),to_hex(sha256('*NA')),
                '*NA','*NA','*NA',cast('1900-01-01' as timestamp),
                cast('9999-12-31'||' '||'23:59:59' as timestamp),
                '*NA','*NA',cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                cast('2021-11-14' as TIMESTAMP),
                'HDM-10001-00',
                'HDM-10001-00');
