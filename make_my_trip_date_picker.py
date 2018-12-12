from selenium import webdriver
from time import sleep as wait
class MMTDatePicker(object):
    """
    @author Aditya Singh
    @date :12,Dec,2018
    """
    def __init__(self):
        self.month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        self.mnth_dic = dict((v, k) for k, v in enumerate(self.month))
        self._ = webdriver.Chrome('C:\\tools\\chromedriver.exe')
        self._.get('https://www.makemytrip.com/')
        self._.maximize_window()
        wait(10)



    def select_date(self, startdate, endate):
        """

        :param startdate:
        :param enddate:
        :return:
        """
        if startdate.split()[1]== endate.split()[1]:       #if depart and retrun month is same.
            self.select_start_date(startdate)
            self.select_end_date(endate, start_end_month_same=True)
        else:
            self.select_start_date(startdate)
            self.select_end_date(endate)


    def select_start_date(self, start_date):
        depart_date = self._.find_element_by_id('hp-widget__depart')
        depart_date.click()
        self.select_year(start_date=start_date)
        self.select_month(start_date=start_date)
        self.select_day(start_date=start_date)


    def select_end_date(self, end_date, start_end_month_same=''):
        depart_date = self._.find_element_by_id('hp-widget__return')
        depart_date.click()
        wait(5)
        self.select_year(end_date=end_date)
        if start_end_month_same:
            self.select_day(start_date=end_date)
        else:
            self.select_month(end_date=end_date)
            self.select_day(end_date=end_date)


    def select_year(self, start_date='', end_date=''):
        if start_date:
            month_year = self._.find_element_by_css_selector('div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-left')
            year = month_year.find_element_by_css_selector('div.ui-datepicker-title').find_element_by_css_selector('span.ui-datepicker-year').text

            while year not in start_date:
                wait(4)
                month_year = self._.find_element_by_css_selector(
                    'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-left')
                year = month_year.find_element_by_css_selector('div.ui-datepicker-title').find_element_by_css_selector(
                    'span.ui-datepicker-year').text
                if int(year) > int(start_date.split()[2]):
                    # click prev
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-w')[0].click()
                    wait(2)
                elif int(year) < int(start_date.split()[2]):
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-e')[0].click()
                    wait(2)


        else:
            month_year = self._.find_elements_by_css_selector(
                'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-right')
            year = month_year[1].find_element_by_css_selector('div.ui-datepicker-title').find_element_by_css_selector(
                'span.ui-datepicker-year').text
            while year not in end_date:
                wait(4)
                month_year = self._.find_elements_by_css_selector(
                    'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-right')
                year = month_year[1].find_element_by_css_selector('div.ui-datepicker-title').find_element_by_css_selector(
                    'span.ui-datepicker-year').text
                if int(year) > int(end_date.split()[2]):
                    # click prev
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-w')[0].click()
                    wait(2)
                elif int(year) < int(end_date.split()[2]):
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-e')[0].click()
                    wait(2)

    def select_month(self, start_date='', end_date=''):
        if start_date:
            month_year = self._.find_element_by_css_selector(
                'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-left')
            month_title = month_year.find_element_by_css_selector(
                'div.ui-datepicker-title').find_element_by_css_selector('span.ui-datepicker-month').text
            while month_title[0:3] not in start_date:
                wait(3)
                month_year = self._.find_element_by_css_selector(
                    'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-left')
                month_title = month_year.find_element_by_css_selector(
                    'div.ui-datepicker-title').find_element_by_css_selector(
                    'span.ui-datepicker-month').text
                if int(self.mnth_dic[month_title[0:3]]) > int(self.mnth_dic[start_date.split()[1]]):
                    # click on previos
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-w')[0].click()
                    wait(3)
                elif int(self.mnth_dic[month_title[0:3]]) < int(self.mnth_dic[start_date.split()[1]]):
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-e')[0].click()
        else:
            month_year = self._.find_elements_by_css_selector(
                'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-right')
            month_title = month_year[1].find_element_by_css_selector(
                'div.ui-datepicker-title').find_element_by_css_selector(
                'span.ui-datepicker-month').text
            while month_title[0:3] not in end_date:
                wait(3)
                print "select month"
                month_year = self._.find_elements_by_css_selector(
                    'div.ui-datepicker-header.ui-widget-header.ui-helper-clearfix.ui-corner-right')
                month_title = month_year[1].find_element_by_css_selector(
                    'div.ui-datepicker-title').find_element_by_css_selector(
                    'span.ui-datepicker-month').text
                if int(self.mnth_dic[month_title[0:3]]) > int(self.mnth_dic[end_date.split()[1]]):
                    # click on previos
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-w')[0].click()
                    wait(3)
                elif int(self.mnth_dic[month_title[0:3]]) < int(self.mnth_dic[end_date.split()[1]]):
                    wait(3)
                    self._.find_elements_by_css_selector('span.ui-icon.ui-icon-circle-triangle-e')[1].click()

    def select_day(self, start_date='', end_date=''):
        if end_date:
            all_date_table = self._.find_elements_by_css_selector('table.ui-datepicker-calendar')
            all_dates = all_date_table[3].find_elements_by_css_selector('tbody>tr>td>a')
            for i in all_dates:
                if i.text == end_date.split()[0]:
                    i.click()
                    break
        else:
            all_dates = self._.find_elements_by_css_selector('table.ui-datepicker-calendar>tbody>tr>td>a')
            for i in all_dates:
                if i.text == start_date.split()[0]:
                    i.click()
                    break

if __name__=='__main__':
    date_picker = MMTDatePicker()
    date_picker.select_date('18 FEB 2019', '21 JUN 2019')
