#单元测试
import unittest
import similarity
"""
def read(doc_path):
    #过滤文本：除去字符，返回字符串
    doc = open(doc_path, encoding='UTF-8')
    punch = '~`!#$%^&*()_+-=|\';:/.,?><~·！@#￥%……&*（）——+-=“”：’；、。，？》《{} \n'
    doc_txt = re.sub(r"[%s]+" % punch, "", doc.read())
    doc.close()
    return doc_txt
"""

class TestSimilarity(unittest.TestCase):
    def setUp(self):
        self.path1 = "./orig.txt"

    def tearDown(self):
        print("over!")

    def test_selt(self):
        print("test self")
        path2 = "./orig.txt"
        s = similarity.Similarity(self.path1,path2).similar()
        print('%.2f' % s)
        #对比判断测试是否正确
        self.assertGreaterEqual(s , 0)
        self.assertLessEqual(s, 1)

    def test_add(self):
        print("test add")
        path2 = "./orig_0.8_add.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_del(self):
        print("test del")
        path2 = "./orig_0.8_del.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_dis_1(self):
        print("test dis_1")
        path2 = "./orig_0.8_dis_1.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_dis_3(self):
        print("test dis_3")
        path2 = "./orig_0.8_dis_3.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_dis_7(self):
        print("test dis_7")
        path2 = "./orig_0.8_dis_7.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_dis_10(self):
        print("test dis_10")
        path2 = "./orig_0.8_dis_10.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_dis_15(self):
        print("test dis_15")
        path2 = "./orig_0.8_dis_15.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_mix(self):
        print("test mix")
        path2 = "./orig_0.8_mix.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)
    def test_rep(self):
        print("test rep")
        path2 = "./orig_0.8_rep.txt"
        s = similarity.Similarity(self.path1, path2).similar()
        print('%.2f' % s)
        # 对比判断测试是否正确
        self.assertGreaterEqual(s, 0)
        self.assertLessEqual(s, 1)

if __name__ == '__main__':
    unittest.main()
