from pages.base_page import Page


class MainPage(Page):

    def open_website(self, MyURL):
        self.open_page(url=MyURL)
