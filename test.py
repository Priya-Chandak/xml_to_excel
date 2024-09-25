import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('input.xml')
root = tree.getroot()

receipt_transactions = []

for transaction in root.findall('.//VOUCHER'):
    voucher_type = transaction.find('VOUCHERTYPENAME').text
    if voucher_type == "Receipt": 
        date = transaction.find('DATE').text if transaction.find('DATE') is not None else None
        guid = transaction.find('GUID').text if transaction.find('GUID') is not None else None
        narration = transaction.find('NARRATION').text if transaction.find('NARRATION') is not None else None
        ref = transaction.find('REFERENCE').text if transaction.find('REFERENCE') is not None else None
        refdate = transaction.find('REFERENCEDATE').text if transaction.find('REFERENCEDATE') is not None else None
        vchno = transaction.find('VOUCHERNUMBER').text if transaction.find('VOUCHERNUMBER') is not None else None
        party = transaction.find('PARTYLEDGERNAME').text if transaction.find('PARTYLEDGERNAME') is not None else None

        receipt_transactions.append({
            'Date': date,
            'Guid': guid,
            'Narration': narration,
            'Reference' : ref,
            'Reference_Date' : refdate,
            'Voucher_Number' : vchno,
            'Party_Name' : party,
            'voucher_type' : 'Receipt'
        })

df_receipts = pd.DataFrame(receipt_transactions)

df_receipts.to_excel('receipt_transactions.xlsx', index=False)
