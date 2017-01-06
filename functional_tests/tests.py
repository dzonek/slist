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
        self.check_for_row_in_list_table('1:Kupic pawie piora')
        self.check_for_row_in_list_table('2:Uzyc pawich pior do zrobienia przynety')


        #Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnej rzeczy do zrobienia
        #Edyta wpisala "Uzyc pawich pior do zrobienia przynety" (Edyta jest niezwykle skrupulatna)

        self.fail('Zakonczenie testu!')


        
        #Strona zostala ponownie uaktualniona i teraz wyswietla dwa elementy na liscie rzeczy do zrobienia

        #Edyta byla ciekawa czy witryna zapamieta jej liste. Zwrocila uwage na wygenerowany dla niej unikatowy adres URL, obok ktorego znajduje sie pewien tekst 
        #z wyjasnieniem

        #Przechodzi pod podany adres URL i widzi wyswietlona swoja liste rzeczy do zrobienia

        #Usatysfakcjonowana kladzie sie spac

#if __name__=='__main__':
#    unittest.main()#warnings='ignore')
