import os

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk1.8.0_112'
os.environ['SPARK_HOME'] = r'E:\weizhi\Python\code\spark-2.3.0-bin-hadoop2.6'
os.environ['HADOOP_HOME'] = r'E:\weizhi\Python\code\hadoop-common-2.2.0-bin-master'
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

sparkConf = SparkConf().setAppName("sougou text").setMaster("local")

sc = SparkContext(conf=sparkConf)

sougou = sc.textFile("E:\SogouQ.txt")

# print(sougou.count())
# print(sougou.take(5))
def f(aa):
    if len(aa)==5:
        return aa

# filterSG = sougou.map(_.split("\t")).filter(_.length == 6)
# print(sougou.take(5))
filterSG = sougou.map(lambda x: x.split("\t"))

aa = filterSG.map(lambda x: f(x))
# print(filterSG.take(5))

# print(aa.count())

# rdd = aa.filter(_(3).toInt == 1).filter(_(4).toInt == 1)

# print(rdd.take(3))

# print(rdd.count())

# rdd.map(lambda x:x= > (x(1), 1)).reduceByKey(_ + _).map(x= > (x._2, x._1)).sortByKey(false).map(x= > (
# x._2, x._1)).saveAsTextFile("G:\\sgresult")
