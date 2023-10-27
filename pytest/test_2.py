from typing import Union, Dict
from pandas import DataFrame
import pandas as pd
import os

def get_source_data() -> Dict[str, DataFrame]:
    metrics_data = DataFrame({
        "Date": ["16/12/2006"] * 24,
        "Time": ["17:24:00"] * 24,
        'ActivePower': [4.216, 5.36, 5.374, 5.388, 3.666, 3.52, 3.702, 3.7, 3.668, 3.662, 4.448, 5.412, 5.224, 5.268,
                        4.054, 3.384, 3.27, 3.43, 3.266, 3.728, 5.894, 7.706, 7.026, 3.666],
        'UnitPrice': [0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,
                      0.6, 0.6, 0.3, 0.3, 0.3]
    })

    return {
        "metrics_data": metrics_data
    }

def generate_report(source: Dict, contract: Union[Dict, None] = None) -> bool:

    if not isinstance(contract, Dict):
        return False

    metrics_data = source.get('metrics_data')

    if not isinstance(metrics_data, DataFrame):
        return False

    metrics_data['Amount'] = metrics_data['UnitPrice'] * metrics_data['ActivePower']

    metrics_data.to_csv('metrics_report.csv', index=False)

    return True


# 1. Write the test cases to test function get_source_data() as much as you can
def test_get_source_data():
    data = get_source_data()
    metrics_data = data.get('metrics_data')

    # 检查数据是否是字典，包含 'metrics_data' 键
    assert isinstance(data, dict)
    assert 'metrics_data' in data

    # 检查 'metrics_data' 是否是 DataFrame
    assert isinstance(metrics_data, pd.DataFrame)

    # 检查 'metrics_data' DataFrame 是否具有预期列
    expected_columns = ["Date", "Time", "ActivePower", "UnitPrice"]
    assert all(col in metrics_data.columns for col in expected_columns)

    # 检查 'metrics_data' DataFrame 是否具有预期行数
    assert len(metrics_data) == 24

# 2. Write the test cases to test function generate_report() as much as you can
def test_generate_report():
    # 创建一个示例合同字典
    contract = {"contract_key": "value"}

    # 使用有效合同和源数据进行测试
    source_data = get_source_data()
    result = generate_report(source_data, contract)

    # 检查结果对于有效合同和源数据是否为 True
    assert result is True

    # 检查是否创建了 'metrics_report.csv' 文件
    assert os.path.exists('metrics_report.csv')

    # 使用无效合同（应返回 False）进行测试
    result = generate_report(source_data, None)
    assert result is False

    # 使用无效源数据（应返回 False）进行测试
    result = generate_report({"invalid_data": "invalid"}, contract)
    assert result is False

    # 清理：删除生成的 'metrics_report.csv' 文件
    if os.path.exists('metrics_report.csv'):
        os.remove('metrics_report.csv')