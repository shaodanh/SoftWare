import jieba.analyse
from math import sqrt
import re
from functools import reduce
import sys

"""
def main (argv):
    path1 = argv[1]
    path2 = argv[2]
    path3 = argv[3]
    s = Similarity(path1, path2)
    print('%.2f' % s.similar())
    #写入文件
    with open(path3, 'w') as file_project:
        file_project.write('%.2f' % s.similar())
"""
class Similarity():

    #初始化，传入两个字符串。
    def __init__(self, path1, path2):

        def read(doc_path):
            # 过滤文本：除去字符，返回字符串
            doc = open(doc_path, encoding='UTF-8')
            punch = '~`!#$%^&*()_+-=|\';:/.,?><~·！@#￥%……&*（）——+-=“”：’；、。，？》《{} \n'
            doc_txt = re.sub(r"[%s]+" % punch, "", doc.read())
            doc.close()
            return doc_txt
        self.str1 = read(path1)
        self.str2 = read(path2)

    # 制作 关键词-词频 字典，获取词频向量
    def vector(self):
        self.vdict1 = {}
        self.vdict2 = {}
        #参数含义：待提取文本，关键词数量（按重要性降序），是否同时返回权重
        #返回值：关键词 词频
        top_keywords1 = jieba.analyse.extract_tags(self.str1, topK=1200, withWeight=True)
        top_keywords2 = jieba.analyse.extract_tags(self.str2, topK=1200, withWeight=True)
        for k, v in top_keywords1:
            #print(k,v)
            self.vdict1[k] = v
            #获取词频向量
        for k, v in top_keywords2:
            #print(k,v)
            self.vdict2[k] = v

    #整合关键词，数据预处理
    def mix(self):
        #整合两个字典
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
            #若vdict2的值存在，则返回dict[key]，不存在则返回0；
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)
        #vdict1和vdict2中分别包含文本1和2的关键词及其特征值

        def pre_treatment(vdict):
            #对特征值进行预处理：数据中每个数值减去最小值，除以极差
            min_ = min(vdict.values())#返回字典中最小值
            max_ = max(vdict.values())#返回最大值
            mid_ = max_ - min_#极差
            for key in vdict:
                vdict[key] = (vdict[key] - min_) / mid_
                #TFIDF： tf*log（
            return vdict

        self.vdict1 = pre_treatment(self.vdict1)
        self.vdict2 = pre_treatment(self.vdict2)

    #余弦向量计算相似度
    def similar(self):
        self.vector()
        self.mix()
        sum = 0
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))#匿名函数
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))
        #平方和开根号
        #print('%.2f' % sum / (A * B))
        return sum / (A * B)


if __name__ == '__main__':
    #main(sys.argv)
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    path3 = sys.argv[3]
    s = Similarity(path1, path2)
    #print('%.2f' % s.similar())
    # 写入文件
    with open(path3, 'w') as file_project:
        file_project.write('%.2f' % s.similar())
    print(0)
