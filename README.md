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
Step 1: Basic BOF (Return to Function)
内容: win() 関数などの、プログラム内に存在する「本来呼ばれないはずの場所」へジャンプさせる。
キーワード: 戻り先アドレスの書き換え、オフセットの特定。

Step 2: Shellcode Injection
内容: スタックに「シェルを起動するマシン語（シェルコード）」を自分で書き込み、そこへジャンプする。
キーワード: execve("/bin/sh")、NXビット無効化。

Step 3: ROP (Return Oriented Programming)
内容: NXビットが有効な場合、既存のコードの断片（gadget）を繋ぎ合わせて攻撃を組み立てる。
キーワード: pop rdi; ret、引数のセット、ガジェットチェーン。

Step 4: ASLR Bypass (Information Leak)
内容: 実行のたびに変わる関数の住所を、一度画面に出力（Leak）させて特定し、攻撃を成立させる。
キーワード: puts@plt、GOT Overwrite、libcベースアドレス計算。

Step 5: Modern Protections (Canary & PIE)
内容: スタックの番人（Canary）や、バイナリ自体のランダム化（PIE）をすべて突破する。
キーワード: Canary Leak、PIE Bypass。

## Heap
Step 1: Use-After-Free (UAF)
内容: free() された後のメモリ（ポインタ）が残っているのを利用して、別のデータとして読み書きする。
キーワード: 解放済みポインタ、データの混線。

Step 2: Heap Overflow
内容: ヒープ上のデータのサイズを超えて書き込み、隣にある「管理情報（メタデータ）」を破壊する。
キーワード: Chunk Metadata、Size書き換え。

Step 3: Double Free
内容: 同じ領域を2回 free() することで、メモリ管理リストを循環させ、好きな住所に malloc させる。
キーワード: tcache poisoning、Fastbin dup。

Step 4: Heap Grooming (Heap Spraying)
内容: メモリ上の配置を意図的にコントロールし、特定の場所にデータを隙間なく並べる。
キーワード: メモリレイアウトの制御。

Step 5: Advanced GLIBC Attacks
内容: 最新の libc が備えるヒープ防御（ポインタの暗号化など）を突破する。
キーワード: Tcache protection bypass、Safe-linking。
