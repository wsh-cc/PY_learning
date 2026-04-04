class Student:
    def __init__ (self,s_name,s_chinese,s_math,s_english):#self表示当前对象,s_name,s_chinese,s_math,s_english表示参数
        self.name=s_name
        self.chinese=s_chinese
        self.math=s_math
        self.english=s_english
    def __str__(self):
        return f"学生姓名：{self.name}\t语文：{self.chinese}分\t数学：{self.math}分\t英语：{self.english}分"
    # def __eq__(self, value):
    #     return self.name==value.name

class Grade_System:
    students=[]#类属性
    def __init__(self):
        pass#空方法，用于占位
    def add_student(self):
        name=input("请输入学生姓名：")
        for ss in self.students:
            if ss.name==name:
                print("该学生已存在")
                return
        chinese=int(input("请输入语文成绩："))
        math=int(input("请输入数学成绩："))
        english=int(input("请输入英语成绩："))
        if(chinese<0 or chinese>100 or math<0 or math>100 or english<0 or english>100):
            print("成绩输入错误")
            return
        st=Student(name,chinese,math,english)
        self.students.append(st)
    
    def modify_grades(self):
        name=input("请输入需要修改成绩的学生姓名：")
        for ss in self.students:
            if ss.name==name:
                chinese=int(input("请输入新的语文成绩："))
                math=int(input("请输入新的数学成绩："))
                english=int(input("请输入新的英语成绩："))
                if(chinese<0 or chinese>100 or math<0 or math>100 or english<0 or english>100):
                    print("成绩输入错误")
                    return
                ss.chinese=chinese
                ss.math=math
                ss.english=english
                print("成绩修改成功")
                return
        print("该学生不存在")
        return 
    def delete_student(self):
        name=input("请输入需要删除的学生姓名：")
        for ss in self.students:
            if ss.name==name:
               self.students.remove(ss)
               print("删除成功")
               return
        print("删除失败，该学生不存在")
        return 
    def query_student(self):
        name=input("请输入需要查询的学生姓名：")
        for ss in self.students:
            if ss.name==name:
                print(ss)
                return
        print("该学生不存在")
        return 
    def display_all(self):
        for ss in self.students:
            print(ss)

GS=Grade_System()
if __name__=="__main__":
  
        while(1):
         try:
            print('-'*20)
            match input("请输入您的选择：1.添加学生 2.修改成绩 3.删除学生 4.查询学生 5.显示所有学生 6.退出\n"):
                case '1':
                    GS.add_student()
            
                case '2':
                    GS.modify_grades()
            
                case '3':
                    GS.delete_student()
                        
                case '4':
                    GS.query_student()
            
                case '5':
                    GS.display_all()
            
                case '6':
                    print("谢谢使用")
                    break
                case _:
                    print("输入错误")
            print('-'*20)
         except Exception:
          print("输入错误，联系管理员")
        
