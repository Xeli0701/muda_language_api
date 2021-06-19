def pyBrainFxck(code):
    #メモリポインタ
    pointer = 0

    #プログラムカウンタ
    program_counter = 0

    #メモリ
    memory = [0 for i in range(10000)]


    #変換処理
    """
    > muda
    < MUDA
    . ムダﾞ
    + むだ
    - 無駄
    , ﾑﾀﾞ
    [ 、
    ] 。
    """
    code_temp = code.replace("muda",">")
    code_temp = code_temp.replace("MUDA","<")
    code_temp = code_temp.replace("ムダ",".")
    code_temp = code_temp.replace("むだ","+")
    code_temp = code_temp.replace("無駄","-")
    code_temp = code_temp.replace("ﾑﾀﾞ",",")
    code_temp = code_temp.replace("、","[")
    tape      = code_temp.replace("。","]")
    print(tape)

    result = ""

    #コードの末尾までプログラムを処理する
    while program_counter < len(tape):

        #プログラム・カウンタが指し示す文字を読み ">"ならメモリポインタをインクリメントする
        if tape[program_counter] == '>':
            pointer += 1

        #"<" メモリポインタをデクリメントする
        elif tape[program_counter] == '<':
            pointer -= 1

        #"." メモリポインタが指し示す先に格納された変数を処理系に表示
        elif tape[program_counter] == '.':
            result += chr(memory[pointer])

        #"+" メモリポインタが指し示す先に格納された変数をインクリメント
        elif tape[program_counter] == '+':
            memory[pointer] += 1

        #"-" メモリポインタが指し示す先に格納された変数をデクリメント
        elif tape[program_counter] == '-':
            memory[pointer] -= 1

        #"," 標準入力された値をメモリポインタが指し示す先に代入
        elif tape[program_counter] == ',':
            memory[pointer] = int(input())

        #"[" メモリポインタが指す値が0なら、対応する"]"までskip
        elif tape[program_counter] == '[':
            if memory[pointer] == 0:
                #nest構造をカウントする変数
                nest = 0
                while True:
                    program_counter += 1
                    if tape[program_counter] == '[':
                        nest += 1
                    if tape[program_counter] == ']' and nest == 0:
                        break
                    if tape[program_counter] == ']':
                        nest -= 1
        #"]" メモリポインタが指す値が非0なら、対応する"["までジャンプ
        elif tape[program_counter] == ']':
            if memory[pointer] != 0:
                #nest構造をカウントする変数
                nest = 0
                while True:
                    program_counter -= 1
                    if tape[program_counter] == ']':
                        nest += 1
                    if tape[program_counter] == '[' and nest == 0:
                        break
                    if tape[program_counter] == '[':
                        nest -= 1
                        
        #プログラム・カウンタをインクリメントする
        program_counter += 1

    return result

if __name__ == '__main__':
    code = """
    むだむだむだむだむだむだむだむだ、mudaむだむだむだむだ、mudaむだむだmudaむだむだむだmudaむだむだむだmudaむだMUDAMUDAMUDAMUDA無駄。mudaむだmudaむだmuda無駄mudamudaむだ、MUDA。MUDA無駄。mudamuda
    ムダmuda無駄無駄無駄ムダむだむだむだむだむだむだむだムダムダむだむだむだムダmudamudaムダMUDA無駄ムダMUDAムダむだむだむだムダ無駄無駄無駄無駄無駄無駄ムダ無駄無駄無駄無駄無駄無駄無駄無駄ムダmudamudaむだムダmudaむだむだムダ
    """
    print(pyBrainFxck(code))