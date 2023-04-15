# import matplotlib.pyplot as plt

# # input data
# dates = ['27/09/21', '27/10/21', '27/11/21']
# values = [1, 2, 3]

# # create plot
# plt.plot(dates, values)

# # set plot title and axis labels
# plt.title('Data Table')
# plt.xlabel('Date')
# plt.ylabel('Value')

# # display plot
# plt.show()

import matplotlib.pyplot as plt

# input data
dates = ['27/09/21', '27/10/21', '27/11/21', '5/01/22' , '6/01/22']
values = [1, 2, 3,4,5]

# create plot
plt.plot(dates, values)

# set plot title and axis labels
plt.title('Data Table')
plt.xlabel('Date')
plt.ylabel('Value')

# save plot as PDF file
plt.savefig('data_table.pdf')
