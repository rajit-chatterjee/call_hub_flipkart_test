'''
This file contains all the user activities in flipkart like login, signup, searching a product, adding to cart etc.
According to the test case need, new user functionality can be added in the file
'''

import Common_Functions.common_functions as cf
import Common_Functions.logger_file as logger
import time
from random import randint
from selenium.webdriver.common.keys import Keys
import sys
import Common_Functions.common_elements as ce
log=logger.set_log("user_activities")
#This function is for user login with username and password
def user_login(browser, find_by, user_name, password):
    invalid_login=False
    log.info("Login button has been clicked")
    
    #Sending username and password
    element_user=browser.find_element_by_xpath(ce.username_element)
    cf.send_inputs(element_user,user_name)
    try:
        cont_btn=browser.find_element_by_xpath(ce.continue_btn_element).is_displayed()
        if cont_btn:
            cont_btn_1=browser.find_element_by_xpath(ce.continue_btn_element)
            cont_btn_1.click()
            time.sleep(3)
            try:
                login_password=browser.find_element_by_css_selector(ce.login_with_password_btn_element)
                if login_password.is_displayed():
                    login_password.click()
            except:
                log.error("Email address is not registered. Please signup")
                sys.exit()
    except:
        log.warning("continue button not found. Login with username and password")
    element_password=browser.find_element_by_xpath(ce.password_element)    
    cf.send_inputs(element_password,password)
    
    #Clicking on Login button
    try:
        element_login_btn=cf.find_an_element(browser, find_by, ce.login_btn_element)
        cf.click_element(element_login_btn)
        time.sleep(2)
        
    except:
        log.info("Login button is not clicked due to wrong username or password")

    try:
        try:
            invalid_login=browser.find_element_by_css_selector(ce.invalid_login_element).is_displayed()
        except:
            log.info("login credentials are given")
        if invalid_login:            
            raise Exception
    except Exception as e:
        log.error("Please give correct user name and/or password")
        sys.exit()
        
    else:
        log.info("Correct login credentials. Continue...")
    
    #wait for sometime until the browser comes
    time.sleep(5)
    
#This function is for searching products using search bar
def search_product(browser, value):
    #search_bar_element=cf.find_an_element(browser, find_by, element)
    try:
        search_bar_element=browser.find_element_by_xpath(ce.search_box_element)
        cf.send_inputs(search_bar_element, value)
        search_bar_element.send_keys(Keys.RETURN)
        log.info("Product is searched")
        time.sleep(5)
    except Exception as e:
        log.error("Search is stopped")
        log.error(str(e))
 
#For selecting a product randomly from the displayed page   
def select_product_randomly(browser, find_by, element):
    try:
        list_of_elements=cf.find_page_elements(browser, find_by, element)
        time.sleep(5)
        rand_num=randint(0,len(list_of_elements)-1)
        list_of_elements[rand_num].click()
        log.info("Product is picked up. Redirecting to the product info page")
    except Exception as e:
        log.error("Can not select a product")
        log.error(str(e))
    
#Entering zip code
def zip_code(browser, value):
    #zip_element=cf.find_an_element(browser, find_by, element)
    zip_element=browser.find_element_by_xpath(ce.zip_code_element)
    try:
        browser.find_element_by_xpath(ce.change_zip_code_btn_element).click()
    except:
        log.info("Change is not needed. Directly writing the zip code")
    time.sleep(2)
    zip_element.clear()
    time.sleep(2)
    cf.send_inputs(zip_element, value)#value="560100"
    browser.find_element_by_xpath(ce.check_zip_code_btn_element).click()
    time.sleep(5)

#Add to cart
def add_to_cart(browser):
    try:
        cart_btn_element=browser.find_element_by_xpath(ce.cart_add_btn_element)
        if cart_btn_element.is_enabled():
            cf.click_element(cart_btn_element)
            time.sleep(5)
        else:
            log.info("This product is not deliverable to the location. Please select other product or other location.")
            sys.exit()
    except:
        log.warning("The item is sold out. Please try for other items")
        sys.exit()
        
#Taking snapshot
def take_snap_shot(browser,save_path):
    try:
        browser.save_screenshot(save_path)
        log.info("Screenshot is saved at "+save_path)
        time.sleep(5)
    except:
        log.error("Please give correct path")
        sys.exit()
        
#remove item from cart
def remove_from_cart(browser):
    try:
        #browser.find_element_by_xpath("//span[@text()='Remove']")
        browser.find_element_by_css_selector(ce.cart_rmv_btn_element).click()
        time.sleep(5)
        log.info("Element has been removed")
    except:
        log.error("Element not found")
        sys.exit()
        
#logout session
def user_logout(browser,find_by):
    cf.mouse_hover_on_element(browser, find_by, ce.name_element)
    logout_elem=cf.find_an_element(browser, find_by, ce.logout_btn_element)
    cf.click_element(logout_elem)
    time.sleep(5)
    
    

