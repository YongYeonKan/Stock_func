
import datetime

class stock():
    '''
    기본적으로 주가 정보 데이터 전처리 등에 사용하는
    '''
    def __init__(self):
        print('stock tool is initialized')



        self.list_호가_기준 = [1, 2000, 5000, 20000, 50000, 200000, 500000]
        self.list_호가_갭 = [1, 5, 10, 50, 100, 500, 1000]

    def run(self):
        print('왜 이게 되지?')
        print('나는 뭐 한게 없는데 ?')
        self.create()
        self.say_ho(10)
    def _check_time(self):
        '''
        check time func

        :return: 현재 시간
        '''
        return datetime.datetime.now()

    def fun_find_상하한가(self, close:int):
        '''
        전일 종가를 기준 금일 상한가 하한가를 찾음
        :param close:
        :return: int(상한가) int(하한가)
        '''
        상한가 = close * 1.3
        하한가 = close * 0.7
        # list_호가 = []
        # list_호가_기준 = [1, 2000, 5000, 20000, 50000, 200000, 500000]
        # list_호가_갭 = [1, 5, 10, 50, 100, 500, 1000]

        for i, 기준 in enumerate(self.list_호가_기준):
            if 상한가 < 기준:
                break
        전기준 = 기준
        호가갭 = self.list_호가_갭[i - 1]
        상한가 = 상한가 - 상한가 % 호가갭

        for i, 기준 in enumerate(self.list_호가_기준):
            if 하한가 < 기준:
                break
        전기준 = 기준
        호가갭 = self.list_호가_갭[i - 1]
        하한가 = 하한가 - 하한가 % 호가갭 + 호가갭

        return int(상한가), int(하한가)

    def fun_dict_호가(self, 기준가):
        '''
        기준가를 기준으로 틱당 호가를 계산하여 dict 호가 생성
        :param 기준가:
        :return:
        '''
        상한가, 하한가 = self.fun_find_상하한가(기준가)

        틱가격 = 기준가

        # list_호가_기준 = [1, 2000, 5000, 20000, 50000, 200000, 500000]
        # list_호가_갭 = [1, 5, 10, 50, 100, 500, 1000]
        count = 0
        dict_호가 = {}
        dict_호가[기준가] = 0
        while 틱가격 < 상한가:
            for i, 기준 in enumerate(self.list_호가_기준):
                if 틱가격 < 기준:
                    break
            호가갭 = self.list_호가_갭[i - 1]
            틱가격 += 호가갭
            count += 1
            dict_호가[틱가격] = count

        틱가격 = 기준가
        count = 0
        while 틱가격 > 하한가:
            for i, 기준 in enumerate(self.list_호가_기준):
                if 틱가격 < 기준:
                    break
            호가갭 = self.list_호가_갭[i - 1]
            틱가격 -= 호가갭
            count -= 1
            dict_호가[틱가격] = count
        return dict_호가
    def cal_VI(self, 기준가 : int,yes_close :int , dict_호가):
        print('cal VI')
        VI_UP = 기준가 * 1.10
        VI_DOWN = 기준가 * 0.90


        for i, 기준 in enumerate(self.list_호가_기준):
            if VI_UP < 기준:
                break
        전기준 = 기준
        호가갭 = self.list_호가_갭[i - 1]
        VI_UP = VI_UP - VI_UP % 호가갭

        for i, 기준 in enumerate(self.list_호가_기준):
            if VI_DOWN < 기준:
                break
        전기준 = 기준
        호가갭 = self.list_호가_갭[i - 1]
        VI_DOWN = VI_DOWN - VI_DOWN % 호가갭 + 호가갭

        return int(VI_UP), int(VI_DOWN)







if __name__ == "__main__":
    st = stock()

    st.run()

