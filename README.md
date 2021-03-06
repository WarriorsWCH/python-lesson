
# Python系列教程(一):简介
### 一、Python发展历史
#### 起源
Python的作者，Guido von Rossum，荷兰人。1982年，Guido从阿姆斯特丹大学获得了数学和计算机硕士学位。然而，尽管他算得上是一位数学家，但他更加享受计算机带来的乐趣。用他的话说，尽管拥有数学和计算机双料资质，他总趋向于做计算机相关的工作，并热衷于做任何和编程相关的活儿。
在那个时候，Guido接触并使用过诸如Pascal、C、Fortran等语言。这些语言的基本设计原则是让机器能更快运行。在80年代，虽然IBM和苹果已经掀起了个人电脑浪潮，但这些个人电脑的配置很低。比如早期的Macintosh，只有8MHz的CPU主频和128KB的RAM，一个大的数组就能占满内存。所有的编译器的核心是做优化，以便让程序能够运行。为了增进效率，语言也迫使程序员像计算机一样思考，以便能写出更符合机器口味的程序。在那个时代，程序员恨不得用手榨取计算机每一寸的能力。有人甚至认为C语言的指针是在浪费内存。至于动态类型，内存自动管理，面向对象…… 别想了，那会让你的电脑陷入瘫痪。
这种编程方式让Guido感到苦恼。Guido知道如何用C语言写出一个功能，但整个编写过程需要耗费大量的时间，即使他已经准确的知道了如何实现。他的另一个选择是shell。Bourne Shell作为UNIX系统的解释器已经长期存在。UNIX的管理员们常常用shell去写一些简单的脚本，以进行一些系统维护的工作，比如定期备份、文件系统管理等等。shell可以像胶水一样，将UNIX下的许多功能连接在一起。许多C语言下上百行的程序，在shell下只用几行就可以完成。然而，shell的本质是调用命令。它并不是一个真正的语言。比如说，shell没有数值型的数据类型，加法运算都很复杂。总之，shell不能全面的调动计算机的功能。
Guido希望有一种语言，这种语言能够像C语言那样，能够全面调用计算机的功能接口，又可以像shell那样，可以轻松的编程。ABC语言让Guido看到希望。ABC是由荷兰的数学和计算机研究所开发的。Guido在该研究所工作，并参与到ABC语言的开发。ABC语言以教学为目的。与当时的大部分语言不同，ABC语言的目标是“让用户感觉更好”。ABC语言希望让语言变得容易阅读，容易使用，容易记忆，容易学习，并以此来激发人们学习编程的兴趣。比如下面是一段来自Wikipedia的ABC程序，这个程序用于统计文本中出现的词的总数：
HOW TO RETURN words document: PUT {} IN collection FOR line IN document: FOR word IN split line: IF word not.in collection: INSERT word IN collection RETURN collection

HOW TO用于定义一个函数。一个Python程序员应该很容易理解这段程序。ABC语言使用冒号和缩进来表示程序块。行 尾没有分号。for和if结构中也没有括号() 。赋值采用的是PUT，而不是更常见的等号。这些改动让ABC程序读起来像一段文字。 尽管已经具备了良好的可读性和易用性，ABC语言最终没有流行起来。在当时，ABC语言编译器需要比较高配置的电脑才能运行。而这些电脑的使用者通常精通计算机，他们更多考虑程序的效率，而非它的学习难度。除了硬件上的困难外，ABC语言的设计也存在一些致命的问题： 可拓展性差。ABC语言不是模块化语言。如果想在ABC语言中增加功能，比如对图形化的支持，就必须改动很多地方。 不能直接进行IO。ABC语言不能直接操作文件系统。尽管你可以通过诸如文本流的方式导入数据，但ABC无法直接读写文 件。输入输出的困难对于计算机语言来说是致命的。你能想像一个打不开车门的跑车么？ 过度革新。ABC用自然语言的方式来表达程序的意义，比如上面程序中的HOW TO 。然而对于程序员来说，他们更习惯 用function或者define来定义一个函数。同样，程序员更习惯用等号来分配变量。尽管ABC语言很特别，但学习难度 也很大。 传播困难。ABC编译器很大，必须被保存在磁带上。当时Guido在访问的时候，就必须有一个大磁带来给别人安装ABC编 译器。 这样，ABC语言就很难快速传播。 1989年，为了打发圣诞节假期，Guido开始写Python语言的编译器。Python这个名字，来自Guido所挚爱的电视剧Monty Python's Flying Circus。他希望这个新的叫做Python的语言，能符合他的理想：创造一种C和shell之间，功能全面，易学易用，可拓展的语言。Guido作为一个语言设计爱好者，已经有过设计语言的尝试。这一次，也不过是一次纯粹的hacking行为。

#### 一门语言的诞生
1991年，第一个Python编译器诞生。它是用C语言实现的，并能够调用C语言的库文件。从一出生，Python已经具有了 ：类，函数，异常处理，包含表和词典在内的核心数据类型，以及模块为基础的拓展系统。 Python语法很多来自C，但又受到ABC语言的强烈影响。来自ABC语言的一些规定直到今天还富有争议，比如强制缩进。 但这些语法规定让Python容易读。另一方面，Python聪明的选择服从一些惯例，特别是C语言的惯例，比如回归等号赋值。Guido认为，如果“常识”上确立的东西，没有必要过度纠结。 Python从一开始就特别在意可拓展性。Python可以在多个层次上拓展。从高层上，你可以直接引入. py文件。在底层，你可以引用C语言的库。Python程序员可以快速的使用Python写. py文件作为拓展模块。但当性能是考虑的重要因素时，Python程序员可以深入底层，写C程序，编译为.so文件引入到Python中使用。Python就好像是使用钢构建房一样，先规定好大的框架。而程序员可以在此框架下相当自由的拓展或更 改。 最初的Python完全由Guido本人开发。Python得到Guido同事的欢迎。他们迅速的反馈使用意见，并参与到Python的改进。Guido和一些同事构成Python的核心团队。他们将自己大部分的业余时间用于hack Python。随后，Python拓 展到研究所之外。Python将许多机器层面上的细节隐藏，交给编译器处理，并凸显出逻辑层面的编程思考。Python程 序员可以花更多的时间用于思考程序的逻辑，而不是具体的实现细节。这一特征吸引了广大的程序员。Python开始流行。

#### 时势造英雄
我们不得不暂停我们的Python时间，转而看一看瞬息万变的计算机行业。1990年代初，个人计算机开始进入普通家庭。Intel发布了486处理器，windows发布window 3.0开始的一系列视窗系统。计算机的性能大大提高。程序员开始关注计算机的易用性，比如图形化界面。

#### Windows 3.0
由于计算机性能的提高，软件的世界也开始随之改变。硬件足以满足许多个人电脑的需要。硬件厂商甚至渴望高需求软 件的出现，以带动硬件的更新换代。C++和Java相继流行。C++和Java提供了面向对象的编程范式，以及丰富的对象库。在牺牲了一定的性能的代价下，C++和Java大大提高了程序的产量。语言的易用性被提到一个新的高度。我们还记得 ，ABC失败的一个重要原因是硬件的性能限制。从这方面说，Python要比ABC幸运许多。 另一个悄然发生的改变是Internet。1990年代还是个人电脑的时代，windows和Intel挟PC以令天下，盛极一时。尽管Internet为主体的信息革命尚未到来，但许多程序员以及资深计算机用户已经在频繁使用Internet进行交流，比如 使用email和newsgroup。Internet让信息交流成本大大下降。一种新的软件开发模式开始流行：开源。程序员利用 业余时间进行软件开发，并开放源代码。1991年，Linus在comp.os.minix新闻组上发布了Linux内核源代码，吸引大批hacker的加入。Linux和GNU相互合作，最终构成了一个充满活力的开源平台。 硬件性能不是瓶颈，Python又容易使用，所以许多人开始转向Python。Guido维护了一个maillist，Python用户就通过邮件进行交流。Python用户来自许多领域，有不同的背景，对Python也有不同的需求。Python相当的开放，又容 易拓展，所以当用户不满足于现有功能，很容易对Python进行拓展或改造。随后，这些用户将改动发给Guido，并由Gu ido决定是否将新的特征加入到Python或者标准库中。如果代码能被纳入Python自身或者标准库，这将极大的荣誉。由于Guido至高无上的决定权，他因此被称为“终身的仁慈独裁者”。 Python被称为“Battery Included”，是说它以及其标准库的功能强大。这些是整个社区的贡献。Python的开发者来自不同领域，他们将不同领域的优点带给Python。比如Python标准库中的正则表达是参考Perl，而lambda, map, filter, reduce等函数参考了Lisp。Python本身的一些功能以及大部分的标准库来自于社区。Python的社 区不断扩大，进而拥有了自己的newsgroup，网站，以及基金。从Python 2.0开始，Python也从maillist的开发方式，转为完全开源的开发方式。社区气氛已经形成，工作被整个社区分担，Python也获得了更加高速的发展。 到今天，Python的框架已经确立。Python语言以对象为核心组织代码，支持多种编程范式，采用动态类型，自动进行内存回收。Python支持解释运行，并能调用C库进行拓展。Python有强大的标准库。由于标准库的体系已经稳定，所以Python的生态系统开始拓展到第三方包。这些包，如Django、web.py、wxpython、numpy、matplotlib、PIL，将Python升级成了物种丰富的热带雨林。

#### 启示录
Python崇尚优美、清晰、简单，是一个优秀并广泛使用的语言。Python在TIOBE排行榜中排行第八，它是Google的第三大开发语言，Dropbox的基础语言，豆瓣的服务器语言。Python的发展史可以作为一个代表，带给我许多启示。 在Python的开发过程中，社区起到了重要的作用。Guido自认为自己不是全能型的程序员，所以他只负责制订框架。如果问题太复杂，他会选择绕过去，也就是cut the corner。这些问题最终由社区中的其他人解决。社区中的人才是异常丰富的，就连创建网站，筹集基金这样与开发稍远的事情，也有人乐意于处理。如今的项目开发越来越复杂，越来越庞大，合作以及开放的心态成为项目最终成功的关键。 Python从其他语言中学到了很多，无论是已经进入历史的ABC，还是依然在使用的C和Perl，以及许多没有列出的其他 语言。可以说，Python的成功代表了它所有借鉴的语言的成功。同样，Ruby借鉴了Python，它的成功也代表了Python某些方面的成功。每个语言都是混合体，都有它优秀的地方，但也有各种各样的缺陷。同时，一个语言“好与不好”的评 判，往往受制于平台、硬件、时代等等外部原因。程序员经历过许多语言之争。其实，以开放的心态来接受各个语言，说不定哪一天，程序员也可以如Guido那样，混合出自己的语言。

#### 关键点常识
Python的发音与拼写
Python的意思是蟒蛇，源于作者喜欢的一部电视剧 (C呢？)
Python的作者是Guido van Rossum（龟叔）
Python是龟叔在1989年圣诞节期间，为了打发无聊的圣诞节而用C编写的一个编程语言
Python正式诞生于1991年
Python的解释器如今有多个语言实现，我们常用的是CPython（官方版本的C语言实现），其他还有Jython（可以运行在Java平台）、IronPython（可以运行在.NET和Mono平台）、PyPy（Python实现的，支持JIT即时编译）
Python目前有两个版本，Python2和Python3，最新版分别为2.7.12和3.5.2，现阶段大部分公司用的是Python2

### 二、Python优缺点
#### 优点
- 简单————Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样，尽管这个英语的要求非常严格！Python的这种伪代码本质是它最大的优点之一。它使你能够专注于解决问题而不是去搞明白语言本身。

- 易学————就如同你即将看到的一样，Python极其容易上手。前面已经提到了，Python有极其简单的语法。

- 免费、开源————Python是FLOSS（自由/开放源码软件）之一。简单地说，你可以自由地发布这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。FLOSS是基于一个团体分享知识的概念。这是为什么Python如此优秀的原因之一——它是由一群希望看到一个更加优秀的Python的人创造并经常改进着的。

- 高层语言————当你用Python语言编写程序的时候，你无需考虑诸如如何管理你的程序使用的内存一类的底层细节。

- 可移植性————由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。如果你小心地避免使用依赖于系统的特性，那么你的所有Python程序无需修改就可以在下述任何平台上面运行。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE甚至还有PocketPC、Symbian以及Google基于linux开发的Android平台！

- 解释性————这一点需要一些解释。一个用编译性语言比如C或C++写的程序可以从源文件（即C或C++语言）转换到一个你的计算机使用的语言（二进制代码，即0和1）。这个过程通过编译器和不同的标记、选项完成。当你运行你的程序的时候，连接/转载器软件把你的程序从硬盘复制到内存中并且运行。而Python语言写的程序不需要编译成二进制代码。你可以直接从源代码运行程序。在计算机内部，Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。事实上，由于你不再需要担心如何编译程序，如何确保连接转载正确的库等等，所有这一切使得使用Python更加简单。由于你只需要把你的Python程序拷贝到另外一台计算机上，它就可以工作了，这也使得你的Python程序更加易于移植。

- 面向对象————Python既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组合而成的对象构建起来的。与其他主要的语言如C++和Java相比，Python以一种非常强大又简单的方式实现面向对象编程。

- 可扩展性————如果你需要你的一段关键代码运行得更快或者希望某些算法不公开，你可以把你的部分程序用C或C++编写，然后在你的Python程序中使用它们。

- 丰富的库————Python标准库确实很庞大。它可以帮助你处理各种工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV文件、密码系统、GUI（图形用户界面）、Tk和其他与系统有关的操作。记住，只要安装了Python，所有这些功能都是可用的。这被称作Python的“功能齐全”理念。除了标准库以外，还有许多其他高质量的库，如wxPython、Twisted和Python图像库等等。

- 规范的代码————Python采用强制缩进的方式使得代码具有极佳的可读性。

#### 缺点
运行速度，有速度要求的话，用C++改写关键部分吧。
国内市场较小（国内以python来做主要开发的，目前只有一些web2.0公司）。但时间推移，目前很多国内软件公司，尤其是游戏公司，也开始规模使用他。
中文资料匮乏（好的python中文资料屈指可数）。托社区的福，有几本优秀的教材已经被翻译了，但入门级教材多，高级内容还是只能看英语版。
构架选择太多（没有像C#这样的官方.net构架，也没有像ruby由于历史较短，构架开发的相对集中。Ruby on Rails 构架开发中小型web程序天下无敌）。不过这也从另一个侧面说明，python比较优秀，吸引的人才多，项目也多。

### 三、Python应用场景
**Web应用开发**
Python经常被用于Web开发。比如，通过mod_wsgi模块，Apache可以运行用Python编写的Web程序。Python定义了WSGI标准应用接口来协调Http服务器与基于Python的Web程序之间的通信。一些Web框架，如Django,TurboGears,web2py,Zope等，可以让程序员轻松地开发和管理复杂的Web程序。

**操作系统管理、服务器运维的自动化脚本**
在很多操作系统里，Python是标准的系统组件。 大多数Linux发行版以及NetBSD、OpenBSD和Mac OS X都集成了Python，可以在终端下直接运行Python。有一些Linux发行版的安装器使用Python语言编写，比如Ubuntu的Ubiquity安装器,Red Hat Linux和Fedora的Anaconda安装器。Gentoo Linux使用Python来编写它的Portage包管理系统。Python标准库包含了多个调用操作系统功能的库。通过pywin32这个第三方软件 包，Python能够访问Windows的COM服务及其它Windows API。使用IronPython，Python程序能够直接调用.Net Framework。一般说来，Python编写的系统管理脚本在可读性、性能、代码重用度、扩展性几方面都优于普通的shell脚本。

**科学计算**
NumPy,SciPy,Matplotlib可以让Python程序员编写科学计算程序。

**桌面软件**
PyQt、PySide、wxPython、PyGTK是Python快速开发桌面应用程序的利器。

**服务器软件（网络软件）**
Python对于各种网络协议的支持很完善，因此经常被用于编写服务器软件、网络爬虫。第三方库Twisted支持异步网络编程和多数标准的网络协议(包含客户端和服务器)，并且提供了多种工具，被广泛用于编写高性能的服务器软件。

**游戏**
很多游戏使用C++编写图形显示等高性能模块，而使用Python或者Lua编写游戏的逻辑、服务器。相较于Python，Lua的功能更简单、体积更小；而Python则支持更多的特性和数据类型。

**构思实现，产品早期原型和迭代**
YouTube、Google、Yahoo!、NASA都在内部大量地使用Python。


# Python系列教程(二):数据类型、变量、运算符
### 一、数据类型

[数据类型](http://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)在[数据结构](http://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)中的定义是一个值的集合以及定义在这个值集上的一组操作。
简单来说，就是特指某一种数据，他们具有相同的特征，可以进行相同的操作。

#### 1.1整型 (int)   
**integer -> [ˈɪntɪdʒɚ]** 

Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

#### 1.2浮点数(float)
**float -> [flot]**

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

#### 1.3字符串(string)
**string ->  [strɪŋ]**

字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如`"I'm OK"`包含的字符是I，'，m，空格，O，K这6个字符。

#### 1.4布尔值(bool)
**bool -> [bu:l]**

布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值。

#### 1.5空值

空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值

### 二、变量

[变量](http://baike.baidu.com/item/%E5%8F%98%E9%87%8F)是用来存储值的所在处，它们有名字和数据类型。[变量](http://baike.baidu.com/item/%E5%8F%98%E9%87%8F)的数据类型决定了如何将代表这些值的位存储到计算机的内存中。
大家类比一下现实生活中，比如去超市买东西，往往咱们需要一个菜篮子，用来进行存储物品。
在Python中，存储一个数据，需要一个叫做变量的东西，如下示例:
```
# -*- coding:utf-8 -*-
num1 = 100 #num1就是一个变量，就好一个小菜篮子
num2 = 87  #num2也是一个变量
result = num1 + num2 #把num1和num2这两个"菜篮子"中的数据进行累加，然后放到 result变量中
```
**说明:**
- 所谓变量，可以理解为菜篮子，如果需要存储多个数据，最简单的方式是有多个变量，当然了也可以使用一个
- 程序就是用来处理数据的，而变量就是用来存储数据的

**怎样知道一个变量的类型呢？**
在python中，只要定义了一个变量，而且它有数据，那么它的类型就已经确定了，不需要咱们开发者主动的去说明它的类型，系统会自动辨别，可以使用type(变量的名字)，来查看变量的类型。
如下示例:
```
# -*- coding:utf-8 -*-
a = 101 # 整型
b = 1.11 # 浮点型
c = 'abc' # 字符串
d = True # 布尔值
e = 0xff00 # 十六进制整型
print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
```
**说明：print()是python3的语法，python2的语法是print后面不使用()，print type(a)**

打印信息：
```
<type 'int'>
<type 'float'>
<type 'str'>
<type 'bool'>
<type 'int'>
```
### 三、运算符
运算符用于执行程序代码运算，会针某几个数据来进行运算。例如：2+3,其操作数是2和3，而运算符则是“+”。
python支持以下几种运算符:

#### 3.1算术运算符

|运算符   |   描述   | 
|:------------:|:-------------:|
| + |    加| 
|- |	  减|	
|*|	  乘|	
|/|	  除|
|//|	取整除|
| %|	  取余|	
| **|	  幂|


#### 3.2赋值运算符

|运算符   |   描述   | 实例|
|:------------:|:---------: |:--------:|
| = |    赋值运算符| 把=号右边的结果给左边的变量 num=1+2*3 结果num的值为7|


#### 3.3复合赋值运算符

| 运算符      | 描述         |实例 |
|:-------------:|:-------------:|:-----:|
|+=	           |加法赋值运算符	|c += a 等效于 c = c + a|
|-=	           |减法赋值运算符	|c -= a 等效于 c = c - a|
|*=	           |乘法赋值运算符	|c *= a 等效于 c = c * a|
|/=	           |除法赋值运算符	|c /= a 等效于 c = c / a|
|%=    	   |取模赋值运算符	|c %= a 等效于 c = c % a|
|**=	           |幂赋值运算符	|c \*\*= a 等效于 c = c \*\* a|
|//=	           |取整除赋值运算符	|c //= a 等效于 c = c // a|


#### 3.4关系运算符

|运算符	|描述	|示例
|:------------:|:---------:|:--------:|
|==	|检查两个操作数的值是否相等，如果是则条件变为真。|	如a=3,b=3则（a == b) 为 true.
|!=	|检查两个操作数的值是否相等，如果值不相等，则条件变为真。|	如a=1,b=3则(a != b) 为 true.
|<>	|检查两个操作数的值是否相等，如果值不相等，则条件变为真。|	如a=1,b=3则(a <> b) 为 true。这个类似于 != 运算符
|>	|检查左操作数的值是否大于右操作数的值，如果是，则条件成立。|	如a=7,b=3则(a > b) 为 true.
|<	|检查左操作数的值是否小于右操作数的值，如果是，则条件成立。|如a=7,b=3则(a < b) 为 false.
|>=	|检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	|如a=3,b=3则(a >= b) 为 true.
|<=	|检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	|如a=3,b=3则(a <= b) 为 true.


#### 3.5逻辑运算符

|运算符	|逻辑表达式	|描述	|实例
|:------------:|:---------:|:--------:|:------:|
|and	|x and y	|布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	|(a and b) 返回 20。
|or	|x or y	|布尔"或" - 如果 x 是 True，它返回 True，否则它返回 y 的计算值。|	(a or b) 返回 10。
|not	|not x	|布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。|	not(a and b) 返回 False

# Python系列教程(三):标识符、关键字
### 一、标识符

标示符（IDentifier）是指用来标识某个实体的一个符号。在不同的应用环境下有不同的含义。
在日常生活中，标示符是用来指定某个东西、人，要用到它，他或她的名字；在数学中解方程时，我们也常常用到这样或那样的变量名或函数名；

**在编程语言中，标识符是用户编程时使用的名字，对于变量、常量、函数、语句块也有名字；我们统统称之为标识符。**

#### 1.1标示符的规则
**标示符由字母、下划线和数字组成，且数字不能开头**

示例如下：
```
   fromNo12
   my_Boolean
   Obj2
   myInt
   test1
   Mike2jack
   My_tExt
   _test
   jack_rose
```
错误示例如下：
```
   from#12
   my-Boolean
   2ndObj
   test!32
   haha(da)tt
   int
   jack&rose
   G.U.I
```
**注：python中的标识符是区分大小写的**
![图1.jpg](http://upload-images.jianshu.io/upload_images/2107063-f63a61ab571ef271.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 1.2命名规则

- **见名知意**

    起一个有意义的名字，尽量做到看一眼就知道是什么意思(提高代码可 读性) 比如: 名字 可以定义为 name , 定义学生可以使用 student

- **驼峰命名法**

    小驼峰式命名法（lower camel case）： 第一个单词以小写字母开始；第二个单词的首字母大写，例如：myName、aDog

    大驼峰式命名法（upper camel case）： 每一个单字的首字母都采用大写字母，例如：FirstName、LastName
![图2.jpg](http://upload-images.jianshu.io/upload_images/2107063-549b8bc8d63074cb.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

     不过在程序员中还有一种命名法比较流行，就是用下划线“_”来连接所有的单词，比如send_buf

### 二、关键字
- **什么是关键字**
    python一些具有特殊功能的标示符，这就是所谓的关键字
    关键字，是python已经使用的了，所以不允许开发者自己定义和关键字相同的名字的标示符

- **所有关键字**
```
     and     as      assert     break     class      continue    def     del
      elif    else    except     exec      finally    for         from    global
      if      in      import     is        lambda     not         or      pass
      print   raise   return     try       while      with        yield
```
**注：也就是说这些关键字不能作为标识符使用**

- **查看关键字**
```
import keyword
print (keyword.kwlist)
```
打印信息：
```
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

# Python系列教程(四):输入、输出
### 一、输出
在程序中输出就是打印信息，python中通过print函数打印变量、常量、表达式、函数的结果，将结果显示在控制台，方便开发人员查看，以及调试程序

示例如下：
```
print('hello, world')
print(300)
print(100 + 200)
print('100 + 200 =', 100 + 200)
```
#### 1.1格式化输出

**<1>格式化操作的目的**

比如有以下代码:


    pirnt("我今年10岁")
    pirnt("我今年11岁")
    pirnt("我今年12岁")
    ...
想一想:

>在输出年龄的时候，用了多次"我今年xx岁"，能否简化一下程序呢？？？

答:

>字符串格式化

**<2>什么是格式化**

看如下代码:


    age = 10
    print("我今年%d岁"%age)

    age += 1
    print("我今年%d岁"%age)

    age += 1
    print("我今年%d岁"%age)

    ...
在程序中，看到了%这样的操作符，这就是Python中格式化输出。

    age = 18
    name = "xiaohua"
    print("我的姓名是%s,年龄是%d"%(name,age))

**<3>常用的格式符号**

下面是完整的，它可以与％符号使用列表:

|            格式符号            |	                    转换            |
|:----------------------------------------------------------------:|:---------------------------------------:|
|%c                        	|字符
|%s                    	|通过str() 字符串转换来格式化
|%i	                        |有符号十进制整数
|%d                    	|有符号十进制整数
|%u                    	|无符号十进制整数
|%o                    	|八进制整数
|%x                    	|十六进制整数（小写字母）
|%X                    	|十六进制整数（大写字母）
|%e                    	|索引符号（小写'e'）
|%E                    	|索引符号（大写“E”）
|%f                    	|浮点实数
|%g                        	|％f和％e 的简写
|%G                    	|％f和％E的简写

#### 1.2 换行输出

在输出的时候，如果有\n那么，此时\n后的内容会在另外一行显示


    print("1234567890-------") # 会在一行显示

    print("1234567890\n-------") # 一行显示1234567890，另外一行显示-------

### 二、输入

用户通过键盘，想要向程序中输入内容，就是的输入

#### 2.1 raw_input()

在Python中，获取键盘输入的数据的方法是采用 raw_input 函

示例如下:

    password = raw_input("请输入密码:")
    print '您刚刚输入的密码是:', password
运行结果:
![图1.gif](http://upload-images.jianshu.io/upload_images/2107063-efcdd6abbc0d5235.gif?imageMogr2/auto-orient/strip)

**注意:**


- raw_input()的小括号中放入的是，提示信息，用来在获取数据之前给用户的一个简单提示
- raw_input()在从键盘获取了数据以后，会存放到等号右边的变量中
- raw_input()会把用户输入的任何值都作为字符串来对待


#### 2.2 input()

input()函数与raw_input()类似，但其接受的输入必须是表达式。
input()接受表达式输入，并把表达式的结果赋值给等号左边的变量
```
>>> a = input()
1+3
>>> a
4
```

**注：python3版本中，没有raw_input()函数，只有input()，并且 python3中的input与python2中的raw_input()功能一样**


# Python系列教程(五):if判断语句
#### 一、if判断语句
if语句是用来进行判断的，其使用格式如下：
``` 
if 要判断的条件: 
      条件成立时，要做的事情
```

示例1如下：
```
    age = 30
    print "------if判断开始------"
    if age>=18:
        print "我已经成年了"
    print "------if判断结束------"
```
运行结果:

```
    ------if判断开始------
    我已经成年了
    ------if判断结束------
```
示例2如下：
```
    age = 16
    print "------if判断开始------"
    if age>=18:
        print "我已经成年了"
    print "------if判断结束------"
```
运行结果:
```
    ------if判断开始------
    ------if判断结束------
```
以上2个示例仅仅是age变量的值不一样，结果却不同；能够看得出if判断语句的作用：就是当满足一定条件时才会执行那块代码，否则就不执行那块代码

**注意：代码的缩进为一个tab键，或者4个空格**

#### 二、if-else
想一想：
>在使用if的时候，它只能做到满足条件时要做的事情。那万一需要在不满足条件的时候，做某些事，该怎么办呢？

答：
>else

**使用格式**

    if 条件:
        满足条件时要做的事情1
        满足条件时要做的事情2
        满足条件时要做的事情3
        ...(省略)...
    else:
        不满足条件时要做的事情1
        不满足条件时要做的事情2
        不满足条件时要做的事情3
        ...(省略)...

示例如下：

    chePiao = 1 # 用1代表有车票，0代表没有车票
    if chePiao == 1:
        print("有车票，可以上火车")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有车票，不能上车")
        print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")
结果1：有车票的情况

    有车票，可以上火车
    终于可以见到Ta了，美滋滋~~~
结果2：没有车票的情况

    没有车票，不能上课
    亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~

#### 三、elif

想一想:

>if能完成当xxx时做事情
if-else能完成当xxx时做事情1，否则做事情2
如果有这样一种情况：当xxx1时做事情1，当xxx2时做事情2，当xxx3时做事情3，那该怎么实现呢？

答:

>elif


**elif的使用格式如下:**


    if xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3

说明:

当xxx1满足时，执行事情1，然后整个if结束
当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束

示例1如下：


    score = 77

    if score>=90 and score<=100:
        print('本次考试，等级为A')
    elif score>=80 and score<90:
        print('本次考试，等级为B')
    elif score>=70 and score<80:
        print('本次考试，等级为C')
    elif score>=60 and score<70:
        print('本次考试，等级为D')
    elif score>=0 and score<60:
        print('本次考试，等级为E')


可以和else一起使用

```
   if 性别为男性:
       输出男性的特征
       ...
   elif 性别为女性:
       输出女性的特征
       ...
   else:
       第三种性别的特征
       ...
```
说明:

当 “性别为男性” 满足时，执行 “输出男性的特征”的相关代码
当 “性别为男性” 不满足时，如果 “性别为女性”满足，则执行 “输出女性的特征”的相关代码
当 “性别为男性” 不满足，“性别为女性”也不满足，那么久默认执行else后面的代码，即 “第三种性别的特征”相关代码
elif必须和if一起使用，否则出错

#### 四、if嵌套

通过学习if的基本用法，已经知道了
当需要满足条件去做事情的这种情况需要使用if
当满足条件时做事情A，不满足条件做事情B的这种情况使用if-else
想一想：
>坐火车或者地铁的实际情况是：先进行安检如果安检通过才会判断是否有车票，或者是先检查是否有车票之后才会进行安检，即实际的情况某个判断是再另外一个判断成立的基础上进行的，这样的情况该怎样解决呢？

答：

>if嵌套

**if嵌套的格式**

    if 条件1:

        满足条件1 做的事情1
        满足条件1 做的事情2
        ...(省略)...

        if 条件2:
            满足条件2 做的事情1
            满足条件2 做的事情2
            ...(省略)...
说明:
外层的if判断，也可以是if-else
内层的if判断，也可以是if-else
根据实际开发的情况，进行选择

**if嵌套的应用**

示例如下：

    chePiao = 1     # 用1代表有车票，0代表没有车票
    daoLenght = 9     # 刀子的长度，单位为cm

    if chePiao == 1:
        print("有车票，可以进站")
        if daoLenght < 10:
            print("通过安检")
            print("终于可以见到Ta了，美滋滋~~~")
        else:
            print("没有通过安检")
            print("刀子的长度超过规定，等待警察处理...")
    else:
        print("没有车票，不能进站")
        print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")
结果1：chePiao = 1;daoLenght = 9

    有车票，可以进站
    通过安检
    终于可以见到Ta了，美滋滋~~~
结果2：chePiao = 1;daoLenght = 20

    有车票，可以进站
    没有通过安检
    刀子的长度超过规定，等待警察处理...
结果3：chePiao = 0;daoLenght = 9

    没有车票，不能进站
    亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~
结果4：chePiao = 0;daoLenght = 20

    没有车票，不能进站
    亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~



# Python系列教程(六):循环
要计算1+2+3，我们可以直接写表达式：1 + 2 + 3
要计算1+2+3+...+10，勉强也能写出来。
但是，要计算1+2+3+...+10000，直接写表达式就不可能了。
为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

Python的循环有两种，一种是while循环，另一种是for循环。

#### 一、while循环
**1.1 while循环的格式**

    while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...

示例如下

    i = 0
    while i<5:
        print("当前是第%d次执行循环"%(i+1))
        print("i=%d"%i)
        i+=1

结果:

    当前是第1次执行循环
    i=0
    当前是第2次执行循环
    i=1
    当前是第3次执行循环
    i=2
    当前是第4次执行循环
    i=3
    当前是第5次执行循环

**1.2 while循环应用**

1.计算1~100的累积和（包含1和100）

参考代码如下:
```
i = 1
sum = 0
while i<=100:
    sum = sum + i
    i += 1

print("1~100的累积和为:%d"%sum)
```

2.计算1~100之间偶数的累积和（包含1和100）

参考代码如下:

```
i = 1
sum = 0
while i<=100:
    if i%2 == 0:
        sum = sum + i
    i+=1

print("1~100的累积和为:%d"%sum)
```
**1.3 while循环嵌套**

类似if的嵌套，while嵌套就是：while里面还有while

**<1>while嵌套的格式**

    while 条件1:

        条件1满足时，做的事情1
        条件1满足时，做的事情2
        条件1满足时，做的事情3
        ...(省略)...

        while 条件2:
            条件2满足时，做的事情1
            条件2满足时，做的事情2
            条件2满足时，做的事情3
            ...(省略)...

**<2>while嵌套应用**
要求：打印如下图形：

    *
    * *
    * * *
    * * * *
    * * * * *
参考代码：

    i = 1
    while i<=5:

        j = 1
        while j<=i:
            print("* ",end='')
            j+=1

        print("\n")
        i+=1

#### 二、for循环

像while循环一样，for可以完成循环的功能。

在Python中 for循环可以遍历任何序列的项目，如一个列表或者一个字符串等。

for循环的格式


    for 临时变量 in 列表或者字符串等:
        循环满足条件时执行的代码
    else:
        循环不满足条件时执行的代码

示例如下：

    name = 'hello'

    for x in name:
        print(x)

运行结果如下:
```
h
e
l
l
o
```

#### 三、break

在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
```
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
```
上面的代码可以打印出1~100。

如果要提前结束循环，可以用break语句：
```
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```
执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。

可见break的作用是提前结束循环。

#### 四、continue

在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
```
n = 0
while n < 10:
    n = n + 1
    print(n)
```
上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
```
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```
执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。

可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。

**注意：**

- 循环是让计算机做重复任务的有效的方法。

- break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

- 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

- 有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

# Python系列教程(七):字符串
#### 1.1 字符串的格式
在python中，字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等

如下定义的变量b，存储的是字符串类型的值

    b = "hello python"
    或者
    b = 'hello python'

#### 1.2 字符串输出

示例如下：

    name = 'joy'
    text= '你好'
    phone='13344880909'

    print('--------------------------------------------------')
    print("姓名：%s"%name)
    print("职位：%s"%text)
   
结果:

    --------------------------------------------------
    姓名： joy
    内容： 你好
    电话： 13344880909
  
#### 1.3 下标索引

所谓“下标”，就是编号，就好比超市中的存储柜的编号，通过这个编号就能找到相应的存储空间

列表与元组支持下标索引好理解，字符串实际上就是字符的数组，所以也支持下标索引。


如果想取出部分字符，那么可以通过下标的方法，（注意python中下标从 0 开始）

```
   name = 'abcdef'

   print(name[0])
   print(name[1])
   print(name[2])
```
结果：
```
a
b
c
```
#### 1.4 字符串常见操作

如有字符串`mystr = 'hello world python world hello'`，以下是常见的操作

#### <1>find
检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

**语法：mystr.find(str, start=0, end=len(mystr))**
```
  mystr.find('python')
  mystr.find('python',0,10)
```
结果：
```
12
-1
```
#### <2>index
跟find()方法一样，只不过如果str不在 mystr中会报一个异常.

**语法：mystr.index(str, start=0, end=len(mystr)) **
```
  mystr.index('python')
  mystr.index('python',0,10)
```
结果：
```
12
File "/usercode/file.py", line 5, in <module>
    mystr.index('python',0,10)
ValueError: substring not found
```

#### <3>count
返回 str在start和end之间 在 mystr里面出现的次数

**语法：mystr.count(str, start=0, end=len(mystr))**
```
  mystr.count('python')
  mystr.count('l')
```
结果：
```
 1
 6
```

#### <4>replace
把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

**语法：mystr.replace(str1, str2,  mystr.count(str1))**
```
  mystr.replace('hello','HELLO')
  mystr.replace('hello','HELLO',1)
```
结果：
```
 HELLO worLd python worLd HELLO
 HELLO world python world hello
```

#### <5>split
以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

**语法：mystr.split(str,maxsplit ) **
```
  mystr.split(' ')
  mystr.replace(' ',2)
```
结果：
```
 ['hello', 'world', 'python', 'world', 'hello']
 ['hello', 'world', 'python world hello']
```
#### <6>capitalize
把字符串的第一个字符大写

**语法：mystr.capitalize()**
```
  mystr.capitalize()
```
结果：
```
 Hello world python world hello
```

#### <7>title
把字符串的每个单词首字母大写
**语法：mystr.title()**
```
  mystr.title()
```
结果：
```
 Hello World Python World Hello
```

#### <8>startswith
检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False

**语法：mystr.startswith(obj)**
```
  mystr.startswith('hello')
  mystr.startswith('ni')
```
结果：
```
  True
  False
```

#### <9>endswith
检查字符串是否以obj结束，如果是返回True,否则返回 False.

**语法：mystr.endswith(obj)**
```
  mystr.endswith('hello')
  mystr.endswith('Python')
```
结果：
```
  True
  False
```
#### <10>lower
转换 mystr 中所有大写字符为小写

**语法：mystr.lower()**
```
  mystr.lower()
```
结果：
```
  hello world python world hello
```
#### <11>upper
转换 mystr 中的小写字母为大写

**语法：mystr.upper()**
```
  mystr.upper()
```
结果：
```
  HELLO WORLD PYTHON WORLD HELLO
```
#### <12>ljust
返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

**语法：mystr.ljust(width)** 
```
  mystr.ljust(30)
```
结果：
```
  'hello world python world hello          '
```
#### <13>rjust
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

**语法：mystr.rjust(width)**    
```
  mystr.rjust(40)
```
结果：
```
 '          hello world python world hello'
```
#### <14>center
返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

**语法：mystr.center(width)**   
```
  mystr.center(40)
```
结果：
```
 '     hello world python world hello     '
```
#### <15>lstrip
删除 mystr 左边的空白字符

**语法：mystr.lstrip()**
```
a = "  abc "
a.lstrip()
```
结果
```
'abc '
```
#### <16>rstrip
删除 mystr 字符串末尾的空白字符
```
a = "  abc "
a.rstrip()
```
结果
```
' abc'
```
**语法：mystr.rstrip()**    

#### <17>strip
删除mystr字符串两端的空白字符
```
a = "  abc "
a.strip()
```
结果
```
'abc'
```

#### <18>rfind
类似于 find()函数，不过是从右边开始查找.

**语法：mystr.rfind(str, start=0,end=len(mystr) )**
```
  mystr.rfind('python')
  mystr.rfind('python',0,10)
```
结果：
```
12
-1
```

#### <19>rindex
类似于 index()，不过是从右边开始.

**语法：mystr.rindex( str, start=0,end=len(mystr))**
```
  mystr.rindex('python')
  mystr.rindex('python',0,10)
```
结果：
```
12
报错：ValueError: substring not found
```
#### <20>partition
把mystr以str分割成三部分,str前，str和str后

**语法：mystr.partition(str)**
```
  mystr.partition('world')
```
结果：
```
 ('hello ', 'world', ' python world hello')
```
#### <21>rpartition
类似于 partition()函数,不过是从右边开始.

**语法：mystr.rpartition(str)**
```
  mystr.rpartition('world')
```
结果：
```
 ('hello world python ', 'world', ' hello')
```
#### <22>splitlines
按照行分隔，返回一个包含各行作为元素的列表

**语法：mystr.splitlines()**  
```
  mystr.splitlines()
```
结果：
```
['hello world python world hello']
```
#### <23>isalpha
如果 mystr 所有字符都是字母 则返回 True,否则返回 False

**语法：mystr.isalpha()** 
```
  mystr.isalpha()
```
结果：
```
False
```
#### <24>isdigit
如果 mystr 只包含数字则返回 True 否则返回 False.

**语法：mystr.isdigit() **
```
  mystr.isdigit()
```
结果：
```
False
```
#### <25>isalnum
如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False

**语法：mystr.isalnum()**
```
  mystr.isalnum()
```
结果：
```
False
```
#### <26>isspace
如果 mystr 中只包含空格，则返回 True，否则返回 False.

**语法：mystr.isspace()**  
```
  mystr.isspace()
```
结果：
```
False
```
#### <27>join
mystr 中每个字符后面插入str,构造出一个新的字符串

**语法：mystr.join(str)**
```
  '-'.join(mystr)
```
结果：
```
h-e-l-l-o- -w-o-r-l-d- -p-y-t-h-o-n- -w-o-r-l-d- -h-e-l-l-o
```

# Python系列教程(八):list 列表、tuple 元组

## 一、list 列表

Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

比如，列出班里所有同学的名字，就可以用一个list表示：
```
>>>names= ['xiaoming', 'xiaoli', 'xiaohong']
>>>names
['xiaoming', 'xiaoli', 'xiaohong']
```
变量names就是一个list。用**len()**函数可以获得list元素的个数：
```
>>> len(names)
3
```
用索引来访问list中每一个位置的元素，记得索引是从0开始的：
```
>>> names[0]
'xiaoming'
>>> names[1]
'xiaoli'
>>> names[2]
'xiaohong'
>>> names[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
**注：**当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是**len(classmates) - 1**。

如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
```
>>> names[-1]
'xiaohong'
```
以此类推，可以获取倒数第2个、倒数第3个：
```
>>> names[-2]
'xiaoli'
>>> names[-3]
'xiaoming'
>>> names[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
当然，倒数第4个就越界了。


### 二、list 列表的相关操作

列表中存放的数据是可以进行修改的，比如"增"、"删"、"改""

**<1>添加元素("增"append, extend, insert)**

- **append**
通过append可以向列表添加元素

示例如下:

    #定义变量A，默认有3个元素
    A = ['xiaoWang','xiaoZhang','xiaoHua']

    print("-----添加之前，列表A的数据-----")
    for tempName in A:
        print(tempName)

    #提示、并添加元素
    temp = input('请输入要添加的学生姓名:')
    A.append(temp)

    print("-----添加之后，列表A的数据-----")
    for tempName in A:
        print(tempName)
结果:

- **extend**
通过extend可以将另一个集合中的元素逐一添加到列表中

```
>>> a = [1, 2]
>>> b = [3, 4]
>>> a.append(b)
>>> a[1, 2, [3, 4]]
>>> a.extend(b)
>>> a[1, 2, [3, 4], 3, 4]
```
- **insert**
insert(index, object) 在指定位置index前插入元素object

```
>>> a = [0, 1, 2]
>>> a.insert(1, 3)
>>> a[0, 3, 1, 2]
```
**<2>修改元素("改")**

修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改
示例如下:
```
 #定义变量A，默认有3个元素 
 A = ['xiaoWang','xiaoZhang','xiaoHua']
 print("-----修改之前，列表A的数据-----") 
 for tempName in A: print(tempName) #修改元素 
    A[1] = 'xiaoLu'
    print("-----修改之后，列表A的数据-----") 
 for tempName in A: 
    print(tempName)
```
结果:
```
-----修改之前，列表A的数据----- 
xiaoWang 
xiaoZhang 
xiaoHua
 -----修改之后，列表A的数据----- 
xiaoWang 
xiaoLu 
xiaoHua
```

**<3>查找元素("查"in, not in, index, count)**

python中查找的常用方法为：
**in（存在）**,如果存在那么结果为true，否则为false
**not in（不存在）**,如果不存在那么结果为true，否则false

示例如下：
```
#待查找的列表 
nameList = ['xiaoWang','xiaoZhang','xiaoHua'] #获取用户要查找的名字 
findName = input('请输入要查找的姓名:') #查找是否存在 

if findName in nameList: 
    print('在字典中找到了相同的名字') 
else: 
    print('没有找到')
```
结果1：(找到)
![01-第3天-3.gif](http://upload-images.jianshu.io/upload_images/2107063-e94b892204ccedd9.gif?imageMogr2/auto-orient/strip)

结果2：(没有找到)
![01-第3天-4.gif](http://upload-images.jianshu.io/upload_images/2107063-f43f0484f56fc088.gif?imageMogr2/auto-orient/strip)

说明：
in的方法只要会用了，那么not in也是同样的用法，只不过not in判断的是不存在

- **index, count**
index和count与字符串中的用法相同

```
>>> a = ['a', 'b', 'c', 'a', 'b']
>>> a.index('a', 1, 3) # 注意是左闭右开区间
Traceback (most recent call last): File "<stdin>", line 1, in <module>
ValueError: 'a' is not in list
>>> a.index('a', 1, 4)3
>>> a.count('b')2
>>> a.count('d')0
```

**<4>删除元素("删"del, pop, remove)**

类比现实生活中，如果某位同学调班了，那么就应该把这个条走后的学生的姓名删除掉；在开发中经常会用到删除这种功能。

列表元素的常用删除方法有：
- **del**：根据下标进行删除
- **pop**：删除最后一个元素
- **remove**：根据元素的值进行删除

示例如下:(del)
```
 movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情'] 
 print('------删除之前------') 

 for tempName in movieName: 
      print(tempName)

 del movieName[2] 
 print('------删除之后------')

 for tempName in movieName: 
     print(tempName)
```
结果:
```
------删除之前------ 
加勒比海盗
 骇客帝国 
第一滴血 
指环王 
霍比特人 
速度与激情 
------删除之后------ 
加勒比海盗 
骇客帝国 
指环王
霍比特人 
速度与激情
```

示例如下:(pop)
```
 movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情'] 
 print('------删除之前------') 

 for tempName in movieName: 
     print(tempName)
 movieName.pop() 
 print('------删除之后------') 

 for tempName in movieName: 
     print(tempName)
```
结果:
```
------删除之前------ 
加勒比海盗 
骇客帝国 
第一滴血 
指环王 
霍比特人
 速度与激情 
------删除之后------ 
加勒比海盗 
骇客帝国 
第一滴血 
指环王 
霍比特人
```

示例如下:(remove)
```
 movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
 print('------删除之前------') 

 for tempName in movieName: 
     print(tempName) 

 movieName.remove('指环王') 
 print('------删除之后------') 

 for tempName in movieName: 
     print(tempName)
```
结果:
```
------删除之前------ 
加勒比海盗 
骇客帝国 
第一滴血 
指环王 
霍比特人
 速度与激情 
------删除之后------ 
加勒比海盗 
骇客帝国 
第一滴血 
霍比特人 
速度与激情
```
**<5>排序(sort, reverse)**

- **sort**方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。

- **reverse**方法是将list逆置。

```
>>> a = [1, 4, 2, 3]
>>> a[1, 4, 2, 3]
>>> a.reverse()
>>> a[3, 2, 4, 1]
>>> a.sort()
>>> a[1, 2, 3, 4]
>>> a.sort(reverse=True)
>>> a[4, 3, 2, 1]
```
### 三、列表的嵌套

#### 3.1 列表嵌套

类似while循环的嵌套，列表也是支持嵌套的

一个列表中的元素又是一个列表，那么这就是列表的嵌套
``` 
schoolNames = [['北京大学','清华大学'], 
               ['南开大学','天津大学','天津师范大学'],
               ['山东大学','中国海洋大学']]
```
#### 3.2  应用

一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
```
#encoding=utf-8

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)    
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)
```
运行结果如下:
```
办公室1的人数为：4
ABCE
--------------------
办公室2的人数为：3
DGH
--------------------
办公室3的人数为：1
F
--------------------
```

### 四、元组

Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
```
>>> tuple= ('abc',66,3.14)
>>> tuple
('abc',66,3.14)
```
**<1>索引查找元素**
```
>>> tuple=('abc',66,3.14)
>>> tuple[0]
'abc'
>>> tuple[1]
66
>>> tuple[2]
3.14
```
**<2>修改元组**
```
>>> tuple=('abc',66,3.14)
>>> tuple[0] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
**说明： python中不允许修改元组的数据，包括不能删除其中的元素。**

**<3>元组的内置函数count, index**

index和count与字符串和列表中的用法相同
```
>>> a = ('a', 'b', 'c', 'a', 'b')
>>> a.index('a', 1, 3) # 注意是左闭右开区间
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
>>> a.index('a', 1, 4)
3
>>> a.count('b')
2
>>> a.count('d')
0
```

# Python系列教程(九):dict 字典

### 一、dict 字典

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
```
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
```
给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。

如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
 ```
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
```
说明：

- 字典和列表一样，也能够存储多个数据
- 列表中找某个元素时，是根据下标进行的
- 字典中找某个元素时，是根据'名字'（就是冒号:前面的那个值，例如上面代码中的'Michael'、'Bob'、'Tracy'）
- 字典的每个元素由2部分组成，键:值。例如 'Tracy':85 ,'name'为键，85为值

若访问不存在的键，则会报错：
```
>>> d ['jack']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'jack'
```
在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值：
```
>>> score= d .get('jack')
>>> score#'age'键不存在，所以jack为None
>>> type(score)
<type 'NoneType'>
>>> score= d .get('jack', 18) # 若d 中不存在'age'这个键，就返回默认值18
>>> score
18
```
### 二、dict字典的常见操作
#### 2.1 修改元素
字典的每个元素中的数据是可以修改的，只要通过key找到，即可修改

示例代码:

    info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

    info['id'] = 200

    print('修改之后的id为%d:'%info['id'])

结果:
```
修改之后的id为200:
```

#### 2.2 添加元素
访问不存在的元素

    info = {'name':'班长', 'sex':'f', 'address':'China'}

    print('id为:%d'%info['id'])

结果:
```
Traceback (most recent call last):
  File "/usercode/file.py", line 5, in <module>
    print('id为:%d'%info['id'])
KeyError: 'id'

```

如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素

添加新的元素

    info = {'name':'班长', 'sex':'f', 'address':'China'}

    # print('id为:%d'%info['id'])#程序会终端运行，因为访问了不存在的键

    info['id'] = 111

    print('添加之后的id为:%d'%info['id'])

结果:
```
添加之后的id为:111
```

#### 2.3 删除元素

对字典进行删除操作，有一下几种：

- del
- clear()
- pop()

del删除指定的元素：


    info = {'name':'班长', 'sex':'f', 'address':'China'}

    print('删除前,%s'%info['name'])

    del info['name']

    print('删除后,%s'%info['name'])

结果：
```
删除前,班长
Traceback (most recent call last):
  File "/usercode/file.py", line 9, in <module>
    print('删除后,%s'%info['name'])
KeyError: 'name'
```
del删除整个字典：


    info = {'name':'monitor', 'sex':'f', 'address':'China'}

    print('删除前,%s'%info)

    del info

    print('删除后,%s'%info)

结果：
```
删除前,{'address': 'China', 'name': 'monitor', 'sex': 'f'}
Traceback (most recent call last):
  File "/usercode/file.py", line 9, in <module>
    print('删除后,%s'%info)
NameError: name 'info' is not defined
```
clear清空整个字典：


    info = {'name':'monitor', 'sex':'f', 'address':'China'}

    print('清空前,%s'%info)

    info.clear()

    print('清空后,%s'%info)

结果：
```
清空前,{'address': 'China', 'name': 'monitor', 'sex': 'f'}
清空后,{}
```
pop删除指定的元素：
```
info = {'name':'monitor', 'sex':'f', 'address':'China'}

print('删除前,%s'%info)

info.pop('name')

print('删除后,%s'%info)
```
结果：
```
删除前,{'address': 'China', 'name': 'monitor', 'sex': 'f'}
删除后,{'address': 'China', 'sex': 'f'}
```

#### 2.4 keys
返回一个包含字典所有KEY的列表
```
>>>info = {'name':'monitor', 'sex':'f', 'address':'China'}
>>>print(info.keys())
['address', 'name', 'sex']
```
#### 2.5 values
返回一个包含字典所有value的列表
```
>>>info = {'name':'monitor', 'sex':'f', 'address':'China'}
>>>print(info.values())
['China', 'monitor', 'f']
```
#### 2.6 items
返回一个包含所有（键，值）元祖的列表
```
>>>info = {'name':'monitor', 'sex':'f', 'address':'China'}
>>>print(info.items())
[('address', 'China'), ('name', 'monitor'), ('sex', 'f')]
```
#### 2.7 has_key
dict.has_key(key)如果key在字典中，返回True，否则返回False
```
>>>info = {'name':'monitor', 'sex':'f', 'address':'China'}
>>>print(info.has_key('name'))
True
>>>print(info.has_key('n'))
False
```

**请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。**

和list比较，dict有以下几个特点：

- 查找和插入的速度极快，不会随着key的增加而变慢；
- 需要占用大量的内存，内存浪费多。

而list相反：

- 查找和插入的时间随着元素的增加而增加；
- 占用空间小，浪费内存很少。
- 所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

```
>>> key = [1, 2, 3]
>>> d[key] = 'list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```