from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait           # 显式等待             方法名   返回一个页面对象
from selenium.webdriver.support import expected_conditions as EC        # 先决条件        用显式等待这 3 个方法同时导入   连带使用
from selenium.webdriver.common.by import By                       # 第一个参数的固定形式

driver = webdriver.Chrome("./tools/chromedriver.exe")

try:
    driver.implicitly_wait(3)

    # copy:#s_position_list > ul > li:nth-child(1) > div.list_item_top > div.position > div.p_top > a
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")        #  Element is not clickable ：该元素不能被点击

    window_zhu = driver.current_window_handle
    driver.switch_to.window(window_zhu)      # 激活主页面  并存起来成变量

    while True:

        jobs_link = driver.find_elements_by_css_selector(".item_con_list li")
        # job_link = driver.find_element_by_css_selector(".p_top a span")     #很多时候 a标签点击不了（会报错）  只能再往下找具体的 标签（如span）
        # job_link = driver.find_element_by_css_selector(".item_con_list li .p_top a")
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.item_con_list li')))

        for job in jobs_link:
            job_link = job.find_element_by_css_selector(".p_top a span")
            job_link.click()
                                             #  没有下面这步  你下面所有的操作都是针对主页面的不是你点击打开的那个页面
            driver.switch_to.window(driver.window_handles[1])   # 第一个页面索引为[1]
            job_compny = driver.find_element_by_css_selector(".company")
            job_name = driver.find_element_by_css_selector(".name")
            job_money = driver.find_element_by_css_selector(".salary")
            job_years = driver.find_element_by_css_selector(".job_request p span:nth-child(3)")
            print("公司名称：",job_compny.text,
                  "职位名称：",job_name.text,
                  "薪资范围",job_money.text,
                  "年限限制",job_years.text)
            driver.close()   # 只关闭当前活动页面
            driver.switch_to.window(window_zhu)
        next_page = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pager_container a:last-child")))
        next_page_class = next_page.get_attribute("class")          # 对象属性有：text                      获得该对象的文本信息属性
        if "pager_next_disabled" in next_page_class:     #             get_attribute（“属性”） 获得该对象的任意一个属性的值
            break
        else:
            next_page.click()
            time.sleep(3)

finally:
    time.sleep(3)
    driver.quit()     # 退出浏览器关闭所有页面
