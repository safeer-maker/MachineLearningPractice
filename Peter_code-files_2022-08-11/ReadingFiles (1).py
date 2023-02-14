#!/usr/bin/env python
# coding: utf-8

# In[5]:


#importing pandas as pd
# Import writer class from csv module
from csv import writer

# List
List=[1,1,1,0]

# Open our existing CSV file in append mode
# Create a file object for this file
with open('diseaseConfiguration.csv', 'a') as f_object:

	# Pass this file object to csv.writer()
	# and get a writer object
	writer_object = writer(f_object)
    

	# Pass the list as an argument into
	# the writerow()
	writer_object.writerow(List)
    

	#Close the file object
	f_object.close()
print('done')


# In[ ]:




