I have a little bit of extra time so i will try to analyze this function for time/space complexity 

Time Complexity :

this function is recursively called once for each unique pair of letters within s1 and s2 so basically if s1 is dog and s2 is cat we are getting all of the following calls:

help(d,c)
help(d,a)
help(d,t)

help(o,c)
help(o,a)
help(o,t)

help(g,c)
help(g,a)
help(g,t)

or 9 executions. Looking at this pattern we can see that the functions time complexity will be the product of the sizes of the two inputs. so I believe this would be considered polynomial????

The function which calls this helper function is constant so this does not impact the time complexity

Space complexity :

The space complexity for this function would actually be constant because neither help nor twostring define any variables 
