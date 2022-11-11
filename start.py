# encoding: utf-8
"""
Author: gugan1
Info：使用无头浏览器批量下载全屏网页
CreateTime: 2022年11月9日
UpdateTime: 2022年11月9日
tips：要使用全屏截图功能，必须使用无头浏览器，这样才能设置浏览器的大小超过当前电脑屏幕的大小
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import re

if __name__ == '__main__':
    url = "https://support.i2group.com/s/article/"
    #设置chrome开启的模式，headless就是无界面模式
    #一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度
    chrome_options = Options()
    chrome_options.add_argument('headless')
    browse = webdriver.Chrome(chrome_options=chrome_options)
    #可以提前用bp抓包获取到不为空的id，也可以直接range出id
    id = [
        1000, 1003, 1004, 1005, 1009, 1010, 1013, 1015, 1016, 1017, 1018, 1023,
        1025, 1026, 1027, 1028, 1029, 1030, 1033, 1881, 1882, 1883, 1884, 1886,
        1887, 1888, 1889, 1893, 1894, 1895, 1896, 1897, 1899, 1900, 1901, 1902,
        1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914,
        1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1924, 1925, 1926, 1927,
        1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939,
        1940, 1941, 1942, 1943, 1944, 1945, 1946, 1949, 1950, 1951, 1953, 1954,
        1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966, 1967,
        1968, 1969, 1971, 1973, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,
        1983, 1985, 1987, 1988, 1989, 1990, 1991, 1992, 1994, 1995, 1996, 1998,
        1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011,
        2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024,
        2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036,
        2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2049,
        2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2060, 2061, 2062,
        2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074,
        2075, 2077, 2079, 2080, 2081, 2083, 2084, 2086, 2088, 2089, 2091, 2093,
        2097, 2098, 2099, 2100, 2101, 2102, 2104, 2106, 2107, 2108, 2110, 2111,
        2112, 2113, 2118, 2119, 2120, 2121, 2124, 2125, 2128, 2131, 2137, 2138,
        2139, 2141, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152,
        2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2165,
        2166, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2176, 2177, 2178, 2180,
        2182, 2183, 2184, 2185, 2186, 2187, 2189, 2190, 2194, 2195, 2196, 2199,
        2200, 2201, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2213, 2214,
        2219, 2220, 2225, 2240, 2242, 2256, 2259, 2260, 2289, 2290, 2291, 2292,
        2298, 2299, 2301, 2302, 2304, 2305, 2306, 2307, 2310, 2312, 2313, 2314,
        2317, 2319, 2321, 2322, 2323, 2324, 2325, 2327, 2330, 2332, 2336, 2337,
        2340, 2343, 2351, 2352, 2353, 2354, 2355, 2358, 2359, 2360, 2361, 2365,
        2366, 2370, 2372, 2373, 2374, 2377, 2378, 2379, 2380, 2381, 2382, 2385,
        2388, 2391, 2392, 2393, 2394, 2396, 2398, 2399, 2406, 2407, 2408, 2409,
        2410, 2411, 2415, 2417, 2418, 2419, 2420, 2421, 2423, 2424, 2429, 2430,
        2431, 2432, 2433, 2436, 2437, 2438, 2440, 2442, 2444, 2446, 2448, 2449,
        2450, 2452, 2453, 2454, 2455, 2456, 2457, 2458, 2460, 2461, 2462, 2463,
        2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474, 2475,
        2477, 2478, 2479, 2480, 2482, 2483, 2484, 2488, 2490, 2491, 2492, 2493,
        2495, 2496, 2497, 2498, 2500, 2501, 2503, 2504, 2506, 2507, 2508, 2509,
        2511, 2512, 2513
    ]
    # id=range(1,1000)
    for i in id:
        print("对第" + str(i) + "页进行截图")
        browse.get(url + str(i))
        time.sleep(20)
        #设置启动时候浏览器的大小，如果不设置，默认大小就是800*600
        browse.set_window_size(800, 1000)
        try:
            if browse.page_source.__len__() > 258300:

                file_name = browse.title
                file_name = str(i) + "_" + re.sub(r'/|\\|:|\*|\?|\"|<|>|\|| ',
                                                  "_", file_name) + ".png"
                #用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
                width = browse.execute_script(
                    "return document.documentElement.scrollWidth")
                height = browse.execute_script(
                    "return document.documentElement.scrollHeight")
                #将浏览器的宽高设置成刚刚获取的宽高
                browse.set_window_size(width, height)
                #保存截图
                browse.save_screenshot(r"./download/" + file_name)
                with open("./log.txt", 'a') as log_file:
                    log_file.write(file_name + '\n')
        except:
            print(str(i))

    print("well done!")
