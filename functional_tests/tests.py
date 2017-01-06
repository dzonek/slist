from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text,[row.text for row in rows],"Nowy element nie znajduje sie w tabeli--jego tekst to:\n%s"%(row_text,))
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edyta dowiedziala sie o nowej aplikacji "lista rzeczy do zrobienia"
        #Postanowila wiec przejsc na strone glowna aplikacji
        self.browser.get(self.live_server_url)#'http://localhost:8000')
        self.browser.implicitly_wait(3)
        
        #Zwrocila uwage, ze tytul strony i naglowek zawieraja slowo Listy
        self.assertIn('Listy', self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('listy',header_text)#cos jest zle w ksiazce-duza/mala litera i odmiana Lista/Listy

        #Od razu zostaje zachecona aby wpisac rzecz do zrobienia
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Wpisz rzecz do zrobienia')

        #W polu tekstowym wpisala "Kupic pawie piora (hobby Edyty polega na tworzeniu ozdobnych przynet)
        inputbox.send_keys('Kupic pawie piora')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1:Kupic pawie piora')

        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Uzyc pawich pior do zrobienia przynety')
        inputbox.send_keys(Keys.ENTER)
 
        #Po nacisnieciu Enter strona zostala zaktualizowana i wyswietla
        #"1:Kupic pawie piora" jako element listy rzeczy do zrobienia
        #inputbox.send_keys(Keys.ENTER)
        
        import time
        time.sleep(10)

       # table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')

        #Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnej rzeczy do zrobienia
        #Edyta wpisala "Uzyc pawich pior do zrobienia przynety" (Edyta jest niezwykle skrupulatna)

        self.fail('Zakonczenie testu!')


        
        #Strona zostala ponownie uaktualniona i teraz wyswietla dwa elementy na liscie rzeczy do zrobienia
        self.check_for_row_in_list_table('1:Kupic pawie piora')
        self.check_for_row_in_list_table('2:Uzyc pawich pior do zrobienia przynety')

        #Teraz nowy uzytkownik Franek zaczyna korzystac  z witryny

        ##Uzywamy nowej sesji przegladarki internetowej aby miec pewnosc ze zadne informacje dotyczace Edyty nie zostana ujawnione np przez cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Nie znajduje zadnych sladow Edyty
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kupic pawie piora', page_text)
        self.assertNotIn('zrobienia przynety',page_text)

        #Franek tworzy nowa liste wprowadzajac nowy element. Jego lista jest mniej interesujaca niz lista Edyty
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kupic mleko')
        inputbox.send_keys(Keys.ENTER)

        #Franek otrzymuje unikatowy URL prowadzacy do listy
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Ponownie nie ma slady po liscie Edyty
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kupic pawie piora',page_text)
        self.assertNoitIn('Kupic mleko',page_text)

        #Usatysfakcjonowani klada sie spac

#if __name__=='__main__':
#    unittest.main()#warnings='ignore')
