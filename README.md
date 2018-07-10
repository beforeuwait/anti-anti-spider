 针对工作中遇到的各类有意思的难的简单的反爬虫
 
 - 只提供思路
 

##目录 
	
		.
		├── README.md
		└── guazi
		    └── guazi.py


> 瓜子二手车

在首次进入页面后，会进行js验证，生成一个antipas字段，放在cookie里

status_code 遇到203 及代表要js验证

笔者发现，一旦 User-Agent换了以及切换Ip都会触发
