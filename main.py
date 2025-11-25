def in_autotests_we_trust(a, b):
    if a == b:
        print('PASS1task')
    else:
        print('FAIL1task')
        print('FAIL2task')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
