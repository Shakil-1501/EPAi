# Session 5 
&nbsp;
---
## Objective
- Write a function which gives out average run time per call, such that it's definition is:

def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

We should be able to call it like this:

- time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
- time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
- time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
- time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
- time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph  
 
- It implements these functions (with exactly the same names) 
&nbsp;
``` html 
    temp_convertor,polygon_area,squared_power_list,speed_convertor,
                            time_it,print
                            
                            
                          

```
&nbsp;
- Write a test file, that tests all of the functions mentioned above + the other basic ones 
- Test file must contain at least 25 tests

---
&nbsp;
## Files
 - Test File : [PyTest file]()
 - Code: [Method Implemantation]()
 - colab File: [![a](https://github.com/jagatabhay/TSAI/blob/master/openincolablogo.JPG)]()
&nbsp;
---
&nbsp;
## Test Cases Results
| Serial No  | Test Case | Result |
| ---------- | --------- | ------ |
| 1 | README File Exists | Pass |
| 2 | RREADME Words Counts | Pass |
| 3 | README proper description | Pass |
| 4 | RREADME Formatting | Pass |
| 5 | Proper identation and  PEP8 guidelines | Pass |
| 6 | Function name not defined with capital letters | Pass |
| 7 | test_temp_convertor_to_cn | Pass |
| 8 | test_polygon_area | Pass |
| 9 | test_squared_power_list | Pass |
| 10 | test_speed_convertor | Pass | 

---

### Author Info
- Email :
- Linkedin :

