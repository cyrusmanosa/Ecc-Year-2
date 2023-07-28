// 分割代入
{
    //この配列の各要素を変数に取り出したい
    const array = ["1", "2", "3"];
    //この書き方が分割代入
    const [a, b, c] = array;     //a:1, b:2, c:3
    //不要な部分は飛ばすこともできる
    const [d, , e] = array;       //d:1, e:3
    //オブジェクトを取り出すこともできるが
    //受け取る側の変数名はオブジェクトのプロパティ名にする必要がある
    const { x, y, z } = { x: 1, y: 2, z: 3 };     //x:1, y:2, z:3
}

// スプレッド演算子
{
    //Math.maxは、渡された引数の中から最大のものを返す
    const maxNum = Math.max(1, 5, 3, 2, 4);
    //もし配列の中で一番大きいものを取り出したい場合
    const array2 = [1, 5, 3, 2, 4];
    //スプレッド演算子を使って渡すことができる
    const maxNum2 = Math.max(...array2);
    console.log(...array2);
}

// 残余引数
{
    //受け取った数値の合計を返す関数を作りたい
    //引数の前に...をつけると残余引数になる
    function sum(...args) {
        let total = 0;
        for (const arg of args) {
            total += arg;
        }
        return total;
    }
    console.log(sum(1, 2, 3));       //結果：6
    console.log(sum(1, 2, 3, 4));    //結果：10
}