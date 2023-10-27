from selenium import webdriver
import time

# 初始化Selenium WebDriver
driver = webdriver.Chrome()

# 打开测试网页
driver.get('./index.html')

try:
    # 测试用例1: 验证网页标题
    assert "Automation Test" in driver.title

    # 测试用例2: 输入姓名和邮箱，选择性别，然后点击提交按钮
    driver.find_element_by_id('name').send_keys('John Doe')
    driver.find_element_by_id('email').send_keys('johndoe@example.com')
    driver.find_element_by_id('male').click()
    driver.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(2)  # 等待弹出的警告框加载

    # 测试用例3: 验证提交后是否出现警告框
    alert = driver.switch_to.alert
    assert "You have submitted the application form." in alert.text
    alert.accept()  # 关闭警告框

    # 测试用例4: 清空表单，然后尝试提交（应该触发JavaScript验证）
    driver.find_element_by_id('name').clear()
    driver.find_element_by_id('email').clear()
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(2)  # 等待弹出的警告框加载

    # 测试用例5: 验证是否出现错误警告框
    alert = driver.switch_to.alert
    assert "请填写所有必填字段" in alert.text
    alert.accept()

    # 测试用例6: 验证单选按钮"女性"是否选中
    female_radio = driver.find_element_by_id('female')
    assert female_radio.is_selected()

    # 测试用例7: 验证单选按钮"男性"是否未选中
    male_radio = driver.find_element_by_id('male')
    assert not male_radio.is_selected()

    # 测试用例8: 验证单选按钮"其他"是否未选中
    others_radio = driver.find_element_by_id('others')
    assert not others_radio.is_selected()

finally:
    # 关闭浏览器
    driver.quit()
