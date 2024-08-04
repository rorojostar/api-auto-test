"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   yaml_utils
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/16 -- 22:33     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import yaml


class YamlUtils:
    @staticmethod
    def read_yaml(yaml_path, node_name):
        with open(yaml_path, 'r', encoding='utf-8') as file:
            datas = yaml.safe_load(file)
            login_dict = datas[node_name]
            print(login_dict)
            return list(login_dict.values())

    def get_non_null_fields(yaml_path, node_name):
        """
        获取yaml文件中所有数据项里非null字段的集合
        返回一个集合，包含所有出现过的非null字段名
        """
        all_data = YamlUtils.read_yaml(yaml_path, node_name)
        non_null_field_set = set()
        for data_item in all_data:
            if isinstance(data_item, dict):  # 确保当前项是字典
                for field, value in data_item.items():
                    if value is not None:
                        non_null_field_set.add(field)
        return non_null_field_set


if __name__ == '__main__':
    YamlUtils.read_yaml("../datas/test_login.yaml", "case_login")
    # YamlUtils.get_non_null_fields("../datas/test_customer_list.yaml", "case_customer_list")

