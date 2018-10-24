from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("./tools/chromedriver.exe")

try:
    driver.implicitly_wait(5)
    driver.get("https://movie.douban.com/top250")
    window_zhu = driver.current_window_handle
    driver.switch_to.window(window_zhu)

    movies_links = driver.find_elements_by_css_selector(".article .grid_view li")
    movies_nums = movies_links.__len__()
    print("总共",movies_nums,"个电影")
    WebDriverWait(driver,8).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".article .grid_view li")))

    for movie in range(0,movies_nums):
        movie_link = movie.find_element_by_css_selector(".hd a span:first-child")  #   ???????????????????
        movie_link.click()

        no = driver.find_element_by_css_selector(".top250-no")
        name = driver.find_element_by_css_selector("#content h1 span:first-child")
        date = driver.find_element_by_css_selector("#info > span:nth-child(16)")
        grade = driver.find_element_by_css_selector(".rating_num")
        print("排名：",no.text,"电影名：",name.text,"上映时间：",date.text,"评分：",grade.text)
        #driver.close()
        driver.back()

        a = WebDriverWait(driver,9).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".paginator .next")))
        b = a.get_attribute("href")
        # if b                ?????????????????????????

finally:
    time.sleep(3)
    driver.quit()