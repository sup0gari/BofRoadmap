# BofRoadmap
バッファオーバーフローの練習をするためのリポジトリです。
64bitにおけるスタックとヒープオーバーフローを習得するためのものです。

# 免責事項
本リポジトリに掲載されている情報は、情報セキュリティの教育および学習、並びに正当な防御手法の向上を目的としています。
掲載された手法を許可されていない対象に対して実行することは違法であり、刑事罰の対象となる可能性があります。本リポジトリの内容を悪用したことにより生じたいかなる損害についても、製作者は一切の責任を負いません。
攻撃手法の理解は、より強固なセキュリティを構築するための第一歩であることを忘れないでください。

# Disclaimer
This repository is for educational and ethical security testing purposes only.
Usage of the tools or techniques provided in this repository for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws.
The author assumes no liability and is not responsible for any misuse or damage caused by this information.

## Stack
Step 1: プログラム内に存在する「本来呼ばれないはずの場所」へジャンプさせる。
1. 本来呼ばれない関数のアドレスを特定する。
2. main関数のbufferに規定のバイト数を超えて入力し、セグメンテーションフォールトを起こす。
3. rspが指すアドレスが入力したデータで上書きされるため、そのデータを利用してrspまでのオフセットを特定する。
4. そのオフセット分を適当なバイトデータで埋めて、rspが指すアドレス部分を1で求めたアドレスにする。

Step 2: スタックにシェルコードを自分で書き込み、そこへジャンプさせる。
1. 脆弱な関数で扱うバッファのアドレスを特定する。
2. 今回は64バイトで、100バイトのデータを入力し、セグメンテーションフォールトを起こす。
3. rspが指すアドレスが入力したデータで上書きされるため、そのデータを利用してrspまでのオフセットを特定する。
4. そのオフセット分に対して自身が作成したシェルコード、適当なバイトデータの順で入力。rspが指すアドレス部分をバッファのアドレスにする。
5. rspが指すアドレスはバッファのアドレスのため、シェルコードの位置にジャンプし、実行される。

Step 3: NXビットが有効な場合、既存のコードの断片（gadget）を繋ぎ合わせて攻撃を組み立てる（ROP）。

Step 4: 実行のたびに変わる関数の住所（ASLRの有効）を、一度画面に出力させて特定し、攻撃を成立させる。

Step 5: CanaryやPIEをすべて突破する。

## Heap
Step 1: free() された後のメモリ（ポインタ）が残っているのを利用して、別のデータとして読み書きする。

Step 2: ヒープ上のデータのサイズを超えて書き込み、隣にある「管理情報（メタデータ）」を破壊する。

Step 3: 同じ領域を2回 free() することで、メモリ管理リストを循環させ、好きな住所に malloc させる。

Step 4: メモリ上の配置を意図的にコントロールし、特定の場所にデータを隙間なく並べる。

Step 5: 最新の libc が備えるヒープ防御（ポインタの暗号化など）を突破する。
