/* 
    alert('hello Javascript'); //警告視視窗 
    let grade = prompt(`請輸入學生成績`); //輸入box
*/

/*
    console.log('Javascript'); //web console內顯示(同 print 差唔多)
    console.log( 1 + 1); //web console內顯示
*/

/*
    //變數 ( Variable )
    let age = 10;
    let language = 'javascript';

    console.log(age.language);
    age = 20;
    console.log(age);
*/


/*
    // 常數(Constant)
    const place = '香港';
    console.log(place);
*/


/*
    // 數字開頭要用$
    // _開頭都得
    // 英文先細階後大階
    let $3bc = 1;
    let _uck = 'fuck';
    console.log($3bc);
    console.log(_uck);
*/


/*
    let age = 20;
    console.log(age,typeof(age)); //Check type
    // Integer (整數)，Flot(浮點數)

    let hobbies = ['打機','打飛機',10,true];
    console.log(hobbies);

    //Object
    let person = {
        name : 'Cyrus',
        age : 30,
        goodInProgramming : true,
        hobbies : ['打機','打飛機',10,true]
    };
*/


/*
    let platform = 'youtube' + '平台';
    let lesson = 'JS入門課程';

    // console.log(platform + '上的' + lesson);
    console.log(lesson[0]); // [0] <- 第一個字
    console.log(lesson.length);

    //Escape character
    let lesson2 = " \" JS入門課程 \" "; //show 符號
    console.log(lesson2);

    // Template String 樣板字面值
    let teacher = `文家俊`;
    console.log(`在${platform}上有個${lesson2}裹, 可以跟${teacher}學習Javascript`);
    console.log('在' + platform + '上有個' + lesson2 + '裹, 可以跟' + teacher + '學習Javascript');

    //String 常用功能
    let userInput = '  學習Javascript    ';
    console.log(userInput);
    console.log(userInput.trim()); //拎走字串既空白
    console.log(userInput.trimEnd()); //拎走字串後面既空白

    let today = '2022年4月4日';
    console.log(today.substring(0,4)); //顯示字串範圍
    console.log(today.includes('山')); //搵字
    console.log(today.replace('20','30')); //將20改30（第一組）
    console.log(today.replaceAll('4','30')); //將20改30（所有組）
*/


/* 
    console.log(2**3); //2既3次方
    console.log(3%2); //3除2晚餘數

    //算術符號執行次序：括號 -＞ 指數 -＞ 成/除 -＞ 加減

    //簡短寫法
    let like = 2;
    like **= 3;
    console.log(like);

    //NaN (Not A Number)
    console.log( 1 - 'A');

    let num = 12.3456;
    console.log(num.toFixed(3)); //小數點後短（會四捨五入）
    console.log(Math.round(num)); //變成整數
    console.log(Math.round(Math.random()*100)); 
*/

/*
    // Array
    let webLanguage = ['php','javascript','python','java'];
    console.log(webLanguage[2]);

    // 2D Array
    let friends = [ ['123','456'] , ['abc','def'] ];
    console.log(friends[0][1]);

    // Array 常用功能
    console.log(webLanguage.indexOf('java')); //找尋內容位置
    console.log(webLanguage.includes('java')); //找尋內容的真偽 （有：trus)

    // 加入新元素
    webLanguage.push('Css');
    console.log(webLanguage);

    // 移除最後的番地
    webLanguage.pop();
    console.log(webLanguage);
*/


/* 
    let AAA = 0; //值和資料類別都相同於
    console.log( AAA === 0 ); 
*/


/*
    // if
    let f = 10;

    if(f == 10) 
    { console.log(true); }
    else
    { console.log(false);}

    // 簡寫
    console.log(f == 10)? true : false;
*/



/*
    // Function 功能
    // 內建功能 Build-in function
    alert();
    console.log('123');

    // 自定義功能 Custom function
    // function declaration
    function hello()
        console.log('hello');

    hello();

    // function expression 功能表達式
    const hi = function()
        console.log('hi');
    
    hi();

    // Hoisting 
    // JavaScript Declarations are Hoisted
    // Paramrter 參數
    const say = function(message , message2) // Local Variable
        console.log(message,message2);

    let message = 'hi'; // Global Variable
    console.log(message);
    say('123' , '3456');

    // 預設參數,Return(返回值)
    const rectangleArea = function( width = 3, height = 4 )
        return width * height;

    let output = rectangleArea( 1 , 2 ); // <- 優先, return 去output
    console.log(output);
*/


/*
    // Arrow Function -> Function 簡寫
    const hi = () =>  console.log('hi');

    // 只有return， 只有一句代碼時，不用寫
    const rectangleArea = ( width = 3 , height = 4 ) => width*height;
*/


/* 
    //Callback function
    const say = (callback) => callback();
    const finish = () => console.log( 'callback function' );
    say(finish);

    // 保證功能是在特定事情做好後才運行
    // 非同步 Asyncronous Javascript
    setTimeout( () => (console.log('hi')) , 4000);
    console.log('之後1');
    console.log('之後2');

    //Callback function in Array
    let webLanguage = ['php' , 'javascript' , 'python' , 'java'];
    webLanguage.forEach( (eLement) => console.log(eLement) );

    // 1. 參數整身就是一個功能
    // 2. 保證功能是在特定事情做好後才運行 （例如去資料庫拿資料，拿到後才用Callback function 去print到網頁上）
    // Asyncronous Javascript() 
*/


/* 
    // 創造新Object方式 #1 ： Object Literal
    const user = {
        name : '文家俊',
        username : 'Cyrusman1207',
        hometown : 'HongKong',
        age : 30,
        isGoodTeacher : true,
        blog : ['1234' , '5678' , '9012'],
        login(){ console.log('登入方法')},   
        logout(){ console.log('登出方法')},
        listBlog(){ console.log(this.blog)}, // this.blog 才能讀取user內的 blog , //寫法 1.function 2.Method
    }

    //更新資料
    user.name = 'Cyrus';

    // 讀取
    console.log(user.name);    // #1
    console.log(user['name']); // #2

    const key = 'hometown';    // Key 叫 Property
    console.log(user[key]);    // 不能用uer.key，讀取唔到 Hometown 內容

    user.login();

    let num = 1.2345;
    console.log(num.toFixed(2));

    user.listBlog();
 */


/*
    //選1個element
    const firstP = document.querySelector('p'); // 在Html內的第一個 P
    console.log(firstP);

    const secondP = document.querySelector('.second'); // class 名
    console.log(secondP);

    const copyrightP = document.querySelector('#copyright'); // class 名
    console.log(copyrightP);

    // 選擇多個HTML元素
    const allP = document.querySelectorAll('p');
    console.log(allP);
    console.log(allP[0]);

    allP.forEach( p => console.log(p) );
*/


// 修改文字內容 （只限顯示，HTML內沒有影響）
const p1 = document.querySelector('p');
console.log(p1);

p1.innerText = 'JavaScript介紹'; // 修改文字
p1.innerText += 'JavaScript介紹'; // 追加文字 

// 內容連帶所有div的內容一齊改
const section = document.querySelector('div');
console.log(section.innerHTML);

section.innerHTML = '<strong> 內容連帶所有HTML一齊改 </strong>'

// 修改HTML tag Attribute
const courseImg = document.querySelector('img');
console.log(courseImg.getAttribute('width'));

// 追加及修改HTML內的功能
courseImg.setAttribute('width',300);
courseImg.setAttribute('style','border: 5px solid #2196f3');
