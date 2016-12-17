from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrive_it_later(self):
        #Edyta dowiedziala sie o nowej aplikacji "lista rzeczy do zrobienia"
        #Postanowila wiec przejsc na strone glowna aplikacji
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        
        #Zwrocila uwage, ze tytul strony i naglowek zawieraja slowo Listy
        self.assertIn('Listy', self.browser.title)
        self.fail('Zakonczenie testu!')


        #Od razu zostaje zachecona aby wpisac rzecz do zrobienia
        #W polu tekstowym wpisala "Kupic pawie piora (hobby Edyty polega na tworzeniu ozdobnych przynet)
        #Po nacisnieciu Enter strona zostala zaktualizowana i wyswietla
        #"1:Kupic pawie piora" jako element listy rzeczy do zrobienia

        #Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnej rzeczy do zrobienia
        #Edyta wpisala "Uzyc pawich pior do zrobienia przynety" (Edyta jest niezwykle skrupulatna)

        #Strona zostala ponownie uaktualniona i teraz wyswietla dwa elementy na liscie rzeczy do zrobienia

        #Edyta byla ciekawa czy witryna zapamieta jej liste. Zwrocila uwage na wygenerowany dla niej unikatowy adres URL, obok ktorego znajduje sie pewien tekst 
        #z wyjasnieniem

        #Przechodzi pod podany adres URL i widzi wyswietlona swoja liste rzeczy do zrobienia

        #Usatysfakcjonowana kladzie sie spac

if __name__=='__main__':
    unittest.main()#warnings='ignore')
