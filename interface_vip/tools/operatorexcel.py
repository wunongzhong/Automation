import os

from openpyxl import *

from requestcommon.configcommon import test_case_path
from tools.log import logger


class excelData:
    def getExcel(self):
        logger.info("遍历用例目录读取用例excel开始。。。。。。。。。。。。。")
        file_name_list = os.walk(test_case_path,topdown=True)
        dict = {}

        for root, dirs, file_name in file_name_list:
            try:
                for name in file_name:
                    print(os.path.join(root, name))
                    logger.info("读取用例excel中sheet开始。。。。。。。。。。。。。")
                    workbook = load_workbook(os.path.join(root, name))
                    sheet = workbook['Sheet1']

                    lists = []
                    rows_sheet = sheet.iter_rows()
                    for item in rows_sheet:
                        if item[0].value == "api":
                            continue
                        list = []
                        for col in item:
                            # logger.info("遍历每一列加入到一行测试数据。。。。。。。。。。。。。")
                            list.append(col.value)
                        lists.append(list)
                    dict[name] = lists
            except Exception as e:
                logger.error("历用例目录读取用例excel执行出错，请查看问题！原因: s%", e)
        # print(dict)

        return dict
    def get_excel_data(self):
        logger.info("执行转换用例开始。。。。")
        contents=[]
        if len(contents) >= 0:
            logger.info("读取excel用例数据。。。。")
            casedata = excelData().getExcel()
            logger.info("循环读取excel中每行数据开始。。。。")
            for case in casedata:
                name = case
                listcase = casedata[name]
                for list in listcase:
                    contents.append(list)
            logger.info("excel用例数据读取完成。。。。")
        # print(contents)
        return contents


