from IsraelIDValidator import IDValidator


if __name__ == '__main__':
    validator = IDValidator()


    def input_validation(user_input, digit):
        if len(user_input) > digit or not user_input:
            return False

    while True:
        print('Insert: 1) For ID validation 2) For Control Digit 3) For stop ')
        user_selection = input()

        match user_selection:
            case '3':
                break
            case '1':
                print('Insert Israeli ID for validation')        
                ID = input()
                if input_validation(ID, 9) is False:
                    print('Your input is wrong , please try again')
                    continue

                ans = validator.id_validation(ID)
                if (ans):
                    print(f'{ID} is a valid Israeli ID number\n')
                else:
                    print(f'{ID} is not a valid Israeli ID number \n')
            case '2':
                print('Insert partial Israeli ID number (without control digit)')        
                missing_ID = input()

                if input_validation(missing_ID, 8) is False:
                    print('Your input is wrong , please try again')
                    continue

                ans = validator.find_control_digit(missing_ID)
                print(f'The control digit of {missing_ID} is {ans} \n')