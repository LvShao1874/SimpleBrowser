# coding=UTF-8
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from pyvirtualdisplay import Display


class SimpleBrowser(object):
    def __init__(self, driver, debug=False, global_wait_time_default=10):
        self.driver = driver
        self.debug = debug
        self.action_chains = action_chains
        self.global_wait_time_default = global_wait_time_default
    
    def __del__(self):
        self.quit()
    
    def quit(self):
        self.driver.quit()
    
    def get(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise e
    
    def set_window_size(self, width=1920, height=1080):
        self.driver.set_window_size(width, height)
    
    def find(self, element, by=By.XPATH, wait_time=None):
        if not wait_time:
            wait_time = self.global_wait_time_default
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located((by, element))
            )
            return element
        except Exception as e:
            raise e
    
    def find_one(self, element, by=By.XPATH, wait_time=None):
        if not wait_time:
            wait_time = self.global_wait_time_default
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, element))
            )
            return element
        except Exception as e:
            raise e
    
    def find_one_clickeable(self, element, by=By.XPATH, wait_time=None):
        if not wait_time:
            wait_time = self.global_wait_time_default
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable((by, element))
            )
            return element
        except Exception as e:
            raise e
    
    def get_current_tab(self):
        return self.driver.current_window_handle
    
    def turn_to_new_tab(self, target_tab):
        handles = self.driver.window_handles
        if self.debug:
            print('当前窗口数:%s' % len(handles))
        for handle in handles:
            if handle != target_tab:
                self.driver.close()
                self.driver.switch_to.window(handle)
                if self.debug:
                    print('已关闭旧窗口,切换到新窗口,当前窗口数:%s' % len(self.driver.window_handles))
                break
    
    def scroll_to_view(self, target_item):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", target_item)
        except Exception as e:
            raise e
    
    def wait_and_click(self, item, wait_time=0):
        try:
            time.sleep(wait_time)
            self.do().move_to_element(item).click().perform()
        except Exception as e:
            raise e
    
    def wait_and_input(self, target_input, text, is_clear=True, wait_time=0):
        try:
            time.sleep(wait_time)
            if is_clear:
                target_input.clear()
            self.do().move_to_element(target_input).click().send_keys(text).perform()
        except Exception as e:
            raise e
    
    def do(self):
        try:
            return self.action_chains.ActionChains(self.driver)
        except Exception as e:
            raise e
    
    def get_page_source(self):
        return self.driver.page_source
    
    def set_max_time_out(self, time):
        self.driver.implicitly_wait(time)
    
    @staticmethod
    def get_virtual_display(is_show=False, width=1920, height=1080):
        display = Display(visible=1 if is_show else 0, size=(width, height))
        return display


if __name__ == "__main__":
    pass
