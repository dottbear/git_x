import numpy as np
import math

##七大晶系晶面间距及晶面夹角计算
##dx:单斜(monoclinic)   sx:三斜(triclinic)   zj:正交(orthorhombic)   lj:六角(hexagonal)
##lx:菱形(trigonal)   sf:四方(tetragonal)   lf:立方(cubic)
##cry_info类，lf（立方）类，zj（正交）类，类里面的dist和ang方法分别计算晶面的间距和夹角

class cry_info:

    def __init__(self,*arg):
        self.a,self.b,self.c,self.x,self.y,self.z = arg
        a,b,c,x,y,z=self.a,self.b,self.c,self.x,self.y,self.z
       

##    def dist(self):
##        return self.a*self.b  #在该类中或子类中要访问a,b时，只能self.a,self.b吗，有没有简便一点的方法？
        
    def sq(self,e,f,g):
        return e**2+f**2+g**2

    def cj(self,h1,k1,l1,h2,k2,l2):
        return h1*h2+k1*k2+l1*l2

    def fbc(self,h,k,l):
        return h**2/self.a**2+k**2/self.b**2+l**2/self.c**2


        
class lf(cry_info):
    def dist(self,*arg):
        self.h,self.k,self.l=arg
        h,k,l=self.h,self.k,self.l
        
        dist=np.sqrt(1/((self.sq(h,k,l))/(self.a**2)))*10
        return dist
    def ang(self,*arg):
        self.h1,self.k1,self.l1,self.h2,self.k2,self.l2=arg
        h1,k1,l1,h2,k2,l2=self.h1,self.k1,self.l1,self.h2,self.k2,self.l2
        ang=np.rad2deg(np.arccos(self.cj(h1,k1,l1,h2,k2,l2)/np.sqrt(self.sq(h1,k1,l1)+np.sqrt(self.sq(h2,k2,l2)))))
        return ang

class zj(cry_info):
    def dist(self,*arg):
        self.h,self.k,self.l=arg
        h,k,l=self.h,self.k,self.l
        a,b,c = self.a,self.b,self.c
        dist=np.sqrt(1/(self.fbc(h,k,l)))
        return dist
    def ang(self,*arg):
        self.h1,self.k1,self.l1,self.h2,self.k2,self.l2=arg
        h1,k1,l1,h2,k2,l2=self.h1,self.k1,self.l1,self.h2,self.k2,self.l2
        a,b,c = self.a,self.b,self.c
        ang=np.rad2deg(np.arccos((h1*h2/a**2+k1*k2/b**2+l1*l2/c**2)/(np.sqrt(self.fbc(h1,k1,l1))*np.sqrt(self.fbc(h2,k2,l2)))))
        return ang


##输入6个晶格参数，并将其转化成元祖类型，便后续传参使用！

zll='4.735 6.025 5.21 90 90 90'

choice=input('请选择输入6个晶格参数（任意键），或输入已有录入数据（zll）:\n').strip().lower()

if choice=='zll':
    jgcs=list(map(float,zll.split(' ')))
else:
    sr1=input('请你分别输入你想查询晶系的缩写，6个晶格参数：\n').strip().lower()
    jgcs=list(map(float,sr1.split(' ')))

def jmjianju():
    jmjj=input('请输入你想查询的晶面，空格隔开：').strip().lower()
    jmjj=list(map(int,jmjj.split(' ')))
    return tuple(jmjj)

def jmjiajiao():
    jmjj=input('请输入你想查询的两个晶面，空格隔开：').strip().lower()
    jmjj=list(map(int,jmjj.split(' ')))
    return tuple(jmjj)

pd=True
while pd:
    crystyle=input('''请输入你想查询的晶体类型(缩写)：lf-立方，zj-正交,q-退出:''').strip().lower()   
    
    if crystyle == 'lf':
        print('你正在查询立方晶系')
        cx1=int(input('查询晶面间距请输入1，查询晶面夹角请输入2:，q-退出')).strip().lower()

        ##创建lf实例
        lf1=lf(*jgcs)   
        if cx1 == 1:
            ##打印计算的d值
            d=lf1.dist(*jmjianju())     
            print('晶面间距是:%.2f'%d)   
            
        elif cx1 == 2:    
            ##打印计算的夹角值
            a=lf2.ang(*jmjiajiao())
            print('夹角是:%.2f'%a)
            
        elif cx1 == 'q':
            pd=False
            break
        else:
            continue
          
    elif crystyle == 'zj':
        print('你正在查询正交晶系')
        cx1=int(input('查询晶面间距输入1，查询晶面夹角输入2:,q-退出')).strip().lower()
        
        ##创建sf实例
        zj1=zj(*jgcs)
        if cx1 == 1:         
            ##打印计算的d值
            d=zj1.dist(*jmjianju())
            print('晶面间距是:%.2f'%d)
            
        elif cx1 == 2:
            ##打印计算的夹角值
            a=zj1.ang(*jmjiajiao())
            print('夹角是:%.2f'%a)
            
        elif cx1 == 'q':
            pd=False
            break
        else:
            continue
        
    elif crystyle == 'q':
        print('正常退出')
        pd=False
    else:
        print('输入有误,请重新输入！\n')

    
        

    
##print(sf1)
##print('%d %d %d'%(sf1.a,sf1.b,sf1.z))
##print(sr1_list)
##print('输入成功！')
##
##
##sf=cry_info(1,2,3,90,90,90)
##print('OK')
##lf1=lf(1,2,3,90,90,90)
##print('cj(1,1,1,1,1,1):%d'%sf.cj(1,1,1,1,1,1))
##print('父类sq是：%d'%sf.sq(1,2,3))
##print('子类sq是：%d'%lf1.sq(1,2,3))
##print('dist is: %.2f'%lf1.dist(1,1,1))
##print('ang is: %.2f'%lf1.ang(1,0,0,0,1,0))
