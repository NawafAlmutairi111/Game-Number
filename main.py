function header(){
    print the welcome message is green and bold
    print the rules of the game in cyan
}

function options(){
    print all the options available in the game with formating
}

function clear(){
    if (os.name == 'nt'){
        system('cls') to clear the screen of console in windows
    }
    else if (os.name == 'posix'){
        system("clear") #to clear the screen in bash and macOS
    }
}

function generate_random_question(symbols, instance_type, num_array, level = 1){
    op_dict = array/(on DS) to collectively store operator based on the instance_type

    function recursive_generation(symbols, symbols_used, op_dict, num_array, instance_type, count_left=1){
        if (instance_type is not in range 1-7){
            oppr = random(op_dict)
        }
        else{
            oppr = op_dict[instance_type]
        }

        sym_x = random(symbols)
        if sym_x is not in used_symbols{
            symbols_used[sym_x] = random(num_array)
        }

        if count_left == 1{
            sym_y = random(symbols)
            if sym_y not in symbols_used:
                symbols_used[sym_y] = random(num_array)

            return (sym_x) oppr (sym_y)
        }

        return (sym_x) oppr (recursive_generation(
            symbols, symbols_used, op_dict, num_array, instance_type, count_left-1))
    }

    values = dictionay of symbol: value pair
    question = recursive_generation(symbols, values_dict, op_dict, num_array, instance_type, level)

    while question is equal to 0{
        question = recursive_generation(symbols, values_dict, op_dict, num_array, instance_type, level)
    }
    return question, values
}

function start_new_game_instance(num_array, instance_type){
    print message of starting the game
    sleep(1)
    print('Initialized the instance')
    print('Type \033[96m.quit\033[00m at the place of answer to quit the game.\nGive float answers by rounding of to
     \033[96m'2 decimal places'\033[00m')

    current_instance_score = 0
    current_instance_symbols = sympy.symbols('a:d, x:z')

    quit = True

    while quit{
        if current_instance_score < 80
            level = 1
        elif current_instance_score < 200
            level = 5
        elif current_instance_score < 400
            level = 6
        elif current_instance_score < 800
            level = 8
        elif current_instance_score < 1200
            level = 10
        else:
            level = 15

        question_, values_ = generate_random_question(current_instance_symbols,
        instance_type, num_array, level)

        print(question_) // with formating

        try{
            answer = input(">>> ") // answer from the user
            if (answer == '.quit'){
                break
            }
            else{
                answer = eval(answer)# evaluating the user input

                correct_ans = question_.evalf(subs=values_, strict = True)
                correct_ans = round(correct_ans)

                if answer is of type float:
                    answer = round(answer, 2)

                if answer == correct_ans{
                    current_instance_score += 4
                    print("Correct answer")// in green
                }
                else{
                    current_instance_score -= 2
                    print("Wrong answer")// in light red
                }
            }
        except{
            print("Invalid choice of options.")
            continue
        }
        return instance_type, current_instance_score
    }
}


def show_score_card(instance_list):
    // shows the score card of the allowed instances

    instance_dict = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Float Division",
        5: "Floor division",
        6: "Modulos",
        7: "Exponential",
        8:"Randomly Generated"
    }
    clear()

    if instance_list is empty:
        print("Haven't played once!".center(40))// centered to 40

    else:
        col_header =f"|{'Game choice'.center(35) | 'Score'|"
        print(col_header)

        body = "\n".join("|"+all element of instance with there score + "|"))
        print(body)
        print("+------------------------------------+")

    input("Press any key to continue -")
    clear()