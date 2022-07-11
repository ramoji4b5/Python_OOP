import pandas as pd

event_payment_paymentGatewayResponseCodes_type = ['AcquirerAVSResponseCode', 'AcquirerApprovalCode',
                                                  'AcquirerCVVResponseCode', 'AcquirerResponseCode']

event_payment_paymentGatewayResponseCodes_value = ['B8', 'MC0002', 'M', '100']

event_payment_paymentGatewayResponseCodes_TestCol = ['Test_Val']

event_refund_taxDetail_taxBreakdown_taxType = ['SEPTA/TAOTA', 'SEPTA/TAOTA_NEW']

event_refund_taxDetail_taxBreakdown_taxInfo_taxableAmount_value = [0, 0]

event_refund_taxDetail_taxBreakdown_taxInfo_taxAmount_value = [0, 0]

event_refund_taxDetail_taxBreakdown_taxInfo_taxAmount_unit = ['string', 'string_NEW']

event_refund_taxDetail_taxBreakdown_taxInfo_taxableAmount_unit = ['string', 'string_NEW']

event_refund_taxDetail_taxBreakdown_taxInfo_taxRate = [0.05, 0.05]

event_refund_taxDetail_taxBreakdown_taxSequence = [1, 2]

event_refund_taxDetail_taxBreakdown_taxName = ['GST', 'GST_NEW']

df_payment = pd.DataFrame()

df_payment['Rescode_type'] = event_payment_paymentGatewayResponseCodes_type

df_payment['Rescode_val'] = event_payment_paymentGatewayResponseCodes_value

df_payment['Test_Col'] = ''.join(event_payment_paymentGatewayResponseCodes_TestCol)

print('*****PAYEMENT********')

print('----COLUMN_LIST-------')

print(df_payment.columns.tolist())

print('---Data_Frame_Data----')

print(df_payment)

df_refund = pd.DataFrame()

df_refund['taxBreakdown_taxType'] = event_refund_taxDetail_taxBreakdown_taxType

df_refund['taxBreakdown_taxInfo_taxableAmount_value'] = event_refund_taxDetail_taxBreakdown_taxInfo_taxableAmount_value

df_refund['taxBreakdown_taxInfo_taxAmount_value'] = event_refund_taxDetail_taxBreakdown_taxInfo_taxAmount_value

df_refund['taxBreakdown_taxInfo_taxAmount_unit'] = event_refund_taxDetail_taxBreakdown_taxInfo_taxAmount_unit

df_refund['taxBreakdown_taxInfo_taxableAmount_unit'] = event_refund_taxDetail_taxBreakdown_taxInfo_taxableAmount_unit

df_refund['taxBreakdown_taxInfo_taxRate'] = event_refund_taxDetail_taxBreakdown_taxInfo_taxRate

df_refund['taxBreakdown_taxSequence'] = event_refund_taxDetail_taxBreakdown_taxSequence

df_refund['taxBreakdown_taxName'] = event_refund_taxDetail_taxBreakdown_taxName

print('*****REFUND********')

print('----COLUMN_LIST-------')

print(df_refund.columns.tolist())

print('---Data_Frame_Data----')

pd.set_option('display.max_columns', None)

print(df_refund)