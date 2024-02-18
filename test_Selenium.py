from selenium.webdriver.common.by import By



def test_keys(web_browser):
    web_browser.get('https://demoqa.com/')
    url = web_browser.current_url
    print(f'Сайт открыт на странице {url}')
    assert url == 'https://demoqa.com/'

    """Нажимаем кнопку елементс и проверяем"""
    element = web_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    text_element = element.text
    print(f'Текст кнопки {text_element} == Elements')
    assert text_element == 'Elements'
    element.click()
    url2 = web_browser.current_url

    """Проверяем, переход после нажатия на кнопку, урл должен измениться + открыта нужная нам страница"""
    print(f'{url}  != {url2}')
    assert url != url2
    print(f'Страница открыта на {url2}')
    assert url2 == 'https://demoqa.com/elements'

    """Кликаем кнопку чек-бокс и делаем проверки страницы"""
    chec_box_button = web_browser.find_element(By.XPATH, '//*[@id="item-1"]')
    text_chec_box = chec_box_button.text
    chec_box_button.click()
    url3 = web_browser.current_url
    print(f'Текст кнопки == {text_chec_box}')
    assert text_chec_box == 'Check Box'
    print(f'{url2} != {url3}')
    assert url2 != {url3}
    print(f'Страница открыта на {url3}')
    assert url3 == 'https://demoqa.com/checkbox'

    """Раскрываем дерикторию Hom и делаем проверки"""
    button_hom = web_browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    title_toggle = button_hom.get_attribute('title')
    button_hom.click()
    text_directoriy = web_browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol').text
    print(f'title содержит в себе название {title_toggle}')
    assert title_toggle == 'Toggle'
    print(f'При нажатии на кнопку, открылись директории {text_directoriy}')
    assert len(text_directoriy) != 0

    """Раскрываем директорию Downloads и делаем проверки"""
    button_downloads = web_browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
    class_button = button_downloads.get_attribute('class')
    button_downloads.click()
    text_directorory_downloads = web_browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol').text
    print(f'Атрибут класса  кнопки downloads == {class_button}')
    assert class_button == 'rct-collapse rct-collapse-btn'
    print(f'При нажатии на кнопку открылись директории {text_directorory_downloads}')

    """Проверяем чек-бокс Word File.doc"""
    chec_box_world = web_browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]')
    text_chec_box_world = chec_box_world.text
    chec_box_world.click()
    text_final = web_browser.find_element(By.XPATH, '//*[@id="result"]').text
    print(f'Текст директории с чек-бокс {text_chec_box_world}')
    assert text_chec_box_world == 'Word File.doc'
    print(f'При нажатии на чек-бокс появилось сообщение -- {text_final}')
    assert len(text_final) != 0




