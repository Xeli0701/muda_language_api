def execute(original_code):
    """
    無駄言語・オラ言語の実行

    DocTest
    >>> execute("むだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだおらおらおらおらおらおらおらおらおらおらおらおらおらおらオラおらオラおらオラoraおらおらおらおらおらおらおらおらおらおらオラ")
    'ABC\\n'
    """
    code = Muda2Bf(original_code)
    code = Ora2Bf(code)
    return BfCompiler(code)

def Muda2Bf(muda_code):
    """
    無駄言語の変換処理
    Muda_language to BrainFxck_code

    DocTest
    >>> Muda2Bf("むだむだむだむだむだむだむだむだ、mudaむだむだむだむだ、mudaむだむだmudaむだむだむだmudaむだむだむだmudaむだMUDAMUDAMUDAMUDA無駄。mudaむだmudaむだmuda無駄mudamudaむだ、MUDA。MUDA無駄。mudamudaムダmuda無駄無駄無駄ムダむだむだむだむだむだむだむだムダムダむだむだむだムダmudamudaムダMUDA無駄ムダMUDAムダむだむだむだムダ無駄無駄無駄無駄無駄無駄ムダ無駄無駄無駄無駄無駄無駄無駄無駄ムダmudamudaむだムダmudaむだむだムダ")
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

def Ora2Bf(muda_code):
    """
    オラ言語の変換処理
    Ora_language to BrainFxck_code
    """
    code_temp = muda_code.replace("ora",">")
    code_temp = code_temp.replace("ORA","<")
    code_temp = code_temp.replace("オラ",".")
    code_temp = code_temp.replace("おら","+")
    code_temp = code_temp.replace("折羅","-")
    code_temp = code_temp.replace("ｵﾗ",",")
    code_temp = code_temp.replace("、","[")
    code      = code_temp.replace("。","]")

    return code

def Bf2Muda(code):
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

def Bf2Ora(code):
    """
    無駄言語の変換処理
    BrainFxck_code to Muda_language
    """
    code_temp = code.replace(">","ora")
    code_temp = code_temp.replace("<","ORA")
    code_temp = code_temp.replace(".","オラ")
    code_temp = code_temp.replace("+","おら")
    code_temp = code_temp.replace("-","折羅")
    code_temp = code_temp.replace(",","ｵﾗ")
    code_temp = code_temp.replace("[","、")
    muda_code = code_temp.replace("]","。")

    return muda_code

def BfCompiler(code):
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
    >>> BfCompiler("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
    'Hello World!\\n'
    >>> BfCompiler("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.>++++++++++.")
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
    ora_code = """
    おらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおらおら
おらおらおらおらおらおらおらおらおらおらおらおらおらおらオラおらオラおらオラoraおらおらおらおらおらおらおらおらおらおらオラ
    """

    muda_ora_code = """
    むだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだおらおらおらおらおらおらおらおらおらおらおらおらおらおらオラおらオラおらオラoraおらおらおらおらおらおらおらおらおらおらオラ
    """

    print(Bf2Muda("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.>++++++++++."))
    print(Bf2Ora("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.>++++++++++."))
    print(execute(muda_code))
    print(execute(ora_code))
    print(execute(muda_ora_code))
    import doctest
    doctest.testmod()