from selene.support.shared import browser
from selene import be, have


def test_google_search_positive(open_browser):
    positive_search = 'selene'
    positive_search_result  = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    browser.element('[name="q"]').should(be.blank).type(positive_search).press_enter()
    browser.element('[id="search"]').should(have.text(positive_search_result))


def test_google_search_negative(open_browser):
    negative_search = 'pofsmasdfusdfaskdfiasdfasdfaS'
    negative_search_result = 'About 0 results'

    browser.element('[name="q"]').should(be.blank).type(negative_search).press_enter()
    browser.element('[id="result-stats"]').should(have.text(negative_search_result))

