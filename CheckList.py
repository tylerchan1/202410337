from course import course
from courseList import courseList
import time



# 목표 학점 설정
goalMajorCredit = 62          # 전공필수 + 전공선택
goalEducationKnowledge = 8     # 교직소양
goalEducationPractice = 4      # 교직실습
goalIntensiveMajor = 15        # 전공심화

# 현재 수강 학점 초기화
myMajorCredit = 0              # 전공필수 + 전공선택 학점
myEducationKnowledge = 0       # 교직소양 학점
myEducationPractice = 0        # 교직실습 학점
myIntensiveMajor = 0           # 전공심화 학점

goalSubCredit = 50 #제2전공
goalGeneralCredit = 33 #교양

completedList = [] #전역변수 설정

requiredList = [
    course(course.ESSENTIAL_MAJOR, 3, "교육학개론"),
    course(course.ESSENTIAL_MAJOR, 3, "교육철학과 교육사"),
    course(course.ESSENTIAL_MAJOR, 3, "교육심리학"),
    course(course.ESSENTIAL_MAJOR, 3, "교육사회학"),
    course(course.ESSENTIAL_MAJOR, 3, "교육공학"),
    course(course.ESSENTIAL_MAJOR, 3, "교육과정"),
    course(course.ESSENTIAL_MAJOR, 3, "교육평가"),
    course(course.ESSENTIAL_MAJOR, 3, "교육행정"),
    course(course.EDUCATION_KNOWLEDGE, 2, "학교폭력예방 및 학생의 이해"),
    course(course.EDUCATION_KNOWLEDGE, 2, "특수교육학개론"),
    course(course.EDUCATION_KNOWLEDGE, 2, "교직실무"),
    course(course.EDUCATION_KNOWLEDGE, 1, "디지털교육"),
    course(course.EDUCATION_KNOWLEDGE, 1, "미래교사와 의사소통"),
    course(course.EDUCATION_PRACTICE, 1, "교육봉사활동1"),
    course(course.EDUCATION_PRACTICE, 1, "교육봉사활동2"),
    course(course.EDUCATION_PRACTICE, 2, "학교현장실습"),
    course(course.ESSENTIAL_MAJOR, 3, "교육학교과교육론"),
    course(course.ESSENTIAL_MAJOR, 3, "교육학교과교재연구 및 지도법")
]

def intro(): #인트로
    print("[교육학과 과목이수 체크리스트]")
    print()
    print()
    print()
    print("*프로그램은 상명대학교 학사 안내서를 참고하였습니다.")
    print("*모든 내용은 2024년도 입학자를 기준으로 합니다.")
    print("*모든 이수 학점 및 과목은 교원자격증 취득을 기준으로 합니다.")
    print("//최종 업데이트 2024.10.31")
    print()
    print()

def majorChoose(): #전공과정 선택
    running = True
    while running:

        any = ""
        print()
        print("[전공과정 선택]")
        print("1 복수전공")
        print("2 부전공")
        print("3 심화전공")
        courseChoice = input("중에서 어떤 전공과정에 있습니까?/또는 할 예정입니까?(1,2,3 숫자로 입력) : ")
        if courseChoice == "1":
            running = False
            running1 = True
            while running1:
                print()
                print("[복수전공 학과 선택]")
                print("1 사범계열")
                print("2 컴퓨터과학과")
                print("3 그외")
                print()
                print()
                majorChoice = input("복수전공 : ")
                if majorChoice == "1":
                    running1 = False
                    print()
                    print("사범계열 복수전공입니다.")
                    print("교육학과 전공 62학점, 사범계열 제 2전공 50학점, 교직소양 8학점, 교육실습 4학점을 이수해야합니다.")
                    print()
                    print()
                    any = input("이제부터 수강한 과목을 선택합니다. \n[계속하려면 엔터를 누르십시오]")
                    return("사범 복전")
                
                elif majorChoice == "2":
                    running1 = False
                    print()
                    print("컴퓨터과학과 복수전공입니다.")
                    print("교육학과 전공 50학점, 컴퓨터과학과 전공 45학점, 교직소양 8학점, 교육실습 4학점을 이수해야합니다.")
                    print()
                    print()
                    any = input("이제부터 수강한 과목을 선택합니다. \n[계속하려면 엔터를 누르십시오]")
                    return("컴공 복전")
                
                elif majorChoice == "3":
                    running1 = False
                    print()
                    print("그외 학과 복수전공입니다.")
                    print("교육학과 전공 50학점, 제 2전공 36학점, 교직소양 8학점, 교육실습 4학점을 이수해야합니다.") #
                    print()
                    print()
                    any = input("이제부터 수강한 과목을 선택합니다. \n[계속하려면 엔터를 누르십시오]")
                    return("일반 복전")
                
                else:
                    running1 = True
                    print()
                    print("1,2,3중에서 입력하십시오.")
        elif courseChoice == "2":
            running = False
            print()
            print("전공 제도는 부전공입니다.")
            print("교육학과 전공 60학점, 부전공 21학점, 교직소양 8학점, 교육실습 4학점을 이수해야합니다.")
            print()
            print()
            any = input("이제부터 수강한 과목을 선택합니다. \n[계속하려면 엔터를 누르십시오]")
            return("부전공")

        elif courseChoice == "3":
            running = False
            print()
            print("전공 제도는 심화전공입니다.")
            print("교육학과 선택과목(필수포함) 60학점, 교육학과 심화과목 15학점, 교직소양 8학점, 교육실습 4학점을 이수해야합니다.")
            print()
            print()
            any = input("이제부터 수강한 과목을 선택합니다. \n[계속하려면 엔터를 누르십시오]")
            return("심화전공")

        else:
            running = True
            print()
            print("1,2,3 중에서 입력하십시오.")
            

def trackChoice(): #전공과정에 따른 필수이수학점 
    global goalMajorCredit, goalSubCredit, goalIntensiveMajor
    if mycourse == "사범 복전":
        goalMajorCredit = 62
        goalSubCredit = 50
        goalIntensiveMajor = 0  

    elif mycourse == "컴공 복전":
        goalMajorCredit = 62
        goalSubCredit = 45
        goalIntensiveMajor = 0

    elif mycourse == "일반 복전":
        goalMajorCredit = 62
        goalSubCredit = 36
        goalIntensiveMajor = 0

    elif mycourse == "부전공":
        goalMajorCredit = 62
        goalSubCredit = 21
        goalIntensiveMajor = 0

    elif mycourse == "심화전공":
        goalMajorCredit = 60
        goalIntensiveMajor = 15
        goalSubCredit = 0

    else:
        pass

def display_courses(filterType=None): #과목 목록 출력하기
    """특정 타입의 과목을 출력하고, 유효한 인덱스를 반환"""
    print()
    print("[", filterType, "과목 목록 ]")
    print("번호", "전공유형", "\t학점", "과목명", sep="\t")
    time.sleep(0.3)
    print("-" * 50)
    
    valid_indices = []  # 유효한 인덱스를 저장할 리스트
    for idx, disCourse in enumerate(courseList, 1):
        if filterType is None or disCourse.courseType == filterType: #필터타입(디스플레이 메서드 매개인자)가 없거나(메서드오버로딩) 코스리스트에 저장된 객체 중에 필터타입과 같은 타입의 객체만 출력
            print(idx, disCourse.courseType, disCourse.credits, disCourse.name, sep="\t") # "1    전공필수    3   교육학개론"과 같이 출력
            valid_indices.append(idx)  # 유효한 인덱스를 리스트에 추가
            time.sleep(0.3)
    return valid_indices #함수값 = valid_indices

def select_courses(valid_indices):  # 과목 선택하기
    # 매개인자 = valid_indices, 출력된 값 중에서만 선택 가능하게

    while True:
        choiceList = input("\n수강한 과목 번호를 쉼표로 구분해 입력하세요 (예: 1,3,5) 또는 0 입력 시 종료: ").split(',')
        
        if choiceList == ["0"]:  # 0만 입력한 경우 함수 종료
            print("선택한 과목이 없어 함수를 종료합니다.")
            return

        HAE = True  # 모든 입력값이 유효한지 확인하는 플래그

        for index in choiceList:
            try:
                idx = int(index.strip())  # 입력값을 정수형으로 변환

                if idx in valid_indices:  # 유효한 인덱스인지 확인
                    completedList.append(courseList[idx - 1])  # completedList에 과목 객체 저장
                    print(courseList[idx - 1].name, "과목이 수강 완료로 저장되었습니다.")
                    time.sleep(0.3)
                else:  # 유효하지 않은 번호일 경우
                    print("유효하지 않은 번호입니다. 다시 선택하세요.")
                    HAE = False
                    break  # 유효하지 않은 입력이 발견되면 반복을 종료하고 다시 입력받음

            except ValueError:
                print("숫자를 입력해야 합니다. 다시 선택하세요.")
                HAE = False
                break  # 유효하지 않은 입력이 발견되면 반복을 종료하고 다시 입력받음

        if HAE:
            break  # 모든 입력이 유효하면 while 루프 종료



def display_completed_courses(): #수강 완료된 과목을 출력
    
    print("\n[ 현재까지 수강한 과목 목록 ]")
    print("유형", "\t학점", "과목명",sep="\t")
    time.sleep(0.5)
    print("-" * 50)
    for comCourse in completedList:  # completedList > course
        print(comCourse.courseType, comCourse.credits, comCourse.name, sep="\t")
        time.sleep(0.3)

def sum_credits(): #completedList에서 각 유형별 학점을 나누어 저장
    
    global myMajorCredit, myEducationKnowledge, myEducationPractice, myIntensiveMajor

    for course_obj in completedList:
        if course_obj.courseType in [course.ESSENTIAL_MAJOR, course.SELECTIVE_MAJOR]:
            myMajorCredit += course_obj.credits
        elif course_obj.courseType == course.EDUCATION_KNOWLEDGE:
            myEducationKnowledge += course_obj.credits
        elif course_obj.courseType == course.EDUCATION_PRACTICE:
            myEducationPractice += course_obj.credits
        elif course_obj.courseType == course.INTENSIVE_MAJOR:
            myIntensiveMajor += course_obj.credits

    print("\n[ 학점 현황 ]")
    print("-" * 50)
    print("전공선택 학점:", myMajorCredit, "/", goalMajorCredit)
    print("교직소양 학점:", myEducationKnowledge, "/", goalEducationKnowledge)
    print("교직실습 학점:", myEducationPractice, "/", goalEducationPractice)
    print("전공심화 학점:", myIntensiveMajor, "/", goalIntensiveMajor)
    print()
# 필수 과목 목록 (객체로 저장)


def check_required_courses():
    # 수강하지 않은 필수 과목 찾기
    missingList = []
    for reqCourse in requiredList:
        if reqCourse not in completedList:
            missingList.append(reqCourse)
    print("\n[ 앞으로 필수로 수강해야할 과목 ]")
    print("유형", "\t학점", "과목명",sep="\t")
    time.sleep(0.5)
    print("-" * 50)
    if missingList:
        for missCourse in missingList:  # completedList > course
            print(missCourse.courseType, missCourse.credits, missCourse.name, sep="\t")
    else:
        print("모든 필수 과목을 수강하셨습니다.")

#______________________________________________________________________________________________________________
intro()
mycourse = majorChoose()
trackChoice()

select_courses(display_courses(course.ESSENTIAL_MAJOR)) #전공필수
select_courses(display_courses(course.EDUCATION_KNOWLEDGE)) #교직소양
select_courses(display_courses(course.SELECTIVE_MAJOR)) #전공선택
select_courses(display_courses(course.EDUCATION_PRACTICE)) #교직실습

display_completed_courses()
sum_credits()
check_required_courses()
time.sleep(100)





