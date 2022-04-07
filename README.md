# IEEE 爬虫

最近在做机器人相关的学习和研究，需要对论文的`Abstract`进行爬取，有些还需要爬`pdf`

所以现在写这个爬虫，也是希望能够群策群力，做一个爬虫的收集





## 代办网站

下边列举一些网站，是我现在觉得有必要研究的

### 网站

- [ ] arxiv.org
- [x] ieeexplore.com
- [ ] code-with-paper

### 期刊



- [ ] TRO（IEEE transactions on robotics）
- [ ] IJRR（international journal of robotics research）
- [ ] JFR(journal of field robotics)
- [ ] RAM(IEEE robotics & automation magazine)
- [ ] 代补充，你来写，我们来做



## 使用方法

#### ieeexplore.com

1. 找到你想要的所有文章的名字并将放入`csv`文件（命名为name_list.csv)（可以通过`excel`软件打开）中，具体的格式如下（一列即可

2. 在`cmd` `windows terminal` 等软件中运行下列命令

   `python ./get_link_from_ieee.py`

   等待他执行完毕，接着执行下列命令

​	`python ./get_paper_abstract.py`

3. 本地会生成一个`abstract.csv`的文件，打开即可看到文件对应的`abstract`



> 如果运行`python ./get_link_from_ieee.py`的时候出现`warning`的提示，说明没有找到文章，那些没有找到文章的会出现在`warning.csv`中