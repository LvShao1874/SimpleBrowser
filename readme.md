### 简介
SimpleBrowser是个人基于python selenium简化封装的工具类.
因为Selnium执行的过程中会面临更多不确定的因素,比如因为网速导致的元素加载过慢,这会导致程序非常不稳定.
因此基于设计模式(外观模式),对selenium常用方法进行进一步封装,提供更加稳定、简单易用地使用selenium.
目前实现方法:
1. 查找单个元素
2. 查找单个可点击元素
3. 查找多个元素
4. 对指定元素输入数据
5. 点击指定元素
6. 请求指定url
7. 滚动到指定元素
8. 新建tag,切换tag
9. 获取浏览器page_source
10. 设置浏览器大小
11. 提供常用的静态方法,取得虚拟Display对象,用于在服务器上运行(无实体屏幕)
12. 退出浏览器,正确释放资源
### 使用方法:
```
初始化:
display = SimpleBrowser.get_virtual_display(False, 1300, 1000)
display.start()     ## 启动虚拟屏幕
driver = webdriver.Chrome(chrome_options=chrome_options)     ## 常规实例化你想要的driver
driver = SimpleBrowser(driver)    ##获得增强简化后的driver
driver.quit()   ## 关闭浏览器,释放资源
display.stop()      ## 关闭虚拟屏幕,释放资源
```

### 测试
你可以参考test.py 执行一下代码,看看实际运行情况~