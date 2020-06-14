import automate as a
from bs4 import BeautifulSoup

def scrapeInfo(email, password):
    driver = a.createDriver(False)
    a.authenticate(driver, email, password)

    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'lxml')
    scores = soup.find_all(id='id_rc')
    for score in scores:
        return score.text

