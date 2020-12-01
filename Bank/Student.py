"""
学生管理
"""


# 存储学生信息 name age score id
class StudentModel:

    def __init__(self, name="", age=0, score=0, id=1):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


# 界面操作
class StudentView:
    def __init__(self):
        # 把逻辑处理类传进来，变成属性
        self.controller = StudentController

    def __display_menu(self):
        print("""
        1)添加学生信息
        2)显示学生信息
        3)删除学生信息
        4)修改学生信息
        5)学生成绩升序排序
        """)

    def __select__menu(self):
        cmd = input("请输入选项：")
        if cmd == 1:
            # 调用insert方法
            self.controller.insert_student()
        elif cmd == 2:
            # 调用show方法
            self.controller.show_student()
        elif cmd == 3:
            # 调用delete方法
            self.controller.delete_student()
        elif cmd == 4:
            # 调用change方法
            self.controller.change_student()
        elif cmd == 5:
            # 调用sort方法
            self.controller.sort_student()
        else:
            print("请输入正确选项")

    # 启动程序入口方法
    def main(self):
        while True:
            self.__display_menu()
            # 选择功能
            self.__select__menu()


# 逻辑处理
class StudentController:
    def insert_student(self):
        pass

    def show_student(self):
        pass

    def delete_student(self):
        pass

    def change_student(self):
        pass

    def sort_student(self):
        pass


stu = StudentView()
# 启动程序
stu.main()