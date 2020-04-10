# from covid import Covid
# import matplotlib.pyplot as pyplot
#
# country = input("Enter your contry")
#
# covid = Covid()
# data = covid.get_status_by_country_name(country)
# cadr = {
#     key: data[key]
#     for key in data.keys() & {"confirmed", "active", "deaths", "recovered"}
# }
# n = list(cadr.keys())
# v = list(cadr.values())
#
# print(cadr)
#
# pyplot.title(country)
# pyplot.bar(range(len(cadr)), v, tick_label=n)
# pyplot.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import ticks as ticks
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = 'https://www.mohfw.gov.in/'
# make a GET request to fetch the raw HTML content
web_content = requests.get(url).content
# parse the html content
soup = BeautifulSoup(web_content, "html.parser")
# remove any newlines and extra spaces from left and right
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
# find all table rows and data cells within
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
# notice that the data that we require is now a list of length 5
    if len(stat) == 5:
        stats.append(stat)
#now convert the data into a pandas dataframe for further processing
new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
state_data = pd.DataFrame(data = stats, columns = new_cols)
state_data.head()

# table = PrettyTable()
# table.field_names = (new_cols)
# for i in stats:
#     table.add_row(i)
# table.add_row([“Total”,
#             sum(state_data[‘Confirmed’]),
#             sum(state_data[‘Recovered’]),
#             sum(state_data[‘Deceased’])
# print(table)

#
# sns.set_style(“ticks”)
# plt.figure(figsize = (15,10))
# plt.barh(state_data[“States/UT”],    state_data[“Confirmed”].map(int),align = ‘center’, color = ‘lightblue’, edgecolor = ‘blue’)
# plt.xlabel(‘No. of Confirmed cases’, fontsize = 18)
# plt.ylabel(‘States/UT’, fontsize = 18)
# plt.gca().invert_yaxis()
# plt.xticks(fontsize = 14)
# plt.yticks(fontsize = 14)
# plt.title(‘Total Confirmed Cases Statewise’, fontsize = 18 )
# for index, value in enumerate state_data[“Confirmed”] :
#     plt.text(value, index, str(value), fontsize = 12)
# plt.show()