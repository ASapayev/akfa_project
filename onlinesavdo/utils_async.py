
import pandas as pd
import asyncio
import aiohttp
from decouple import config

# Create session asynchronously
async def create_session_async(url):
    session = aiohttp.ClientSession()  # Create session without using async with
    login_data = {
        'login': config('LOGIN_SAVDO'), 
        'password': config('PASSWORD_SAVDO') 
    }
    response = await session.post(url, data=login_data)
    # Do not close the session here
    return session  

# Base URL for login and data requests
base_url = 'http://test.app.akfa.onlinesavdo.com'

# The main function that will manage the session and call other functions
async def main(df,search_multiple=False):
    # Create session
    # import time
    # start = time.time()
    session = await create_session_async(f'{base_url}/auth/login')
    
    # Call the function to check items from Savdo with the session
    try:
        result = await check_item_from_savdo_async(session,df,search_multiple)
        return result
    finally:
        await session.close()

async def main_check_sena(df):
    import time
    # start = time.time()
    session = await create_session_async(f'{base_url}/auth/login')
    
    # Call the function to check items from Savdo with the session
    result = await check_sena_async(session,df)
    # end = time.time()
    # over = end - start
    # print(result,over,'sena-checkkk')
    return result

async def main_check_savdo(df):
    import time
    start = time.time()
    session = await create_session_async(f'{base_url}/auth/login')
    
    # Call the function to check items from Savdo with the session
    result = await check_item_from_savdo_async3(session,df)
    end = time.time()
    over = end - start
    # print(result,over)
    return result

# URL for the AJAX endpoint
url = 'http://test.app.akfa.onlinesavdo.com/ajax-goods-datagrid'

# Function to format data and get requests from Savdo
async def format_to_online_async(session, df,search_multiple):
    tasks = []  # This will store all the requests
    # search_multiple =True
    # Loop through each row in the DataFrame and create the GET request
    for key, row in df.iterrows():
        if search_multiple:
            name = row["Название"]
            sapcode = row["SAP Код вручную (вставится вручную)"]
            params = {
                'page': 1,
                'rows': 50,
                'sort': 'id',
                'order': 'asc',
                'filterRules': '[{"field":"name","op":"contains","value":"'+name+'"},{"field":"sapCode","op":"contains","value":"'+sapcode+'"}]'
            }
        else:
            params = {
                'page': 1,
                'rows': 50,
                'sort': 'id',
                'order': 'asc',
                'filterRules': f'[{{"field":"name","op":"contains","value":"{row["Название"]}"}}]'
            }
        tasks.append(session.get(url, params=params))  # Append the request to tasks
    return tasks  # Return the tasks to be awaited later


async def sena_req_online_async(session, df):
    tasks = []  # This will store all the requests
    for key, row in df.iterrows():
        if row['CLIENTYPE'] =='AKFA':
            client_type = 1
        elif row['CLIENTYPE'] =='IMZO':
            client_type = 2
        elif row['CLIENTYPE'] =='FRANCHISING':
            client_type = 4
        params = {
            'clientTypeId': client_type,
            'typeStr': 'PURCHASE_RATE',
            'goodId': int(row['ID']),
            }
        url_new ='http://test.app.akfa.onlinesavdo.com/ajax-goodsRate-datagrid'
        tasks.append(session.post(url_new,params=params))
    return tasks  

# Function to check items from Savdo using the session
async def check_item_from_savdo_async(session,df,search_multiple):
    
    form_response = await format_to_online_async(session, df,search_multiple)
    responses = await asyncio.gather(*form_response)
    
    results = []  
    for res in responses:
        data = await res.json()  # Convert the response to JSON
        if 'rows' in data:
            results.extend(data['rows'])  # Add rows from each response to result
    
    last_resut ={}
    for ress in results:
        if 'name' in ress:
            last_resut[str(ress['name'])]=ress['id']

    return last_resut
  
async def check_item_from_savdo_async3(session,df,search_multiple=False):
    
    form_response = await format_to_online_async(session, df,search_multiple=True)
    responses = await asyncio.gather(*form_response)
    
    results = []  
    for res in responses:
        data = await res.json()  # Convert the response to JSON
        if 'rows' in data:
            results.extend(data['rows'])  # Add rows from each response to result
    
    last_resut ={}
    for ress in results:
        new_dict = {}
        if 'id' in ress:
            new_dict['id'] = ress['id'] 
        if 'name' in ress:
            new_dict['name'] = ress['name'] 
        
        if 'group' in ress:
            if 'name' in ress['group']:
                new_dict['group_name'] = ress['group']['name'] 
            else:
                new_dict['group_name'] =''
        else:
            new_dict['group_name']=''

        if 'sapCode' in ress:
            new_dict['sapCode']= ress['sapCode']
        else:
            new_dict['sapCode']='' 
        
        if 'alternateUnitVal' in ress:
            new_dict['alternateUnitVal']=ress['alternateUnitVal']
        else:
           new_dict['alternateUnitVal']=''
        
        if 'purchasingGroup' in ress:
            if 'name' in ress['purchasingGroup']:
                new_dict['purchasingGroup_name']=(ress['purchasingGroup']['name'])
            else:
                new_dict['purchasingGroup_name']=''
        else:
            new_dict['purchasingGroup_name']=''

        if 'segment' in ress:
            if 'name' in ress['segment']:
                new_dict['segment_name'] = ress['segment']['name']
            else:
                new_dict['segment_name'] = ''
        else:
            new_dict['segment_name'] = ''

        if 'accountingGoods' in ress:
            if isinstance(ress['accountingGoods'],dict) and 'name' in ress['accountingGoods']:
                new_dict['accountingGoods_name'] = ress['accountingGoods']['name']
            else:
                new_dict['accountingGoods_name'] =''
        else:
            new_dict['accountingGoods_name'] = ''

        if 'factory' in ress:
            if 'name' in ress['factory']:
                new_dict['factory_name'] = ress['factory']['name']
            else:
                new_dict['factory_name'] = ''
        else:
            new_dict['factory_name'] = ''

        # if 'name' in ress:
        last_resut[str(ress['name']).lower()]=new_dict

    return last_resut  


async def check_sena_async(session,df):
    
    form_response = await sena_req_online_async(session, df)
    responses = await asyncio.gather(*form_response)
    
    results = []  
    for res in responses:
        data = await res.json()
        if 'rows' in data:
            results.extend(data['rows'])   
    
    last_resut ={}
    for ress in results:
        if len(ress) > 1:
            if 'goods' in ress:
                last_resut[int(ress['goods']['id'])]={
                    'cost':ress['cost'],
                    'rate':ress['rate'],
                    'dateStr':ress['dateStr'],
                }

    return last_resut  