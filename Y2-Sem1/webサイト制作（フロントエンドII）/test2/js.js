// 原始的 JSON 字串
var jsonStr = '{"name": "John", "description": "A programmer"}';

// 將 JSON 字串轉換成對應的 JavaScript 物件
var jsonObj = JSON.parse(jsonStr);

// 對同一個屬性的值進行字串連接
jsonObj.description += " who loves JavaScript";

// 將 JavaScript 物件轉換回 JSON 字串
var newJsonStr = JSON.stringify(jsonObj);

// 顯示新的 JSON 字串
console.log(newJsonStr);
