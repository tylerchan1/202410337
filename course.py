class course:
    INTENSIVE_MAJOR = "전공심화"
    SELECTIVE_MAJOR = "전공선택"
    ESSENTIAL_MAJOR = "전공필수"
    EDUCATION_KNOWLEDGE = "교직소양"
    EDUCATION_PRACTICE = "교직실습"

    BASIC_GENERAL = "기초교양"
    CORE_GENERAL_A = "핵심교양A"
    CORE_GENERAL_B = "핵심교양B"
    CORE_GENERAL_C = "핵심교양C"
    CORE_GENERAL_D = "핵심교양D"
    CORE_GENERAL_E = "핵심교양E"
    BALANCE_GENERAL_SOCIAL = "균형교양사회"
    BALANCE_GENERAL_NATURAL = "균형교양자연"
    BALANCE_GENERAL_ART = "균형교양예술"
    BALANCE_GENERAL_BRIDGE = "균형교양브리지"
    
    def __init__(self, courseType, credits, name):
        
        self.courseType = courseType
        self.credits = credits
        self.name = name

"""
    def getCredit(self):
        if self.courseType in [course.INTENSIVE_MAJOR, course.SELECTIVE_MAJOR, course.ESSENTIAL_MAJOR ]: 
            myMajorCredit += self.credits
        else:
            myGeneralCredit += self.credits

    def getName(self):
        return self.name
    
    def getType(self):
        return self.courseType
"""
    

    
        
