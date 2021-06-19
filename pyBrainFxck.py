def Muda_language_execute(muda_code):
    code = Muda_language2BrainFxck_code(muda_code)
    return pyBrainFxck(code)

def Muda_language2BrainFxck_code(muda_code):
    """
    無駄言語の変換処理
    Muda_language to BrainFxck_code

    DocTest
    >>> Muda_language2BrainFxck_code("むだむだむだむだむだむだむだむだ、mudaむだむだむだむだ、mudaむだむだmudaむだむだむだmudaむだむだむだmudaむだMUDAMUDAMUDAMUDA無駄。mudaむだmudaむだmuda無駄mudamudaむだ、MUDA。MUDA無駄。mudamudaムダmuda無駄無駄無駄ムダむだむだむだむだむだむだむだムダムダむだむだむだムダmudamudaムダMUDA無駄ムダMUDAムダむだむだむだムダ無駄無駄無駄無駄無駄無駄ムダ無駄無駄無駄無駄無駄無駄無駄無駄ムダmudamudaむだムダmudaむだむだムダ")
    '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    """
    code_temp = muda_code.replace("muda",">")
    code_temp = code_temp.replace("MUDA","<")
    code_temp = code_temp.replace("ムダ",".")
    code_temp = code_temp.replace("むだ","+")
    code_temp = code_temp.replace("無駄","-")
    code_temp = code_temp.replace("ﾑﾀﾞ",",")
    code_temp = code_temp.replace("、","[")
    code      = code_temp.replace("。","]")

    return code

def BrainFxck_code2Muda_language(code):
    """
    無駄言語の変換処理
    BrainFxck_code to Muda_language
    """
    code_temp = code.replace(">","muda")
    code_temp = code_temp.replace("<","MUDA")
    code_temp = code_temp.replace(".","ムダ")
    code_temp = code_temp.replace("+","むだ")
    code_temp = code_temp.replace("-","無駄")
    code_temp = code_temp.replace(",","ﾑﾀﾞ")
    code_temp = code_temp.replace("[","、")
    muda_code = code_temp.replace("]","。")

    return muda_code

def pyBrainFxck(code):
    """
    Python上でBrainFxckを実行するコンパイラ
    入れられたcodeを処理し、その結果出力される文章を返却する。

    BrainFxck仕様
    ">" メモリポインタをインクリメント
    "<" メモリポインタをデクリメント
    "." メモリポインタが指し示す先に格納された変数を処理系に表示
    "+" メモリポインタが指し示す先に格納された変数をインクリメント
    "-" メモリポインタが指し示す先に格納された変数をデクリメント
    "," 標準入力された値をメモリポインタが指し示す先に代入
    "[" メモリポインタが指す値が0なら、対応する"]"までskip
    "]" メモリポインタが指す値が非0なら、対応する"["までジャンプ
    →これらの分岐が終わったらプログラムカウンタをインクリメント

    DocTest
    >>> pyBrainFxck("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
    'Hello World!\\n'
    >>> pyBrainFxck("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.>++++++++++.")
    'ABC\\n'
    """
    #メモリポインタ・プログラムカウンタ・メモリ定義
    pointer = 0
    program_counter = 0
    memory = [0 for i in range(10000)]

    #結果
    result = ""

    #実行部分
    while program_counter < len(code):
        if code[program_counter] == '>':
            pointer += 1
        elif code[program_counter] == '<':
            pointer -= 1
        elif code[program_counter] == '.':
            result += chr(memory[pointer])
        elif code[program_counter] == '+':
            memory[pointer] += 1
        elif code[program_counter] == '-':
            memory[pointer] -= 1
        elif code[program_counter] == ',':
            memory[pointer] = int(input())
        elif code[program_counter] == '[':
            if memory[pointer] == 0:
                #nestカウント
                nest = 0
                while True:
                    program_counter += 1
                    if code[program_counter] == '[':
                        nest += 1
                    if code[program_counter] == ']' and nest == 0:
                        break
                    if code[program_counter] == ']':
                        nest -= 1
        elif code[program_counter] == ']':
            if memory[pointer] != 0:
                #nestカウント
                nest = 0
                while True:
                    program_counter -= 1
                    if code[program_counter] == ']':
                        nest += 1
                    if code[program_counter] == '[' and nest == 0:
                        break
                    if code[program_counter] == '[':
                        nest -= 1
        program_counter += 1

    return result

if __name__ == '__main__':
    muda_code = """
    むだむだむだむだむだむだむだむだ、mudaむだむだむだむだ、mudaむだむだmudaむだむだむだmudaむだむだむだmudaむだMUDAMUDAMUDAMUDA無駄。mudaむだmudaむだmuda無駄mudamudaむだ、MUDA。MUDA無駄。mudamuda
    ムダmuda無駄無駄無駄ムダむだむだむだむだむだむだむだムダムダむだむだむだムダmudamudaムダMUDA無駄ムダMUDAムダむだむだむだムダ無駄無駄無駄無駄無駄無駄ムダ無駄無駄無駄無駄無駄無駄無駄無駄ムダmudamudaむだムダmudaむだむだムダ
    """
    print(BrainFxck_code2Muda_language("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.>++++++++++."))
    print(Muda_language_execute(muda_code))
    import doctest
    doctest.testmod()