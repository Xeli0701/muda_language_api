# muda-language-api

## docs
https://muda-language-api.herokuapp.com/docs

# 言語仕様
BrainFxck系と同じ。
| mudaLang | oraLang | BrainFxck | 解説 |
| ---- | ---- | ---- | ---- |
| muda  | ora | > | メモリポインタをインクリメント |
| MUDA | ORA | < | メモリポインタをデクリメント |
| ムダ | オラ | . | メモリポインタが指し示す先に格納された変数を処理系に表示 |
| むだ | おら | + | メモリポインタが指し示す先に格納された変数をインクリメント |
| 無駄 | 折羅 | - | メモリポインタが指し示す先に格納された変数をデクリメント |
| ﾑﾀﾞ | ｵﾗ | , | 標準入力された値をメモリポインタが指し示す先に代入 |
| 、 | 、| [ | メモリポインタが指す値が0なら、対応する"]"までskip |
| 。 | 。| ] | メモリポインタが指す値が非0なら、対応する"["までジャンプ |

## /muda/{message}
- 無駄言語を受け取り、コンパイルする。
- クエリパラメータで受け取ってるので文字数制限がある……(4000文字前後？)
- 返却値は{"inputed":(入力コード),"message":(実行結果),"status":(ステータス)}

## 関連レポジトリ
https://github.com/Xeli0701/muda_language_next