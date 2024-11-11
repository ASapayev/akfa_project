
import pandas as pd
import asyncio
import aiohttp

# Create session asynchronously
async def create_session(url):
    session = aiohttp.ClientSession()  # Create session without using async with
    login_data = {
        'login': 'Mexrillayev',  
        'password': 'qwerty3'   
    }
    response = await session.post(url, data=login_data)
    # Do not close the session here
    return session  

# Base URL for login and data requests
base_url = 'http://test.app.akfa.onlinesavdo.com'

# The main function that will manage the session and call other functions
async def main():
    # Create session
    import time
    start = time.time()
    session = await create_session(f'{base_url}/auth/login')
    
    # Call the function to check items from Savdo with the session
    result = await check_item_from_savdo(session)
    end = time.time()
    over = end - start
    print(result,over)

# URL for the AJAX endpoint
url = 'http://test.app.akfa.onlinesavdo.com/ajax-goods-datagrid'

# Function to format data and get requests from Savdo
async def format_to_online(session, df):
    tasks = []  # This will store all the requests
    
    # Loop through each row in the DataFrame and create the GET request
    for key, row in df.iterrows():
        params = {
            'page': 1,
            'rows': 50,
            'sort': 'id',
            'order': 'asc',
            'filterRules': f'[{{"field":"name","op":"contains","value":"{row["Название"]}"}}]'
        }
        tasks.append(session.get(url, params=params))  # Append the request to tasks
    return tasks  # Return the tasks to be awaited later

# Function to check items from Savdo using the session
async def check_item_from_savdo(session):
    # Read the Excel file
    df = pd.read_excel(r'D:\Users\Muzaffar.Tursunov\Desktop\Алю_профиль_создание_ОЗМ_Савдо_87_3.xlsx', header=0, sheet_name='Алюмин Навои Жомий')
    df = df[~df['Название системы'].isnull()]  # Remove rows with null system names
    df = df.astype(str)  # Ensure all data is string type for consistency
    
    # Get all tasks to fetch data for each row
    form_response = await format_to_online(session, df)
    
    # Await all the tasks concurrently using asyncio.gather
    responses = await asyncio.gather(*form_response)
    
    results = []  # Store the results
    
    # Loop through all responses and extract the relevant data
    for res in responses:
        data = await res.json()  # Convert the response to JSON
        if 'rows' in data:
            results.extend(data['rows'])  # Add rows from each response to result
    
    ff = [[],[]]
    for ress in results:
        if 'name' in ress:
            ff[0].append(ress['id'])
            ff[1].append(ress['name'])
    
    new_df = pd.DataFrame({'ID':ff[0],'NAME':ff[1]})
    new_df.to_excel('newwwww.xlsx',index=False)

    return results  # Return the accumulated results

# Run the main function asynchronously
asyncio.run(main())
