from behave import given, when, then


@given("Open Walmart Page")
def open_page(context):
    print("Test")
    context.app.main_page.open_website("https://walmart.com")
    # context.driver.get("https://yahoo.com")

