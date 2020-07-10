#!/usr/bin/env python
# coding: utf-8

# In[26]:


class Information():
    
    def __init__(self, name, DataType, size):
        print("sinifin init fonksiyonu cagrildi..")
        self.name = name
        self.DataType = DataType
        self.size = size
        
    def DataInfo(self):
        print(""" Verinin özelikleri
                  feature name: {}
                  data type: {}
                  No of missing values:{} """.format(self.name, self.DataType, self.size))

        

class DataCleaning():
    
    def __init__(self):
        print("DataCleaning init fonksiyonu cagrildi..")
        
    def Cleaning(self):
        print("veri temizlendi")

        
        
class DataReduction():
    
    def __init__(self):
        print("DataReduction init fonksiyonu cagrildi..")
        
    def Reducing(self):
        print("veri azaltildi")
        
        

class DataConversion():
    
    def __init__(self):
        print("DataConversion init fonksiyonu cagrildi..")
        
    def Conversion(self):
        print("veri donusturuldu")
        
        
        
class DataVisualization():
    
    def __init__(self):
        print("DataVisualization init fonksiyonu cagrildi..")
        
    def boxPlot():
        pass
    
    def histogram():
        pass
    
    def chart():
        pass
    
    def TreeMaps():
        pass
    
    def Visualization(self):
        print("veri gorsellestirildi")
        
        

        
class PreProcess():
    
    def __init__(self):
        print("PreProcess init fonksiyonu cagrildi..")     
        
    def  preprocess(self):
        print("veri hazirlandi")
        
        
        
        
class Evaluation():
    
    def __init__(self):
        print("Evaluation init fonksiyonu cagrildi..")        
        
    def  AppEvaluation(self):
        print("uygulama değerlendirildi")


# In[ ]:




