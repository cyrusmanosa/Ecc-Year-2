<?php
//
// config.php
// ホットペッパーグルメAPIの各種設定
//

const API_KEY            = "ed7fda0f1bf044c0";
const API_VERSION        = "v1";

const API_GOURMET        = "gourmet";
const API_SHOP           = "shop";
const API_SERVICE_AREA   = "service_area";
const API_SERVICE_AREA_L = "large_service_area";
const API_AREA_L         = "large_area";
const API_AREA_M         = "middle_area";
const API_AREA_S         = "small_area";

// ホットペッパーグルメAPI  
const API_URL                    = "https://webservice.recruit.co.jp/hotpepper/";

const API_GOURMET_URL            = API_URL . API_GOURMET        . "/" . API_VERSION . "/";  // グルメサーチ
const API_SHOP_URL               = API_URL . API_SHOP           . "/" . API_VERSION . "/";  // 店名サーチ
const API_SERVICE_AREA_URL       = API_URL . API_SERVICE_AREA   . "/" . API_VERSION . "/";  // サービスエリア
const API_LARGE_SERVICE_AREA_URL = API_URL . API_SERVICE_AREA_L . "/" . API_VERSION . "/";  // 大サービスエリア
const API_AREA_L_URL             = API_URL . API_AREA_L         . "/" . API_VERSION . "/";  // 大エリア
const API_AREA_M_URL             = API_URL . API_AREA_M         . "/" . API_VERSION . "/";  // 中エリア
const API_AREA_S_URL             = API_URL . API_AREA_S         . "/" . API_VERSION . "/";  // 小エリア

// ホットペッパーグルメAPI リクエストパラメータ
const API_RESPONSE_FORMAT         = "json";
