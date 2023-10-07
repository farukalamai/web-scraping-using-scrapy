from selenium.webdriver import Chrome

driver = Chrome()
driver.get("https://www.thebluebook.com/search.html?region=4&class=2200&page=3")


links = []
for link in driver.find_elements_by_xpath("//h3/a/@href"):
    print(link)
    links.append(link)

driver.quit()
# links = []

# for link in link_list:
#     print(link)
#     links.append(link)

# driver.quit()






