class C_Student:
    def __init__(self):
        self.m_name = '' #姓名
        self.m_id = 0 #学号
        self.m_class = '' #班级
        self.m_major = '' #专业
        self.m_school = '' #学院
        self.m_restoreCredits = 0 #重修学分
        self.m_earnedTotalCredits = 0 #获得总学分
        self.m_failedCredits = 0 #不及格学分
        self.m_totalCredits  = 0 #总学分
        self.m_averageWeightedCredits = 0 #学分加权平均分
        self.m_totalGPA = 0 #总绩点分
        self.m_gpa = 0 #平均学分绩点
        self.m_passedRate = 0 #通过率
        self.m_credits_required = 0 #必修课程学分
        self.m_credits_professionalElected = 0 #专业任选课程学分
        self.m_credits_limiteElected = 0 #限选课程学分
        self.m_credits_elected = 0 #任选课学分