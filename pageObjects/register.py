from utils.utils import element_exists_by_id, element_exists_by_css_selector


class Register:
    def __init__(self, driver):
        self.address = 'https://apteline.pl/customer/account/create'
        self.driver = driver

    def registration_form(self):
        return {
        'name' : self.driver.find_element_by_id('firstname'),
        'surname' : self.driver.find_element_by_id('lastname'),
        'email' : self.driver.find_element_by_id('email_address'),
        'phone' : self.driver.find_element_by_id('telephone'),
        'password' : self.driver.find_element_by_id('password'),
        'confirm_password' : self.driver.find_element_by_id('confirmation'),
        'agreement_checkbox' : self.driver.find_element_by_css_selector("label[for='agreement_4']")
        }

    def submit_registration(self):
        return self.driver.find_element_by_css_selector("button[type='submit'][title='Złóż zamówienie zakładając jednocześnie konto']")

    def fill_form(self, data):
        self.driver.get(self.address)
        self.registration_form()["name"].send_keys(data["name"])
        self.registration_form()["surname"].send_keys(data["surname"])
        self.registration_form()["email"].send_keys(data["email"])
        self.registration_form()["phone"].send_keys(data["phone"])
        self.registration_form()["confirm_password"].send_keys(data["password"])
        self.registration_form()["password"].send_keys(data["password"])
        self.registration_form()['agreement_checkbox'].click()
        self.submit_registration().click()

    def test_empty_form_validation_errors_present(self, data):
        self.fill_form(data)
        return (element_exists_by_id('advice-required-entry-firstname', self.driver)
                and element_exists_by_id('advice-required-entry-lastname', self.driver)
                and element_exists_by_id('advice-required-entry-email', self.driver)
                and element_exists_by_id('advice-required-entry-telephone', self.driver)
                and element_exists_by_id('advice-required-entry-pass', self.driver)
                and element_exists_by_id('advice-required-entry-agreement_4', self.driver)
                )

    def test_successful_registration(self, data):
        self.fill_form(data)
        return element_exists_by_css_selector('li.success-msg', self.driver)



