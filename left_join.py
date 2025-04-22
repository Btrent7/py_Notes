import pandas as pd

master_file = r"C:\Users\btrent\OneDrive - The Reliable Automatic Sprinkler Co., Inc\Documents\Data Analysis\Data Cleaning\SKU\SKU Master\SKU MASTER.xlsx"
update_file = r"C:\Users\btrent\OneDrive - The Reliable Automatic Sprinkler Co., Inc\Documents\Data Analysis\Data Cleaning\SKU\SKU Master\update_py_file.xlsx"
updated_final = r"C:\Users\btrent\OneDrive - The Reliable Automatic Sprinkler Co., Inc\Documents\Data Analysis\Data Cleaning\SKU\SKU Master\updated_SKU.xlsx"

master = pd.read_excel(master_file)
update = pd.read_excel(update_file)

#Left join tables
master_update = master.merge(update[['ITMID', 'Vendor SKU']], on='ITMID', how='left', suffixes=('', '_updated'))

#Fill blank rows
master_update['Vendor SKU'] = master_update['Vendor SKU'].fillna(master_update['Vendor SKU_updated'])

#Drop SKU update column
master_update.drop(columns=['Vendor SKU_updated'], inplace=True) 
    # OR master_update = master_update.drop(columns=['Vendor SKU_updated'])

print(master_update)

# Send DataFrame to new excel sheet
master_update.to_excel(updated_final, index=False)
