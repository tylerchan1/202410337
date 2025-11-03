
from course import course



# 과목 정보 리스트 (과목명, 학점, 유형)
course_data = [
    
]
# courseList에 자동으로 추가
#courseList = [course(name, credits, courseType) for name, credits, courseType in course_data]
#courseList.append(course14)


from course import course

# 필수 과목
courseList = [
    # 전공필수
    course(course.ESSENTIAL_MAJOR, 3, "교육학개론"),
    course(course.ESSENTIAL_MAJOR, 3, "교육철학과 교육사"),
    course(course.ESSENTIAL_MAJOR, 3, "교육심리학"),
    course(course.ESSENTIAL_MAJOR, 3, "교육사회학"),
    course(course.ESSENTIAL_MAJOR, 3, "교육공학"),
    course(course.ESSENTIAL_MAJOR, 3, "교육과정"),
    course(course.ESSENTIAL_MAJOR, 3, "교육평가"),
    course(course.ESSENTIAL_MAJOR, 3, "교육행정"),
    course(course.ESSENTIAL_MAJOR, 3, "교육학교과교육론"),
    course(course.ESSENTIAL_MAJOR, 3, "교육학교과교재연구 및 지도법"),
    
    # 교직소양 필수
    course(course.EDUCATION_KNOWLEDGE, 2, "학교폭력예방 및 학생의 이해"),
    course(course.EDUCATION_KNOWLEDGE, 2, "특수교육학개론"),
    course(course.EDUCATION_KNOWLEDGE, 2, "교직실무"),
    course(course.EDUCATION_KNOWLEDGE, 1, "디지털교육"),
    course(course.EDUCATION_KNOWLEDGE, 1, "미래교사와 의사소통"),
    
    # 교직실습 필수
    course(course.EDUCATION_PRACTICE, 1, "교육봉사활동1"),
    course(course.EDUCATION_PRACTICE, 1, "교육봉활동2"),
    course(course.EDUCATION_PRACTICE, 2, "학교현장실습"),

# 선택 과목

    # 전공선택    
    course(course.SELECTIVE_MAJOR, 3, "인간발달과 교육"),
    course(course.SELECTIVE_MAJOR, 3, "교육과 법"),
    course(course.SELECTIVE_MAJOR, 3, "인간관계와 교육"),
    course(course.SELECTIVE_MAJOR, 3, "청소년문화"),
    course(course.SELECTIVE_MAJOR, 3, "평생교육론"),
    course(course.SELECTIVE_MAJOR, 3, "인적자원개발론"),
    course(course.SELECTIVE_MAJOR, 3, "교육복지론"),
    course(course.SELECTIVE_MAJOR, 3, "평생교육방법론"),
    course(course.SELECTIVE_MAJOR, 3, "교육학연구방법"),
    course(course.SELECTIVE_MAJOR, 3, "청소년프로그램개발과 평가"),
    course(course.SELECTIVE_MAJOR, 3, "평생교육경영론"),
    course(course.SELECTIVE_MAJOR, 3, "교육학교과교육과정"),
    course(course.SELECTIVE_MAJOR, 3, "청소년문제와 보호"),
    course(course.SELECTIVE_MAJOR, 3, "청소년심리 및 상담"),
    course(course.SELECTIVE_MAJOR, 3, "평생교육실습"),
    course(course.SELECTIVE_MAJOR, 3, "교육학교과평가방법론"),
    course(course.SELECTIVE_MAJOR, 3, "미래교육론"),
    course(course.SELECTIVE_MAJOR, 3, "성인학습 및 상담"),
    course(course.SELECTIVE_MAJOR, 3, "교과교실수업연구"),
    
    # 교직소양 선택
    course(course.EDUCATION_KNOWLEDGE, 1, "미래교사와 인성"),
    course(course.EDUCATION_KNOWLEDGE, 1, "미래교사와 학교현장"),
    course(course.EDUCATION_KNOWLEDGE, 2, "생활지도 및 상담"),
    course(course.EDUCATION_KNOWLEDGE, 2, "교직과 미래교사"),
    
    # 전공심화
    course(course.INTENSIVE_MAJOR, 3, "교육과정개발과 컨설팅"),
    course(course.INTENSIVE_MAJOR, 3, "디지털학습콘텐츠설계 및 개발"),
    course(course.INTENSIVE_MAJOR, 3, "이러닝콘텐츠기획 및 설계"),
    course(course.INTENSIVE_MAJOR, 3, "교육정책"),
    course(course.INTENSIVE_MAJOR, 3, "평생교육프로그램개발론"),
    course(course.INTENSIVE_MAJOR, 3, "기업교육론"),
    course(course.INTENSIVE_MAJOR, 3, "상담심리학"),
    course(course.INTENSIVE_MAJOR, 3, "교수설계이론과 실제"),
    course(course.INTENSIVE_MAJOR, 3, "교육프로그램평가"),
    course(course.INTENSIVE_MAJOR, 3, "AI기반학습분석학"),
    course(course.INTENSIVE_MAJOR, 3, "집단상담"),
    

# 기초교양 과목들
    course(course.BASIC_GENERAL, 0, "사고와 표현"),
    course(course.BASIC_GENERAL, 0, "잉파/기초수학"),
    course(course.BASIC_GENERAL, 0, "컴퓨터사고와 데이터의 이해"),
    course(course.BASIC_GENERAL, 0, "알고리즘과 게임콘텐츠"),

    # 핵심교양 A
    course(course.CORE_GENERAL_A, 3, "이미지시대의 테크놀로지와 예술"),
    course(course.CORE_GENERAL_A, 3, "빅히스토리와 인공지능"),
    course(course.CORE_GENERAL_A, 3, "과학적사고와 탐구"),
    course(course.CORE_GENERAL_A, 3, "예술, 비즈니스, 문화와 함께하는 지식재산권법 입문"),

    # 핵심교양 B
    course(course.CORE_GENERAL_B, 2, "상상속의 아이디어"),
    course(course.CORE_GENERAL_B, 3, "창의적 디자인 상상"),
    course(course.CORE_GENERAL_B, 2, "창의적 문제 해결"),
    course(course.CORE_GENERAL_B, 2, "컴퓨테이셔널 씽킹"),

    # 핵심교양 C
    course(course.CORE_GENERAL_C, 3, "K-Culture를 통해 보는 예술의 산업가치"),
    course(course.CORE_GENERAL_C, 3, "색채심리학"),
    course(course.CORE_GENERAL_C, 3, "영화 속의 건축여행"),
    course(course.CORE_GENERAL_C, 2, "융합 창의 수학"),

    # 핵심교양 D
    course(course.CORE_GENERAL_D, 2, "다른 곳의 세계와 나"),
    course(course.CORE_GENERAL_D, 3, "문화 감수성의 이해와 실천"),
    course(course.CORE_GENERAL_D, 3, "문화 다양성과 미디어"),
    course(course.CORE_GENERAL_D, 2, "치유와 공간"),

    # 핵심교양 E
    course(course.CORE_GENERAL_E, 2, "호모 엠파티쿠스 (고통받는 인간)"),
    course(course.CORE_GENERAL_E, 3, "과학 기술자의 직업 윤리"),
    course(course.CORE_GENERAL_E, 2, "인간과 시간"),
    course(course.CORE_GENERAL_E, 2, "상명 정신과 윤리적 삶"),

    # 균형교양 - 사회
    course(course.BALANCE_GENERAL_SOCIAL, 3, "인구와 사회"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "경제학의 이해"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "글로벌 경제의 이해"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "법과 민주주의"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "현대 사회와 심리학"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "현대 사회와 인간"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "현대 정치의 이해"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "의식주와 소비 문화"),
    course(course.BALANCE_GENERAL_SOCIAL, 2, "리터러시 탐구와 응용"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "창의적 사고의 프레임워크"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "세계 종교와 문화"),
    course(course.BALANCE_GENERAL_SOCIAL, 3, "인터넷 윤리"),
    course(course.BALANCE_GENERAL_SOCIAL, 2, "현대 사회와 윤리"),
    course(course.BALANCE_GENERAL_SOCIAL, 2, "문화 다양성과 글로벌 시민"),

    # 균형교양 - 자연
    course(course.BALANCE_GENERAL_NATURAL, 3, "생명 과학의 이해"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "자연 과학의 세계"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "과학의 철학적 이해"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "대학 수학"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "물리 현상의 이해"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "미래 생활과 화학"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "정량적 사고"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "우주의 역사"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "창의적 프로그래밍 입문"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "미래 사회와 디지털 기술"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "기초 AI와 콘텐츠"),
    course(course.BALANCE_GENERAL_NATURAL, 3, "플랫폼 비즈니스와 사회적 가치"),

    # 균형교양 - 예술
    course(course.BALANCE_GENERAL_ART, 3, "미와 예술의 이해"),
    course(course.BALANCE_GENERAL_ART, 3, "현대 음악과 문화"),
    course(course.BALANCE_GENERAL_ART, 3, "오페라의 이해와 감상"),
    course(course.BALANCE_GENERAL_ART, 3, "교향곡의 이해"),
    course(course.BALANCE_GENERAL_ART, 3, "현대 생활과 디자인"),
    course(course.BALANCE_GENERAL_ART, 3, "현대 미술의 이해"),
    course(course.BALANCE_GENERAL_ART, 3, "현대 미술사와 이론"),
    course(course.BALANCE_GENERAL_ART, 3, "기업 메세나와 예술을 통한 사회공헌"),

    # 균형교양 - 브리지
    course(course.BALANCE_GENERAL_BRIDGE, 3, "인간과 환경의 이해"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "기초 세계사"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "철학으로 읽는 사회와 문화"),
    course(course.BALANCE_GENERAL_BRIDGE, 2, "기초 과학과 산업 제품"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "인공지능의 현재와 미래"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "신소재와 문명 발달"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "현대 사회와 의사결정"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "일본 대중음악으로 배우는 일본사회일본어"),
    course(course.BALANCE_GENERAL_BRIDGE, 3, "예술 경영의 이해"),
]








#print(courseList)
