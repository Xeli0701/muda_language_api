def execute(code):
    """
    無駄言語の実行

    DocTest
    >>> execute("むだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだむだおらおらおらおらおらおらおらおらおらおらおらおらおらおらオラおらオラおらオラoraおらおらおらおらおらおらおらおらおらおらオラ")
    'ABC\\n'
    """
    code = Muda2Bf(code)
    return BfCompiler(code)

muda_command = [["muda","ora"],
    ["MUDA","ORA"],
    ["ムダ","オラ"],
    ["むだ","おら"],
    ["無駄","折羅"],
    ["ﾑﾀﾞ","ｵﾗ"],
    ["、"],
    ["。"]
    ]

bf_command = [">","<",".","+","-",",","[","]"]

def Muda2Bf(code_input):
    """
        無駄言語をBrainFxckに変換

        Parameters
        ----------
        code_input : String
            無駄言語
        
        Returns
        -------
        String
            Brainfxck言語

        DocTest
        >>> Muda2Bf("むだむだむだむだむだむだむだむだ、mudaむだむだむだむだ、mudaむだむだmudaむだむだむだmudaむだむだむだmudaむだMUDAMUDAMUDAMUDA無駄。mudaむだmudaむだmuda無駄mudamudaむだ、MUDA。MUDA無駄。mudamudaムダmuda無駄無駄無駄ムダむだむだむだむだむだむだむだムダムダむだむだむだムダmudamudaムダMUDA無駄ムダMUDAムダむだむだむだムダ無駄無駄無駄無駄無駄無駄ムダ無駄無駄無駄無駄無駄無駄無駄無駄ムダmudamudaむだムダmudaむだむだムダ")
        '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    """
    converted = code_input 
    for m_l,b in zip(muda_command,bf_command):
        for m in m_l:
            converted = converted.replace(m,b)
    return converted

def Bf2Muda(code_input):
    """
        BrainFxckを無駄言語に変換

        Parameters
        ----------
        code_input : String
            無駄言語
        
        Returns
        -------
        String
            Brainfxck言語

        DocTest
        >>> Muda2Bf("むだむだむだむだむだむだむだむだ、mudaむだむだむだむだ、mudaむだむだmudaむだむだむだmudaむだむだむだmudaむだMUDAMUDAMUDAMUDA無駄。mudaむだmudaむだmuda無駄mudamudaむだ、MUDA。MUDA無駄。mudamudaムダmuda無駄無駄無駄ムダむだむだむだむだむだむだむだムダムダむだむだむだムダmudamudaムダMUDA無駄ムダMUDAムダむだむだむだムダ無駄無駄無駄無駄無駄無駄ムダ無駄無駄無駄無駄無駄無駄無駄無駄ムダmudamudaむだムダmudaむだむだムダ")
        '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    """
    converted = code_input 
    for m_l,b in zip(muda_command,bf_command):
        for m in m_l:
            converted = converted.replace(b,m)
    return converted

def BfCompiler(code):
    """
        Python上でBrainFxckを実行するコンパイラ。入れられたcodeを処理し、その結果出力される文章を返却する。

        BrainFxck仕様
        - ">" メモリポインタをインクリメント
        - "<" メモリポインタをデクリメント
        - "." メモリポインタが指し示す先に格納された変数を処理系に表示
        - "+" メモリポインタが指し示す先に格納された変数をインクリメント
        - "-" メモリポインタが指し示す先に格納された変数をデクリメント
        - "," 標準入力された値をメモリポインタが指し示す先に代入
        - "[" メモリポインタが指す値が0なら、対応する"]"までskip
        - "]" メモリポインタが指す値が非0なら、対応する"["までジャンプ
            - →これらの分岐が終わったらプログラムカウンタをインクリメント

        DocTest
        >>> BfCompiler("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
        'Hello World!\\n'
        >>> BfCompiler("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.>++++++++++.")
        'ABC\\n'
    """
    #メモリポインタ・プログラムカウンタ・メモリ定義
    p = 0 # Pointer
    p_c = 0 # Program_counter
    memory = [0 for i in range(10000)]

    #結果
    result = ""

    #実行部分
    while p_c < len(code):
        if code[p_c] == '>':
            p += 1
        elif code[p_c] == '<':
            p -= 1
        elif code[p_c] == '.':
            result += chr(memory[p])
        elif code[p_c] == '+':
            memory[p] += 1
        elif code[p_c] == '-':
            memory[p] -= 1
        elif code[p_c] == ',':
            memory[p] = int(input())
        elif code[p_c] == '[':
            if memory[p] == 0:
                #nestカウント
                nest = 0
                while True:
                    p_c += 1
                    if code[p_c] == '[':
                        nest += 1
                    if code[p_c] == ']' and nest == 0:
                        break
                    if code[p_c] == ']':
                        nest -= 1
        elif code[p_c] == ']':
            if memory[p] != 0:
                #nestカウント
                nest = 0
                while True:
                    p_c -= 1
                    if code[p_c] == ']':
                        nest += 1
                    if code[p_c] == '[' and nest == 0:
                        break
                    if code[p_c] == '[':
                        nest -= 1
        p_c += 1

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()