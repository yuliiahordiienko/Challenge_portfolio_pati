from pages.base_page import BasePage

class Dashboard(BasePage):

    form_name_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span"
    my_team_field_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    submit_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]"
    clear_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    calendar_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    number_field_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    form_group_radio_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div"
    rating_form_group_select_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    required_helper_text_xpath = "//*[contains( @class,"MuiFormHelperText-root Mui-error Mui-required")]"
    icon_radio_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]"
    pass
