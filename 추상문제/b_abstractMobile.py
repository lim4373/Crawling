
if __name__ == '__main__':
    lt = LTab("LTab", 50, "AP-01")
    ot = OTab("OTab", 100, "AND-20")


    # 출력 함수
    def print_status(title, devices):
        print(title)
        print("Mobile\t\tBattery\t\tOS")
        print("---------------------------------------------")
        for device in devices:
            print(device)
        print()


    # 상태 출력
    devices = [lt, ot]
    print_status("초기 상태", devices)

    # 10분 충전 후 상태 출력
    for device in devices:
        device.charge(10)
    print_status("10분 충전", devices)

    # 5분 사용 후 상태 출력
    for device in devices:
        device.operate(5)
    print_status("5분 통화", devices)
