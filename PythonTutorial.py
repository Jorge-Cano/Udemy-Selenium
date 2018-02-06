from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")

# get the search text box
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium Webdriver Python Projects + Node")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elemets_by_classname method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + "searches:")

# iterate through each elements and print the text that is
# name of the search

i=0
for listitem in lists:
    print (listitem)
    i=i+1
    if(i>10):
        break

#close the browser window
driver.quit()



# end of requirement

# a = "NYC"
# b = "Austin"
# distance = "1,599"
#
# print(a + " is your starting point.")
# print (b + " is your destination point")
# print ("The total distance from " + a + " to " + b + " is approxmiately " + distance + " miles.")
#
# for x in xrange(3):
#     print x
# else:
#     print 'Final x = %d' % (x)

# for x in xrange(16):
#     print x
# else:
#     print 'Final X = %d' % (x)


# for x in xrange(1, 16):
#     for y in xrange(1, 21):
#         print '%d * %d = %d' % (x, y, x*y)

# list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for list in list_of_lists:
#     for x in list:
#         print x
