URL = 'https://phoible.org/parameters'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(URL)
# print(driver.page_source)
# driver.quit()

search = driver.find_element_by_id('dt-filter-name')
table = driver.find_element_by_id('Segments')
tbody = driver.find_element_by_xpath('//tbody')

def get_sound(name, page):
    source = page.find_element_by_xpath("//table[@class='infobox']//tbody//tr[last()]//td//div[2]//small//a[1]")
    print(source.text, source.get_attribute('href'))
    source.click()
    downloadUrl = page.find_element_by_xpath("//div[@class='fullMedia']//p//a").get_attribute('href')
    print(downloadUrl)
    r = requests.get(downloadUrl, allow_redirects=True)
    open('./Sounds/Union/' + name + '.ogg', 'wb').write(r.content)
    

def get_page(phoneme, link):
    print(phoneme, link)
    page = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    page.get(link)

    name = page.find_element_by_xpath("//p[1]").text
    wikiLink = page.find_element_by_xpath("//h2[1]//a")
    print(name, wikiLink.get_attribute('href'))
    wikiLink.click()
    get_sound(name, page)

    page.quit()


def search_and_destroy(phoneme):
    search.clear()
    search.send_keys(phoneme)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//tbody//tr[1]//a[@title="' + phoneme + '"]'))
        )
        # print(element.find_element_by_xpath("..//..//td[3]").text)
        get_page(phoneme, element.get_attribute('href'))
    finally:
        pass


for phoneme in phonemes:
    search_and_destroy(phoneme)

driver.quit()