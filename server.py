# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os

import cherrypy

import config as conf
from datasource import ExcelData


class GetPostMethods(object):

    def __init__(self):
        try:
            self.hci_obj = ExcelData(conf.EXCEL_INFO['xls_name'][0])
            self.sds_obj = ExcelData(conf.EXCEL_INFO['xls_name'][1])
            self.job_name = ''
            self.build_name = ''

            self.html_body = open('html_code/index.html').read()
        except Exception as e:
            print(str(e))

    @cherrypy.expose
    def index(self):
        try:
            home_page = '<div class="cnt_header"><h1>Welcome to IBM Sepctrum Fustion (ISF) automation</h1> \
                            <p>&nbsp;</p> \
                          <h3>The app is to show/update automation executions of HCI and SDS</h3> \
                            <p>&nbsp;</p> <p>&nbsp;</p> \
                       <p>-> Click <a href="hci_dashboard">here</a> for HCI Automation</p> \
                            <p>&nbsp; &nbsp;</p> \
                          <p>-> Click <a href="hci_dashboard">here</a> for SDS Automation</p> </div>'
            html_body = open('html_code/index.html').read()
            html_body = html_body.replace('{content}', home_page)
            html_body = html_body.replace('{header_text}',
                                          "Welcome!")
            return html_body
        except Exception as e:
            print(str(e))

    # @cherrypy.expose
    # def hci_dashboard(self):
    #     try:
    #         home_page = '<div class="cnt_header"><h2>Dashboard development is in progress...</h2> \
    #                         </div>'
    #         html_body = open('html_code/index.html').read()
    #         html_body = html_body.replace('{content}', home_page)
    #         html_body = html_body.replace('{header_text}',
    #                                       "Welcome!")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def hci_bvt_execs(self, sel_job=None):
    #     try:
    #         html_body = open('html_code/index.html').read()
    #         html_body = html_body.replace('{content}',
    #                                       self.hci_obj.excel_to_html(
    #                                           conf.EXCEL_INFO["sheet_name"][
    #                                               0]))
    #         html_body = html_body.replace('{header_text}',
    #                                       "BVT Execution Result")
    #         print(sel_job)
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def hci_fvt_execs(self):
    #     try:
    #         html_body = open('html_code/index.html').read()
    #         html_body = html_body.replace('{content}',
    #                                       self.hci_obj.excel_to_html(
    #                                           conf.EXCEL_INFO["sheet_name"][
    #                                               1]))
    #         html_body = html_body.replace('{header_text}',
    #                                       "FVT/SVT Execution Result")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def jenkin_jobs(self, **value):
    #     try:
    #         if value and value.get('type') == 'sds':
    #             html_body = self.html_body.replace('{content}',
    #                                                self.sds_obj.get_all_jobs_html())
    #         else:
    #             html_body = self.html_body.replace('{content}',
    #                                                self.hci_obj.get_all_jobs_html())
    #         html_body = html_body.replace('{header_text}',
    #                                       "Select Jenkins job")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def jenkin_job_builds(self, **value):
    #     try:
    #         self.job_name = value['name_jobs']
    #         if value and value.get('type') == 'sds':
    #             html_body = self.html_body.replace('{content}',
    #                                                self.sds_obj.get_all_builds_html(
    #                                                    self.job_name))
    #         else:
    #             html_body = self.html_body.replace('{content}',
    #                                                self.hci_obj.get_all_builds_html(
    #                                                    self.job_name))
    #
    #         html_body = html_body.replace('{header_text}',
    #                                       "Select build from {} to update result".format(
    #                                           self.job_name))
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def update_result(self, **value):
    #     try:
    #         self.build_name = value['name_builds']
    #         html_body = open('html_code/index.html').read()
    #         excel_obj = self.hci_obj
    #         if value and value.get('type') == 'sds':
    #             excel_obj = self.sds_obj
    #
    #         if excel_obj.update_jenkins_data(self.job_name,
    #                                          self.build_name):
    #             status_string = '<div class="cnt_header">Updated Successfully</div>'
    #         else:
    #             status_string = '<div class="cnt_header">Failed to update</div>'
    #         html_body = html_body.replace('{content}', status_string)
    #         html_body = html_body.replace('{header_text}',
    #                                       "Update Jenkins build results")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # # SDS
    # @cherrypy.expose
    # def sds_bvt_execs(self, sel_job=None):
    #     try:
    #         html_body = self.html_body.replace('{content}',
    #                                            self.sds_obj.excel_to_html(
    #                                                conf.EXCEL_INFO[
    #                                                    "sheet_name"][
    #                                                    0]))
    #         html_body = html_body.replace('{header_text}',
    #                                       "BVT Execution Result")
    #         print(sel_job)
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def sds_fvt_execs(self):
    #     try:
    #         html_body = self.html_body.replace('{content}',
    #                                            self.sds_obj.excel_to_html(
    #                                                conf.EXCEL_INFO[
    #                                                    "sheet_name"][
    #                                                    1]))
    #         html_body = html_body.replace('{header_text}',
    #                                       "FVT/SVT Execution Result")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def sds_jenkin_jobs(self, **value):
    #     try:
    #         html_body = self.html_body.replace('{content}',
    #                                            self.sds_obj.get_all_jobs_html())
    #         html_body = html_body.replace('{header_text}',
    #                                       "Select Jenkins job")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def sds_jenkin_job_builds(self, **value):
    #     try:
    #         self.job_name = value['name_jobs']
    #         html_body = self.html_body.replace('{content}',
    #                                            self.sds_obj.get_all_builds_html(
    #                                                self.job_name))
    #         html_body = html_body.replace('{header_text}',
    #                                       "Select build from {} to update result".format(
    #                                           self.job_name))
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #
    # @cherrypy.expose
    # def sds_update_result(self, **value):
    #     try:
    #         status_string = ''
    #         self.build_name = value['name_builds']
    #         html_body = open('html_code/index.html').read()
    #         if self.sds_obj.update_jenkins_data(self.job_name,
    #                                             self.build_name):
    #             status_string = '<div class="cnt_header">Updated Successfully</div>'
    #         else:
    #             status_string = '<div class="cnt_header">Failed to update</div>'
    #         html_body = html_body.replace('{content}', status_string)
    #         html_body = html_body.replace('{header_text}',
    #                                       "Update Jenkins build results")
    #         return html_body
    #     except Exception as e:
    #         print(str(e))
    #

if __name__ == '__main__':
    try:
        curr_dir = os.getcwd()
        server_config = {
            # '/html_code':{'tools.staticdir.on' : True,
            # }
            '/': {
                'tools.staticdir.root': curr_dir + '/html_code'
            },
            '/images': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'images'},
            '/css': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'css'},
            'global': {
                'server.socket_host': '0.0.0.0'}
        }
        cherrypy.quickstart(GetPostMethods(), '/', server_config)

        # ds_obj=ExcelData(conf.EXCEL_INFO['xls_name'][0])
        # ds_obj.update_jenkins_data(2,2)
        # ds_obj.get_jobs_in_html()
        # ds_obj.get_suite_input_params()
        # ds_obj.excel_to_html()
        # ds_obj.update_excel_data()
    except Exception as e:
        print(str(e))
