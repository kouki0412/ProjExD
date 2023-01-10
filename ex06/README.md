# 第6回
## パックマン
### ゲーム概要
- 制限時間以内にクッキーをたくさん食べて高スコアを目指す
- 敵キャラがいるのでそれに当たらないようにしよう

### 操作方法
- 矢印キーで移動

### 基本機能
- 迷路の作成、Playerの移動

### 追加機能
- Enemyの実装

### toDo
- そもそも未完成であるので完成させる...…(TkinterからPygameに移植したら破滅して時間が無くなりました。)
- PlayerClassとEnemyClassをMazeClassの上でで管理するように変更(グリッド単位で動けるようになるため)
- Enemyを賢くさせる(今は完全ランダムにしてお茶を濁しているため)
- 迷路生成プログラムの改良(Enemyが賢くなった場合、袋小路に追いやられて詰むと考えられるので本家パックマンのようにトーラスにする)
- Enemyに触れたときにゲームオーバーにする(忘れていました...…)

### 参考資料
- コード内のコメントでも触れたましたがmaze_maker.pyを一部お借りしました。