from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageFont, ImageDraw
from requests_html import HTMLSession
import personalinfo
import time


class JeromeBot:
    firefox_profile_dir = personalinfo.firefox_profile_dir

    def __init__(self, headless=False):
        self.profile = FirefoxProfile(self.firefox_profile_dir)
        self.options = Options()
        self.options.add_argument('-headless')
        if headless:
            self.driver = Firefox(firefox_profile=self.profile,
                                  executable_path='geckodriver',
                                  options=self.options)
        else:
            self.driver = Firefox(firefox_profile=self.profile,
                                  executable_path='geckodriver')
        self.driver.get('https://mbasic.facebook.com/jeromebot5000')

    def post_image(self, file_path, message):

        self.driver.find_element_by_name('view_photo').click()
        self.driver.find_element_by_name('file1').send_keys(file_path)
        self.driver.find_element_by_name('add_photo_done').click()
        time.sleep(1)
        for msg in message:
            self.driver.find_element_by_name(
                'xc_message').send_keys(msg, Keys.ENTER)
        #self.driver.find_element_by_name('view_post').click()

    def make_image(self, font, img_path, msg1, msg2, pos1, pos2, color, output_path):

        FONT = ImageFont.truetype(font, 60)

        base = Image.open(img_path).convert('RGBA')
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(txt)

        d.text(pos1, msg1, font=FONT, fill=color)
        d.text(pos2, msg2, font=FONT, fill=color)

        out = Image.alpha_composite(base, txt)
        out.save(output_path)

    def get_dolar(self):
        s = HTMLSession()
        r = s.get('https://www.google.com/search?q=dolar')
        raw = r.html.find(
            "#knowledge-currency__updatable-data-column", first=True)
        cotacao = raw.text.split('\n')[1]
        return cotacao


if __name__ == "__main__":
    jerome = JeromeBot()
    jerome.post_image('teste.jpeg', ['teste', 'outra linha'])
