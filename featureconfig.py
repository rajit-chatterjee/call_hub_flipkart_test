'''
This file is the configuration file.
The user configuration for a particular test case is written here.
Change this file according to the need to test configurations.
'''

browser_details={'browser_name':"Chrome",
                 'browser_path':"C:\DRIVERS\chromedriver.exe",
                 "url":"https://www.flipkart.com/"}

user_login_details={"username":"chatterjeerajit007@gmail.com", "password":"R@jit1994!"}

elements_to_access={"Electronics_element":"//span[text()='Electronics']",
                    "Mobile_submenu_element":"//a[@href='/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles']"}
                

find_element_by={"xpath":"ByXpath",
                 "linktext":"ByLinkText",
                 "partiallink":"ByPartialLinkText",
                 "cssselector":"ByCssSelector"}

product_search={"phone":"iphone 7"}

find_product={"product_apple":"Apple iPhone 7"}

user_address_details={"zip_code":"560100"}

snap_shot_save_path={"path":"C:\\Users\\rajchatt\\Downloads\\rajit_ss.png"}