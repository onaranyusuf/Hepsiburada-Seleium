from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

def log_finish(logtext):
    logtext = "----------------------------- " + logtext
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(logtext + "\n")
    log_file.close()

def test_chrome():
    print("CHROME PART IS OPENING")
    log_finish("CHROME PART IS OPENING -----------------------------")
    #------------------------------
    driver = webdriver.Chrome() #create an instance of webDriver object /launch Chrome
    wait5 = WebDriverWait(driver, 20)
    #------------------------------
    driver.get("https://www.hepsiburada.com/") #navigate to url
    title = driver.title
    url = driver.current_url
    print("Website Title is:", title)
    print("Website URL is:", url)
    log("Website Title is: " + title)
    log("Website URL is: " + url)
    #------------------------------
    cookies = wait5.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
    cookies.click()
    print("Cookies accepted!")
    log("Cookies accepted!")
    # ------------------------------
    find_value = input("What are you looking for? : ")
    print("Searching item: ", find_value)
    log("Searched item: " + find_value)
    find = driver.find_element(by=By.CLASS_NAME, value="desktopOldAutosuggestTheme-UyU36RyhCTcuRs_sXL9b")
    find.send_keys(find_value)
    # ------------------------------
    search_button = driver.find_element(by=By.CLASS_NAME, value="SearchBoxOld-cHxjyU99nxdIaAbGyX7F")
    search_button.click()
    log("Clicking search button!")
    # ------------------------------
    succeed = False
    while succeed==False :
        try:
            wait5.until(EC.element_to_be_clickable(
                (By.ID, "i1"))).click()
            succeed = True
        except:
            pass
    log("Clicking second item!")
    # ------------------------------
    driver.switch_to.window(driver.window_handles[-1])  # new tab'in urlsi
    item_url = driver.current_url
    item_title = driver.title
    log("ITEM TITLE is: " + item_title)
    log("ITEM URL is: " + item_url)
    print("ITEM TITLE is:", item_title)
    print("ITEM URL is:", item_url)
    fiyat = driver.find_element(by=By.XPATH, value='//*[@class="product-price-and-ratings"]').text
    item_price = fiyat.splitlines()[0]
    print("ITEM PRICE is: " + item_price)
    log("ITEM PRICE is: " + item_price)
    # ------------------------------
    comments = wait5.until(EC.element_to_be_clickable((By.ID, 'productReviewsTab')))
    comments.click()
    log('Navigated to Comment Page!')
    print('Navigated to Comment Page')
    # ------------------------------
    wait5.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hermes-ReviewCard-module-PbSfiSWIgfswGGBaOrw7')))
    comment = driver.find_element(by=By.XPATH, value='//*[@class="hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw"]').text
    # ------------------------------
    print("First Comment:\n", comment.splitlines()[0])
    comment_to_file = comment.splitlines()[0]
    log("First Comment is: " + comment_to_file)
    yorum_file = open("comment.txt", "a", encoding='utf-8')
    yorum_file.write("-->"+find_value+" first comment: \n"+comment_to_file + "\n")
    yorum_file.close()
    # -------------------------------
    log_finish("CHROME PART FINISH-----------------------------\n")
    print("CHROME PART FINISH")
    driver.quit()

def test_firefox():
    print("FIREFOX PART IS OPENING")
    log_finish("FIREFOX PART IS OPENING -----------------------------")

    # ------------------------------
    driver = webdriver.Firefox()  # create an instance of webDriver object /launch Chrome
    wait5 = WebDriverWait(driver, 10)
    # ------------------------------
    driver.get("https://www.hepsiburada.com/")  # navigate to url
    title = driver.title
    url = driver.current_url
    print("Website Title is:", title)
    print("Website URL is:", url)
    log("Website Title is: " + title)
    log("Website URL is: " + url)
    # ------------------------------
    cookies = wait5.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler')))
    cookies.click()
    print("Cookies accepted!")
    log("Cookies accepted!")
    # ------------------------------
    find_value = input("What are you looking for? : ")
    print("Searching item: ", find_value)
    log("Searched item: " + find_value)
    find = driver.find_element(by=By.CLASS_NAME, value="desktopOldAutosuggestTheme-UyU36RyhCTcuRs_sXL9b")
    find.send_keys(find_value)
    # ------------------------------
    search_button = driver.find_element(by=By.CLASS_NAME, value="SearchBoxOld-cHxjyU99nxdIaAbGyX7F")
    search_button.click()
    log("Clicking search button!")
    # ------------------------------
    succeed = False
    while succeed == False:
        try:
            wait5.until(EC.element_to_be_clickable(
                (By.ID, "i1"))).click()
            succeed = True
        except:
            pass
    log("Clicking second item!")
    # ------------------------------
    driver.switch_to.window(driver.window_handles[-1])  # new tab'in urlsi
    item_url = driver.current_url
    item_title = driver.title
    log("ITEM TITLE is: " + item_title)
    log("ITEM URL is: " + item_url)
    print("ITEM TITLE is:", item_title)
    print("ITEM URL is:", item_url)
    succeed = False
    while succeed == False:
        try:
            fiyat = driver.find_element(by=By.XPATH, value='//*[@id="offering-price"]').text
            succeed = True
        except:
            pass
    #fiyat = driver.find_element(by=By.XPATH, value='//*[@id="offering-price"]').text
    item_price = fiyat.splitlines()[0]
    print("ITEM PRICE is: " + item_price)
    log("ITEM PRICE is: " + item_price)
    # ------------------------------
    #comments = wait5.until(EC.element_to_be_clickable((By.ID, 'reviewsTabTrigger')))
    succeed = False
    while succeed == False:
        try:
            wait5.until(EC.element_to_be_clickable((By.ID, 'reviewsTabTrigger'))).click()
            succeed = True
        except:
            pass
    succeed = False
    while succeed == False:
        try:
            wait5.until(EC.element_to_be_clickable((By.ID, 'reviewsTabTrigger'))).click()
            succeed = True
        except:
            pass

    succeed = False
    while succeed == False:
        try:
            wait5.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productReviewsTab"]'))).click()
            succeed = True
        except:
            pass

    log('Navigated to Comment Page!')
    print('Navigated to Comment Page')
    # ------------------------------
    wait5.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hermes-ReviewCard-module-PbSfiSWIgfswGGBaOrw7')))
    comment = driver.find_element(by=By.XPATH, value='//*[@class="hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw"]').text
    # ------------------------------
    print("First Comment:\n", comment.splitlines()[0])
    comment_to_file = comment.splitlines()[0]
    log("First Comment is: " + comment_to_file)
    yorum_file = open("comment.txt", "a", encoding='utf-8')
    yorum_file.write("-->"+find_value + " first comment: \n" + comment_to_file + "\n")
    yorum_file.close()
    # -------------------------------
    log_finish("FIREFOX PART FINISH-----------------------------\n")
    print("FIREFOX PART FINISH")
    driver.quit()

test_chrome()
time.sleep(2)
test_firefox()
