'''
 name   kor  eng  mat    => Score
홍길동   90    80   70    => s1
정길동   50    60   70    => s2
이길동   100  100   100   => s3
'''

class Score:# 클래스에서 멤버는 self
    def __init__(self,name,kor,eng,mat,muse,pe) -> None :    #객체를 생성할 때 값을 받으면서 생성 하겠다.(초기값을 자동으로 생성하지 않고 받아서 초기화)
        self.name  = name
        self.kor  =  kor
        self.eng  = eng
        self.mat  = mat
        self.muse = muse
        self.pe = pe
    def getTot(self):
        return self.kor + self.eng+ self.mat
    
    def getAvg(self):
        #return #(self.kor + self.eng+ self.mat)/3
        return self.getTot()//3
    
    def getGrade(self): #임의로 함
        avg = self.getAvg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    

if __name__ == "__main__":
    s1  = Score("홍길동",   90, 80, 70)
    s2 = Score("정길동", 50, 60, 70)
    s3 = Score("이길동", 100, 100, 100)

    print(f'{s1.name} {s1.kor} {s1.eng} {s1.mat} {s1.getTot()} {s1.getAvg()} {s1.getGrade()}')
    print(f'{s2.name} {s2.kor} {s2.eng} {s2.mat} {s2.getTot()} {s2.getAvg()} {s2.getGrade()}')
    print(f'{s3.name} {s3.kor} {s3.eng} {s3.mat} {s3.getTot()} {s3.getAvg()} {s3.getGrade()}')

    #print(f'{s1.name:<5} {s1.kor:5d}  {s1.eng:5d} {s1.mat:5d}  {s1.getTot()}  {s1.getAvg():5.1f}   {s1.getGrade()}')

    #print(f'{s2.name:<5} {s2.kor:5d}  {s2.eng:5d} {s2.mat:5d}  {s2.getTot()}  {s2.getAvg():5.1f}   {s2.getGrade()}')

    #print(f'{s3.name:<5} {s3.kor:5d}  {s3.eng:5d} {s3.mat:5d}  {s3.getTot()}  {s3.getAvg():5.1f}   {s3.getGrade()}')

#