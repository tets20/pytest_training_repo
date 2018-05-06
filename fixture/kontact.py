from model.kontact import Kontact

class KontactHelper:


    def __init__(self, app):
        self.app = app

    def create(self, kontact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_kontact_form(kontact)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.go_to_home_page()
        self.kontact_cache = None


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def fill_kontact_form(self, kontact):
        wd = self.app.wd
        # fill group form
        self.change_field_value("firstname",kontact.firstname)
        self.change_field_value("middlename", kontact.middlename)
        self.change_field_value("lastname", kontact.lastname)
        self.change_field_value("nickname",kontact.nickname)
        self.change_field_value("title", kontact.title)
        self.change_field_value("company", kontact.company)
        self.change_field_value("address", kontact.address)
        self.change_field_value("home", kontact.home)
        self.change_field_value("mobile", kontact.mobile)
        self.change_field_value("work", kontact.work)
        self.change_field_value("fax", kontact.fax)
        self.change_field_value("email", kontact.email)
        self.change_field_value("email2", kontact.email2)
        self.change_field_value("email3", kontact.email3)
        self.change_field_value("homepage", kontact.homepage)

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()

        self.change_field_value("byear",kontact.byear)
        self.change_field_value("ayear", kontact.ayear)
        self.change_field_value("address2", kontact.address2)
        self.change_field_value("phone2", kontact.phone2)
        self.change_field_value("notes", kontact.notes)


    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def delete_kontact_by_index(self,index):
        wd = self.app.wd
        self.go_to_home_page()
        #select first kontact
        self.select_group_by_index(index)
        # push button Delete
        wd.execute_script("DeleteSel()")
        #accept delete
        wd.switch_to_alert().accept()
        self.kontact_cache = None

    def delete_first_kontact(self):
        self.delete_kontact_by_index(0)


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def modify_kontact_by_index(self, new_kontact_data,index):
        wd = self.app.wd
        self.go_to_home_page()
        #select a contact for editing
        self.select_kontact_by_index(index)
        #editting
        self.fill_kontact_form(new_kontact_data)
        #update
        wd.find_element_by_name("update").click()
        if not (wd.current_url.endswith("/index.php") and
                len(wd.find_element_by_id("MassCB")) > 0):
            self.go_to_home_page()
        self.kontact_cache = None


    def modify_first_kontact(self,new_kontact_data):
        self.modify_kontact_by_index(new_kontact_data,0)


    def select_first_kontact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def select_kontact_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr" + str([index + 2])+ "/td[8]/a/img").click()



    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    kontact_cache = None


    def get_kontact_list(self):
        if self.kontact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.kontact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                list_td = element.find_elements_by_tag_name("td")
                firstname = list_td[1].text
                lastname = list_td[2].text
                self.kontact_cache.append(Kontact(id =id,firstname=firstname,lastname=lastname))
        return list(self.kontact_cache)

