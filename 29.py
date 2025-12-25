#-----------------------------------------------
#深いネストを避ける

class SimpleGradebook:
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = []
    def report_grade(self, name, score):
        self._grades[name].append(score)
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student("Shin Sasaki")
book.report_grade("Shin Sasaki", 90)
book.report_grade("Shin Sasaki", 95)
book.report_grade("Shin Sasaki", 85)

print(book.average_grade("Shin Sasaki"))

#-----------------------------------------------
#もろいコードになるので注意するパターン

from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {} #外部辞書
    def add_student(self, name):
        self._grades[name] = defaultdict(list) #内部辞書
        
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count
    

book = BySubjectGradebook()
book.add_student("Atama Itai")
book.report_grade("Atama Itai", "Math", 75)
book.report_grade("Atama Itai", "Math", 65)
book.report_grade("Atama Itai", "Gym", 65)
book.report_grade("Atama Itai", "Gym", 95)

print(book.average_grade("Atama Itai"))

#-----------------------------------------------
#ここまでくると複雑すぎる

class WeightedGradebook:
    def __init__(self):
        self._grades = {} #外部辞書
        
    def add_student(self, name):
        self._grades[name] = defaultdict(list) #内部辞書
        
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight)) #👈変えた
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for scores in by_subject.values():
            subject_avg, total_weight = 0, 0
            for score, weight in scores: #内部ループ追加
                subject_avg += score * weight
                total_weight += weight
                
            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count
    
book = WeightedGradebook()
book.add_student("Shin Sasaki")
book.report_grade("Shin Sasaki", "Math", 75,0.05)
book.report_grade("Shin Sasaki", "Math", 65,0.15)
book.report_grade("Shin Sasaki", "Math", 70,0.80)
book.report_grade("Shin Sasaki", "Gym", 100,0.40)
book.report_grade("Shin Sasaki", "Gym", 85,0.60)

print(book.average_grade("Shin Sasaki"))

#-----------------------------------------------
#リファクタリング　まずはタプルで

grades = []
grades.append((95,0.45))
grades.append((85,0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades) #タプルの先頭要素を無視するための記法
average_grade = total / total_weight

#タプルの位置に依存している　要素が増えると_を増やさないといけない

grades = []
grades.append((95, 0.45, "Great Job"))
grades.append((85, 0.55, "Better Next Time"))
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight,  _ in grades)
average_grade = total / total_weight

#要素が増えて_も増えた👆

#-----------------------------------------------
#要素が多く、タプルが長くなる場合にクラスを検討する
#コードは長いが非常に読みやすい

from dataclasses import dataclass

@dataclass(frozen=True)
class Grade:
    score: int
    weight: float

class Subject:
    def __init__(self):
        self._grades = []
    
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
    
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight
    
class Student:
    def __init__(self):
        self._subject = defaultdict(Subject)
        
    def get_subject(self, name):
        return self._subject[name]
    
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count
    
class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
        
    def get_student(self, name):
        return self._students[name]

book = Gradebook()
Shin = book.get_student("Shin Sasaki")
math = Shin.get_subject("Math")
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)  #全部でweight100
gym = Shin.get_subject("Gym")
gym.report_grade(90, 0.10)
gym.report_grade(90, 0.10)
gym.report_grade(90, 0.10)
gym.report_grade(90, 0.10)
gym.report_grade(90, 0.10)
gym.report_grade(100, 0.10)
gym.report_grade(100, 0.10)
gym.report_grade(100, 0.10)
gym.report_grade(100, 0.10)
gym.report_grade(100, 0.10)

print(Shin.average_grade())
#辞書が複雑になりすぎたらクラスに分割して記述する！