from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

# paths
cwd = Path(__file__).parent.resolve()
data_dir = cwd.joinpath("data/")

print(data_dir.joinpath("latest.csv"))
# config
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1230x970")


# set up dataframe
df = pd.DataFrame(columns=["id", "school", "status", "color", "staff_student", "transmission", "staff_student_rate", "community_rate", "lac_rate", "community_schools", "community", "date", "time"])

#
url = 'https://achieve.lausd.net/covidreportcard'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
html_data = requests.get(soup.iframe['src']).text

driver = webdriver.Chrome(
    ChromeDriverManager().install(),
    options=chrome_options
)


def load():
    """
    load webdriver and wait for contents
    """

    print("Wating to load")

    driver.get(soup.iframe['src'])

    while True:
        divs = driver.find_elements_by_class_name("bringToFront")
        time.sleep(15)
        if len(divs) > 24:
            time.sleep(30)
            date_raw = divs[4]
            date_raw.text != ''
            break

    date_trim = date_raw.text.split()[2]
    date_clean = date_trim.replace("/", "-")
    timestamp = f"{date_raw.text.split()[3].split(':')[0]}{date_raw.text.split()[4]}"

    print(f"Updated date: {date_clean}-{timestamp}")

    return date_clean, timestamp


def clickToOpen():
    """
    Click on the dropdown - make sure it's open
    """
    btn = driver.find_element_by_class_name("slicer-restatement")

    arrow = driver.find_element_by_class_name("dropdown-chevron")

    btn.click()

    time.sleep(.2)

    state = arrow.get_attribute("class").split()[-1]

    if state == "chevron-down":
        btn.click()


def clearSearch():
    clickToOpen()
    field = driver.find_element_by_tag_name("input")

    field.send_keys(Keys.COMMAND + 'a')
    field.send_keys(Keys.BACKSPACE)

    btn = driver.find_element_by_class_name("slicer-restatement")

    btn.click()


def findEndpoint():
    """
    scroll to bottom to get the last number
    """
    print("Fetching school count")

    clickToOpen()

    # get scroller
    scrollbar = driver.find_elements_by_class_name("scrollbar-inner")[1]
    driver.execute_script("arguments[0].scrollBy(0,2);", scrollbar)

    inner = driver.find_elements_by_class_name("scroll-bar")
    time.sleep(2)
    top = float(inner[1].get_attribute("style").split("top: ")[-1].replace("px;", ""))

    # scroll until
    while top < 159:
        driver.execute_script("arguments[0].scrollBy(0,200);", scrollbar)
        time.sleep(0.3)
        top = float(inner[1].get_attribute("style").split("top: ")[-1].replace("px;", ""))

    time.sleep(2)

    # get point-inset
    vis = driver.find_element_by_class_name("visibleGroup")
    children = vis.find_elements_by_xpath(".//div[@class='slicerItemContainer']")
    last = children[-1].get_attribute("point-inset")

    print(f"School count: {last}")

    time.sleep(1)

    return int(last)


def scroll_to(i):
    clickToOpen()

    scrollbar = driver.find_elements_by_class_name("scrollbar-inner")[1]
    dropper = None
    while dropper is None:
        try:
            driver.execute_script("arguments[0].scrollBy(0,1);", scrollbar)
            dropper = driver.find_element_by_xpath(f".//div[@point-inset='{i}']")
        except NoSuchElementException:
            driver.execute_script(f"arguments[0].scrollBy(0,{174});", scrollbar)
            time.sleep(0.2)


colors = {
    "rgb(36, 211, 27)": "green",
    "rgb(237, 198, 23)": "yellow"
}


def get_data(i):
    """
    get data
    """

    while True:
        try:
            scroll_to(i)
            time.sleep(0.2)
            dropper = driver.find_element_by_xpath(f".//div[@point-inset='{i}']")
            dropper.click()

        except NoSuchElementException:
            print(i)
            print("no element")
            time.sleep(1)
            continue

        except StaleElementReferenceException:
            print(i)
            print("stale")
            time.sleep(2)
            continue

        except ElementNotInteractableException:
            print(i)
            print("not interactable")
            time.sleep(1)
            continue

        except ElementClickInterceptedException:
            print(i)
            print("click intercepted")

            time.sleep(1)
            continue

        break

    time.sleep(0.8)

    if i > 2:
        while True:
            time.sleep(0.1)
            cards = driver.find_elements_by_class_name("card")
            # keep pulling cards till it's not same as one before
            if cards[0].text != df.loc[(len(df)-1), "school"]:
                break
    else:
        cards = driver.find_elements_by_class_name("card")

    # collect
    school_name = cards[0].text
    status = cards[1].text
    rgb = cards[1].find_elements_by_xpath('./*')[0].find_elements_by_xpath('./*')[0].get_attribute("style").split(';')[1].split(': ')[1]
    if rgb in colors.keys():
        color = colors[rgb]
    else:
        color = 'red'

    update_date = cards[2].text.split(": ")[1].split()[0]
    update_time = "".join(cards[2].text.split()[-2:])
    staff_student = cards[3].text
    transmission = cards[4].text
    staff_student_rate = cards[5].text
    community_rate = cards[6].text
    lac_rate = cards[7].text
    s_comm = cards[8].text
    comm = cards[9].text

    row = [i, school_name, status, color, staff_student, transmission, staff_student_rate, community_rate, lac_rate, s_comm, comm, update_date, update_time]

    df_length = len(df)

    df.loc[df_length] = row


def scrape():
    date_clean, timestamp = load()

    clearSearch()

    end = findEndpoint()

    print(f"Scraping {date_clean}-{timestamp} data from LAUSD")

    for i in range(2, end+1):
        get_data(i)

    driver.quit()

    print(df.duplicated().any())

    print(df.school.duplicated().any())

    df.to_csv(data_dir.joinpath("latest.csv"), index=False)

    print(f"Writing dataframe with {len(df)} rows.")


if __name__ == "__main__":
    scrape()
