'''
This file is for testing a particular scenario.
Test case description:
a) Login to flipkart.com (assume you have a login with flipkart)

b) After login, search for iPhone7 in Electronics section

c) Pick up top 25 products listed in this category and add one of the products to Shopping Cart

d) Now browse to your Cart and take a screenshot of the product that got added to your Cart

e) Remove the product from the Cart and Logout

'''

import Common_Functions.common_functions as cf
import Common_Functions.user_activities as ua
import Common_Functions.featureconfig as fc
import unittest
class test_iphone_flipkart(unittest.TestCase):
#Open browser, go to the website and login with username and password
#setting up the browser
    def test_iphone(self):
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        
        #Opening the URL
        cf.go_to_url(browser, fc.browser_details.get("url"))
        
        #click on login
        cf.click_login_signup(browser, fc.find_element_by.get("linktext"))
        
        #user logs in their flipkart account
        ua.user_login(browser, fc.find_element_by.get("xpath"), fc.user_login_details.get("username"), fc.user_login_details.get("password"))
        
        #Mouse hover on Electronics
        cf.mouse_hover_on_element(browser, fc.find_element_by.get("xpath"), fc.elements_to_access.get("Electronics_element"))
        #Clicking on Mobile sub menu
        mobile_element=cf.find_an_element(browser, fc.find_element_by.get("xpath"), fc.elements_to_access.get("Mobile_submenu_element"))
        cf.click_element(mobile_element)
        #Search for a particular element
        ua.search_product(browser, fc.product_search.get("phone"))
        #Select a product randomly from the search result
        ua.select_product_randomly(browser, fc.find_element_by.get("partiallink"), fc.find_product.get("product_apple"))
        #Switch to new tab
        cf.switch_to_new_window(browser)
        #changing the zip code
        ua.zip_code(browser, fc.user_address_details.get("zip_code"))
        #Add the item to cart
        ua.add_to_cart(browser)
        #Taking snapshot of the cart and saving it
        ua.take_snap_shot(browser, fc.snap_shot_save_path.get("path"))
        
        #removing item from cart
        ua.remove_from_cart(browser)
        #logout from account
        ua.user_logout(browser, fc.find_element_by.get("cssselector"))
        #Close browser at the end of testing
        cf.close_browser(browser, "All")







