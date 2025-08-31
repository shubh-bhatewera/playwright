import time

from playwright.sync_api import Page, expect


def test_ui_checks(page: Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    element = page.get_by_placeholder('Hide/Show Example')
    expect(element).to_be_visible()
    page.get_by_role('button', name='Hide').click()
    expect(element).to_be_hidden()

    #handle alert
    page.on("dialog", lambda dialog : dialog.accept())
    page.get_by_role('button', name='Confirm')

    #mouse hover
    page.locator("xpath=//*[@id='mousehover']").hover()
    time.sleep(3)
    page.get_by_role('link', name="Top").click()
    time.sleep(3)

    #frame handiling
    frame = page.frame_locator('#courses-iframe')
    frame.get_by_role('link', name='All Access Plan').click()
    expect(frame.locator('body')).to_contain_text('Happy Subscibers!')

#Check the Price of rice is equal to 37
#Identity the price column
#Identify the rice row
#Extract the price of the rice

def test_ecart_one(page: Page):
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/')
    with page.expect_popup() as new_page_info:
        page.get_by_role('link', name='Top Deals').click()
        new_page = new_page_info.value
        for i in range(new_page.locator('th').count()):
            if new_page.locator('th').nth(i).filter(has_text='Price').count()>0:
                price_column_index = i
                print(f'Price column index is : {price_column_index}')
                break
        rice_row = new_page.locator('tr').filter(has_text='Rice')
        expect(rice_row.locator('td').nth(price_column_index)).to_have_text('37')


