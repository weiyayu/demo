def add_student(student_info):
    """添加学生成绩（处理重复学号）"""
    for s in students:
        if s["学号"] == student_info["学号"]:
            return False  # 学号重复，添加失败
    students.append(student_info)
    return True

def query_student(key, value):
    """按条件查询学生成绩"""
    results = []
    for s in students:
        if s[key] == value:
            results.append(s)
    return results

def calculate_course_stats(course_name):
    """统计课程成绩"""
    scores = [s["成绩"] for s in students if s["课程名称"] == course_name]
    if not scores:
        return None
    return {
        "平均分": sum(scores)/len(scores),
        "最高分": max(scores),
        "最低分": min(scores)
    }


def menu():
    """显示菜单"""
    print("\n学生成绩管理系统")
    print("1. 录入成绩")
    print("2. 按姓名查询")
    print("3. 按学号查询")
    print("4. 按课程查询")
    print("5. 统计课程成绩")
    print("6. 退出系统")
    return input("请选择操作：")

def validate_score(score):
    """验证成绩有效性"""
    try:
        score = int(score)
        if 0 <= score <= 100:
            return score
        raise ValueError
    except:
        print("错误：成绩必须为0-100的整数！")
        return None

def main():
    while True:
        choice = menu()
        if choice == "1":
            # 录入成绩
            name = input("姓名：")
            sid = input("学号：")
            course = input("课程名称：")
            score = validate_score(input("成绩："))
            if score is not None:
                if add_student({
                    "姓名": name,
                    "学号": sid,
                    "课程名称": course,
                    "成绩": score
                }):
                    print("录入成功！")
                else:
                    print("错误：学号已存在！")
        elif choice in ["2", "3", "4"]:
            # 查询成绩
            key = ["姓名", "学号", "课程名称"][int(choice)-2]
            value = input(f"请输入{key}：")
            results = query_student(key, value)
            if results:
                print(f"\n查询结果（{key}={value}）：")
                for idx, s in enumerate(results, 1):
                    print(f"{idx}. {s['姓名']}（学号：{s['学号']}）：{s['课程名称']}={s['成绩']}分")
            else:
                print("未找到匹配记录！")
        elif choice == "5":
            # 统计课程成绩
            course = input("请输入课程名称：")
            stats = calculate_course_stats(course)
            if stats:
                print(f"\n{course}成绩统计：")
                print(f"平均分：{stats['平均分']:.2f}，最高分：{stats['最高分']}，最低分：{stats['最低分']}")
            else:
                print("该课程暂无成绩记录！")
        elif choice == "6":
            print("系统已退出，感谢使用！")
            break
        else:
            print("错误：请输入有效选项（1-6）！")
