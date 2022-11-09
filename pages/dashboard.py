from pages.base_page import BasePage


class Dashboard(BasePage):
    expect_title_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
    language_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    add_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[2]/b"
    main_page_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_list_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    logo_scouts_panel_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]"
    count_block_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div"
    shortcuts_block_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/h2"
    
    pass
