import os, json


class Data:
    """解析测试数据"""

    @classmethod
    def get_json_data(cls, file):
        """
        解析json文件
        :param file: 项目Data目录下文件名字
        :return: json文件数据
        """
        # 打开json文件
        with open("./Data" + os.sep + file, "r", encoding="utf-8") as f:
            # 使用json库解析数据
            return json.load(f)

    def get_csv_data(self):
        """解析csv文件"""
