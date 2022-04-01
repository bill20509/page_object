import pytest
'''
-s: 顯示程序中的print/logging輸出
-v: 豐富信息模式, 輸出更詳細的用例執行信息
-q: 安靜模式, 不輸出環境信息
-k：關鍵字匹配，用and區分：匹配範圍（文件名、類名、函數名)
-m=xxx: 運行打標籤的用例 
pytest.main(['./'])               # 運行./目錄下所有（test_*.py  和 *_test.py）
pytest.main (['./subpath1'])    # 運行./subpath1 目錄下用例
pytest.main (['./subpath1/test_module1.py'])    # 運行指定模塊
pytest.main (['./subpath1/test_module1.py::test_m1_1'])  # 運行模塊中的指定用例
pytest.main (['-k','pp'])         # 匹配包含pp的用例(匹配目錄名、模塊名、類名、用例名)
pytest.main(['-k','spec','./subpath1/test_module1.py'])     # 匹配test_module1.py模塊下包含spec的用例
pytest.main(['-k','pp','./subpath2/test_module2.py::TestM2'])   # 匹配TestM2類中包含pp的用例
pytest.main(['-s','./subpath1/test_module1.py'])        # -s: 顯示程序中的print/logging輸出
@pytest.mark.test "-m=test"
'''
if __name__ == '__main__':
    pytest.main(['--html=result.html', '-s', '-m=not test'])
