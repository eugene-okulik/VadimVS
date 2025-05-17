from selenium.webdriver.common.by import By


def result_row_in_modal(driver):
    tag_tr = driver.find_elements(By.TAG_NAME, 'tr')
    data_results = []
    for line in tag_tr:
        cells = line.find_elements(By.TAG_NAME, 'td')
        cell = [cell.text for cell in cells]
        data_results.append(cell)
    return data_results
