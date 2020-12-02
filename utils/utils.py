from selenium.common.exceptions import NoSuchElementException


def element_exists_by_id(element_id, driver):
    try:
        driver.find_element_by_id(element_id)
    except NoSuchElementException:
        return False
    return True


def element_exists_by_css_selector(css_selector, driver):
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True
