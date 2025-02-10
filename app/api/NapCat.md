---
title: NapCat
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.27"
---

# NapCat

Base URLs:

# Authentication

# 用户

## POST 设置账号信息

POST /set_qq_profile

> Body 请求参数

```json
{
  "nickname": "string",
  "personal_note": "string",
  "sex": "string"
}
```

### 请求参数

| 名称            | 位置 | 类型   | 必选 | 说明     |
| --------------- | ---- | ------ | ---- | -------- |
| body            | body | object | 否   | none     |
| » nickname      | body | string | 是   | 昵称     |
| » personal_note | body | string | 是   | 个性签名 |
| » sex           | body | string | 是   | 性别     |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取推荐好友/群聊卡片

POST /ArkSharePeer

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "phoneNumber": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 否   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » user_id      | body | any    | 否   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » phoneNumber  | body | string | 否   | 对方手机号        |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "errCode": 0,
    "errMsg": "string",
    "arkJson": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称       | 类型        | 必选 | 约束 | 中文名 | 说明      |
| ---------- | ----------- | ---- | ---- | ------ | --------- |
| » status   | string      | true | none |        | none      |
| » retcode  | number      | true | none |        | none      |
| » data     | object      | true | none |        | none      |
| »» errCode | number      | true | none |        | none      |
| »» errMsg  | string      | true | none |        | none      |
| »» arkJson | string      | true | none |        | 卡片 json |
| » message  | string      | true | none |        | none      |
| » wording  | string      | true | none |        | none      |
| » echo     | string¦null | true | none |        | none      |

## POST 获取推荐群聊卡片

POST /ArkShareGroup

> Body 请求参数

```json
{
  "group_id": "string"
}
```

### 请求参数

| 名称       | 位置 | 类型   | 必选 | 说明 |
| ---------- | ---- | ------ | ---- | ---- |
| body       | body | object | 否   | none |
| » group_id | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": "string",
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明      |
| --------- | ----------- | ---- | ---- | ------ | --------- |
| » status  | string      | true | none |        | none      |
| » retcode | number      | true | none |        | none      |
| » data    | string      | true | none |        | 卡片 json |
| » message | string      | true | none |        | none      |
| » wording | string      | true | none |        | none      |
| » echo    | string¦null | true | none |        | none      |

## POST 设置在线状态

POST /set_online_status

## 状态列表

### 在线

```json5
{ status: 10, ext_status: 0, battery_status: 0 }
```

### Q 我吧

```json5
{ status: 60, ext_status: 0, battery_status: 0 }
```

### 离开

```json5
{ status: 30, ext_status: 0, battery_status: 0 }
```

### 忙碌

```json5
{ status: 50, ext_status: 0, battery_status: 0 }
```

### 请勿打扰

```json5
{ status: 70, ext_status: 0, battery_status: 0 }
```

### 隐身

```json5
{ status: 40, ext_status: 0, battery_status: 0 }
```

### 听歌中

```json5
{ status: 10, ext_status: 1028, battery_status: 0 }
```

### 春日限定

```json5
{ status: 10, ext_status: 2037, battery_status: 0 }
```

### 一起元梦

```json5
{ status: 10, ext_status: 2025, battery_status: 0 }
```

### 求星搭子

```json5
{ status: 10, ext_status: 2026, battery_status: 0 }
```

### 被掏空

```json5
{ status: 10, ext_status: 2014, battery_status: 0 }
```

### 今日天气

```json5
{ status: 10, ext_status: 1030, battery_status: 0 }
```

### 我 crash 了

```json5
{ status: 10, ext_status: 2019, battery_status: 0 }
```

### 爱你

```json5
{ status: 10, ext_status: 2006, battery_status: 0 }
```

### 恋爱中

```json5
{ status: 10, ext_status: 1051, battery_status: 0 }
```

### 好运锦鲤

```json5
{ status: 10, ext_status: 1071, battery_status: 0 }
```

### 水逆退散

```json5
{ status: 10, ext_status: 1201, battery_status: 0 }
```

### 嗨到飞起

```json5
{ status: 10, ext_status: 1056, battery_status: 0 }
```

### 元气满满

```json5
{ status: 10, ext_status: 1058, battery_status: 0 }
```

### 宝宝认证

```json5
{ status: 10, ext_status: 1070, battery_status: 0 }
```

### 一言难尽

```json5
{ status: 10, ext_status: 1063, battery_status: 0 }
```

### 难得糊涂

```json5
{ status: 10, ext_status: 2001, battery_status: 0 }
```

### emo 中

```json5
{ status: 10, ext_status: 1401, battery_status: 0 }
```

### 我太难了

```json5
{ status: 10, ext_status: 1062, battery_status: 0 }
```

### 我想开了

```json5
{ status: 10, ext_status: 2013, battery_status: 0 }
```

### 我没事

```json5
{ status: 10, ext_status: 1052, battery_status: 0 }
```

### 想静静

```json5
{ status: 10, ext_status: 1061, battery_status: 0 }
```

### 悠哉哉

```json5
{ status: 10, ext_status: 1059, battery_status: 0 }
```

### 去旅行

```json5
{ status: 10, ext_status: 2015, battery_status: 0 }
```

### 信号弱

```json5
{ status: 10, ext_status: 1011, battery_status: 0 }
```

### 出去浪

```json5
{ status: 10, ext_status: 2003, battery_status: 0 }
```

### 肝作业

```json5
{ status: 10, ext_status: 2012, battery_status: 0 }
```

### 学习中

```json5
{ status: 10, ext_status: 1018, battery_status: 0 }
```

### 搬砖中

```json5
{ status: 10, ext_status: 2023, battery_status: 0 }
```

### 摸鱼中

```json5
{ status: 10, ext_status: 1300, battery_status: 0 }
```

### 无聊中

```json5
{ status: 10, ext_status: 1060, battery_status: 0 }
```

### timi 中

```json5
{ status: 10, ext_status: 1027, battery_status: 0 }
```

### 睡觉中

```json5
{ status: 10, ext_status: 1016, battery_status: 0 }
```

### 熬夜中

```json5
{ status: 10, ext_status: 1032, battery_status: 0 }
```

### 追剧中

```json5
{ status: 10, ext_status: 1021, battery_status: 0 }
```

### 我的电量

```json5
{
  status: 10,
  ext_status: 1000,
  battery_status: 0,
}
```

> Body 请求参数

```json
{
  "status": 10,
  "ext_status": 0,
  "battery_status": 0
}
```

### 请求参数

| 名称            | 位置 | 类型   | 必选 | 说明       |
| --------------- | ---- | ------ | ---- | ---------- |
| body            | body | object | 否   | none       |
| » status        | body | number | 是   | 详情看顶部 |
| » extStatus     | body | number | 是   | 详情看顶部 |
| » batteryStatus | body | number | 是   | 电量       |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取好友分组列表

POST /get_friends_with_category

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "categoryId": 0,
      "categorySortId": 0,
      "categoryName": "string",
      "categoryMbCount": 0,
      "onlineCount": 0,
      "buddyList": [
        {
          "qid": "string",
          "longNick": "string",
          "birthday_year": 0,
          "birthday_month": 0,
          "birthday_day": 0,
          "age": 0,
          "sex": "string",
          "eMail": "string",
          "phoneNum": "string",
          "categoryId": 0,
          "richTime": 0,
          "richBuffer": {},
          "uid": "string",
          "uin": "string",
          "nick": "string",
          "remark": "string",
          "user_id": 0,
          "nickname": "string",
          "level": 0
        }
      ]
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称               | 类型                          | 必选 | 约束 | 中文名 | 说明         |
| ------------------ | ----------------------------- | ---- | ---- | ------ | ------------ |
| » status           | string                        | true | none |        | none         |
| » retcode          | number                        | true | none |        | none         |
| » data             | [object]                      | true | none |        | none         |
| »» categoryId      | number                        | true | none |        | 分组 ID      |
| »» categorySortId  | number                        | true | none |        | 分组排序 ID  |
| »» categoryName    | string                        | true | none |        | 分组名       |
| »» categoryMbCount | number                        | true | none |        | 好友数量     |
| »» onlineCount     | number                        | true | none |        | 在线好友数量 |
| »» buddyList       | [[好友信息](#schema好友信息)] | true | none |        | 好友列表     |
| »»» qid            | string                        | true | none |        | QQID         |
| »»» longNick       | string                        | true | none |        | 个性签名     |
| »»» birthday_year  | number                        | true | none |        | 生日\_年     |
| »»» birthday_month | number                        | true | none |        | 生日\_月     |
| »»» birthday_day   | number                        | true | none |        | 生日\_日     |
| »»» age            | number                        | true | none |        | 年龄         |
| »»» sex            | string                        | true | none |        | 性别         |
| »»» eMail          | string                        | true | none |        | 邮箱         |
| »»» phoneNum       | string                        | true | none |        | 手机号       |
| »»» categoryId     | number                        | true | none |        | 分类         |
| »»» richTime       | number                        | true | none |        | 注册时间     |
| »»» richBuffer     | object                        | true | none |        | none         |
| »»» uid            | string                        | true | none |        | none         |
| »»» uin            | string                        | true | none |        | none         |
| »»» nick           | string                        | true | none |        | none         |
| »»» remark         | string                        | true | none |        | 备注         |
| »»» user_id        | number                        | true | none |        | none         |
| »»» nickname       | string                        | true | none |        | none         |
| »»» level          | number                        | true | none |        | 等级         |
| » message          | string                        | true | none |        | none         |
| » wording          | string                        | true | none |        | none         |
| » echo             | string¦null                   | true | none |        | none         |

## POST 设置头像

POST /set_qq_avatar

> Body 请求参数

```json
"{\r\n    // 本地路径\r\n    \"file\": \"D:/a.jpg\"\r\n    // 网络路径\r\n    // \"file\": \"http://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png\"\r\n}"
```

### 请求参数

| 名称   | 位置 | 类型   | 必选 | 说明       |
| ------ | ---- | ------ | ---- | ---------- |
| body   | body | object | 否   | none       |
| » file | body | string | 是   | 路径或链接 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 点赞

POST /send_like

> Body 请求参数

```json
{
  "user_id": "string",
  "times": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明     |
| -------------- | ---- | ------ | ---- | -------- |
| body           | body | object | 否   | none     |
| » user_id      | body | any    | 是   | none     |
| »» _anonymous_ | body | string | 否   | none     |
| »» _anonymous_ | body | number | 否   | none     |
| » times        | body | number | 是   | 点赞次数 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 创建收藏

POST /create_collection

> Body 请求参数

```json
{
  "rawData": "http://localhost:2017/",
  "brief": "123"
}
```

### 请求参数

| 名称      | 位置 | 类型   | 必选 | 说明 |
| --------- | ---- | ------ | ---- | ---- |
| body      | body | object | 否   | none |
| » rawData | body | string | 是   | 内容 |
| » brief   | body | string | 是   | 标题 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 处理好友请求

POST /set_friend_add_request

> Body 请求参数

```json
{
  "flag": "string",
  "approve": true,
  "remark": "string"
}
```

### 请求参数

| 名称      | 位置 | 类型    | 必选 | 说明     |
| --------- | ---- | ------- | ---- | -------- |
| body      | body | object  | 否   | none     |
| » flag    | body | string  | 是   | 请求 id  |
| » approve | body | boolean | 是   | 是否同意 |
| » remark  | body | string  | 是   | 好友备注 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置个性签名

POST /set_self_longnick

> Body 请求参数

```json
{
  "longNick": "唔，瓦拉瓦拉"
}
```

### 请求参数

| 名称       | 位置 | 类型   | 必选 | 说明 |
| ---------- | ---- | ------ | ---- | ---- |
| body       | body | object | 否   | none |
| » longNick | body | string | 是   | 内容 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取账号信息

POST /get_stranger_info

> Body 请求参数

```json
{
  "user_id": 1627126029
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "user_id": 0,
    "uid": "string",
    "uin": "string",
    "nickname": "string",
    "age": 0,
    "qid": "string",
    "qqLevel": 0,
    "sex": "string",
    "long_nick": "string",
    "reg_time": 0,
    "is_vip": true,
    "is_years_vip": true,
    "vip_level": 0,
    "remark": "string",
    "status": 0,
    "login_days": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称            | 类型        | 必选 | 约束 | 中文名 | 说明         |
| --------------- | ----------- | ---- | ---- | ------ | ------------ |
| » status        | string      | true | none |        | none         |
| » retcode       | number      | true | none |        | none         |
| » data          | object      | true | none |        | none         |
| »» user_id      | number      | true | none |        | none         |
| »» uid          | string      | true | none |        | none         |
| »» uin          | string      | true | none |        | none         |
| »» nickname     | string      | true | none |        | 昵称         |
| »» age          | number      | true | none |        | 年龄         |
| »» qid          | string      | true | none |        | none         |
| »» qqLevel      | number      | true | none |        | 账号等级     |
| »» sex          | string      | true | none |        | 性别         |
| »» long_nick    | string      | true | none |        | 个性签名     |
| »» reg_time     | number      | true | none |        | 注册时间     |
| »» is_vip       | boolean     | true | none |        | 是否会员     |
| »» is_years_vip | boolean     | true | none |        | 是否年费会员 |
| »» vip_level    | number      | true | none |        | 会员等级     |
| »» remark       | string      | true | none |        | 备注         |
| »» status       | number      | true | none |        | none         |
| »» login_days   | number      | true | none |        | 连续登录天数 |
| » message       | string      | true | none |        | none         |
| » wording       | string      | true | none |        | none         |
| » echo          | string¦null | true | none |        | none         |

## POST 获取好友列表

POST /get_friend_list

> Body 请求参数

```json
{
  "no_cache": false
}
```

### 请求参数

| 名称       | 位置 | 类型    | 必选 | 说明   |
| ---------- | ---- | ------- | ---- | ------ |
| body       | body | object  | 否   | none   |
| » no_cache | body | boolean | 是   | 不缓存 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "qid": "string",
      "longNick": "string",
      "birthday_year": 0,
      "birthday_month": 0,
      "birthday_day": 0,
      "age": 0,
      "sex": "string",
      "eMail": "string",
      "phoneNum": "string",
      "categoryId": 0,
      "richTime": 0,
      "richBuffer": {},
      "uid": "string",
      "uin": "string",
      "nick": "string",
      "remark": "string",
      "user_id": 0,
      "nickname": "string",
      "level": 0
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称              | 类型        | 必选 | 约束 | 中文名 | 说明     |
| ----------------- | ----------- | ---- | ---- | ------ | -------- |
| » status          | string      | true | none |        | none     |
| » retcode         | number      | true | none |        | none     |
| » data            | [object]    | true | none |        | none     |
| »» qid            | string      | true | none |        | QQID     |
| »» longNick       | string      | true | none |        | 个性签名 |
| »» birthday_year  | number      | true | none |        | 生日\_年 |
| »» birthday_month | number      | true | none |        | 生日\_月 |
| »» birthday_day   | number      | true | none |        | 生日\_日 |
| »» age            | number      | true | none |        | 年龄     |
| »» sex            | string      | true | none |        | 性别     |
| »» eMail          | string      | true | none |        | 邮箱     |
| »» phoneNum       | string      | true | none |        | 手机号   |
| »» categoryId     | number      | true | none |        | 分类     |
| »» richTime       | number      | true | none |        | 注册时间 |
| »» richBuffer     | object      | true | none |        | none     |
| »» uid            | string      | true | none |        | none     |
| »» uin            | string      | true | none |        | none     |
| »» nick           | string      | true | none |        | none     |
| »» remark         | string      | true | none |        | 备注     |
| »» user_id        | number      | true | none |        | none     |
| »» nickname       | string      | true | none |        | none     |
| »» level          | number      | true | none |        | 等级     |
| » message         | string      | true | none |        | none     |
| » wording         | string      | true | none |        | none     |
| » echo            | string¦null | true | none |        | none     |

## POST 获取点赞列表

POST /get_profile_like

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "total_count": 0,
    "new_count": 0,
    "new_nearby_count": 0,
    "last_visit_time": 0,
    "userInfos": [
      {
        "uid": "string",
        "src": 0,
        "latestTime": 0,
        "count": 0,
        "giftCount": 0,
        "customId": 0,
        "lastCharged": 0,
        "bAvailableCnt": 0,
        "bTodayVotedCnt": 0,
        "nick": "string",
        "gender": 0,
        "age": 0,
        "isFriend": true,
        "isvip": true,
        "isSvip": true,
        "uin": 0
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                | 类型        | 必选 | 约束 | 中文名 | 说明     |
| ------------------- | ----------- | ---- | ---- | ------ | -------- |
| » status            | string      | true | none |        | none     |
| » retcode           | number      | true | none |        | none     |
| » data              | object      | true | none |        | none     |
| »» total_count      | number      | true | none |        | 总点赞数 |
| »» new_count        | number      | true | none |        | 新点赞数 |
| »» new_nearby_count | number      | true | none |        | none     |
| »» last_visit_time  | number      | true | none |        | none     |
| »» userInfos        | [object]    | true | none |        | none     |
| »»» uid             | string      | true | none |        | none     |
| »»» src             | number      | true | none |        | none     |
| »»» latestTime      | number      | true | none |        | none     |
| »»» count           | number      | true | none |        | none     |
| »»» giftCount       | number      | true | none |        | none     |
| »»» customId        | number      | true | none |        | none     |
| »»» lastCharged     | number      | true | none |        | none     |
| »»» bAvailableCnt   | number      | true | none |        | none     |
| »»» bTodayVotedCnt  | number      | true | none |        | none     |
| »»» nick            | string      | true | none |        | none     |
| »»» gender          | number      | true | none |        | none     |
| »»» age             | number      | true | none |        | none     |
| »»» isFriend        | boolean     | true | none |        | none     |
| »»» isvip           | boolean     | true | none |        | none     |
| »»» isSvip          | boolean     | true | none |        | none     |
| »»» uin             | number      | true | none |        | none     |
| » message           | string      | true | none |        | none     |
| » wording           | string      | true | none |        | none     |
| » echo              | string¦null | true | none |        | none     |

## POST 获取收藏列表

POST /get_collection_list

> Body 请求参数

```json
{
  "category": 10,
  "count": 1
}
```

### 请求参数

| 名称       | 位置 | 类型   | 必选 | 说明 |
| ---------- | ---- | ------ | ---- | ---- |
| body       | body | object | 否   | none |
| » category | body | string | 是   | none |
| » count    | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": ["string"],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [string]    | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取收藏表情

POST /fetch_custom_face

> Body 请求参数

```json
{
  "count": 40
}
```

### 请求参数

| 名称    | 位置 | 类型   | 必选 | 说明 |
| ------- | ---- | ------ | ---- | ---- |
| body    | body | object | 否   | none |
| » count | body | number | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": ["string"],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [string]    | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 上传私聊文件

POST /upload_private_file

> Body 请求参数

```json
{
  "user_id": 0,
  "file": "string",
  "name": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |
| » file         | body | string | 是   | none |
| » name         | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 删除好友

POST /delete_friend

> Body 请求参数

```json
{
  "user_id": 0,
  "friend_id": 0,
  "temp_block": true,
  "temp_both_del": true
}
```

### 请求参数

| 名称            | 位置 | 类型    | 必选 | 说明     |
| --------------- | ---- | ------- | ---- | -------- |
| body            | body | object  | 否   | none     |
| » user_id       | body | any     | 否   | none     |
| »» _anonymous_  | body | number  | 否   | none     |
| »» _anonymous_  | body | string  | 否   | none     |
| » friend_id     | body | any     | 否   | none     |
| »» _anonymous_  | body | number  | 否   | none     |
| »» _anonymous_  | body | string  | 否   | none     |
| » temp_block    | body | boolean | 是   | 拉黑     |
| » temp_both_del | body | boolean | 是   | 双向删除 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取用户状态

POST /nc_get_user_status

> Body 请求参数

```json
{
  "user_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "status": 0,
    "ext_status": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------------- | ----------- | ---- | ---- | ------ | ---- |
| » status      | string      | true | none |        | none |
| » retcode     | number      | true | none |        | none |
| » data        | object      | true | none |        | none |
| »» status     | number      | true | none |        | none |
| »» ext_status | number      | true | none |        | none |
| » message     | string      | true | none |        | none |
| » wording     | string      | true | none |        | none |
| » echo        | string¦null | true | none |        | none |

## POST 获取小程序卡片

POST /get_mini_app_ark

> Body 请求参数

```json
{
  "type": "bili",
  "title": "拾雪的一天",
  "desc": "vlog记录一天的生活",
  "picUrl": "https://thirdqq.qlogo.cn/g?b=oidb&k=09ElpZZZUTHFhoIlvs0lFg&kti=ZyBvjxHhVOI&s=640",
  "jumpUrl": "https://www.bilibili.com/video/BV1GJ411x7h7/"
}
```

### 请求参数

| 名称              | 位置 | 类型    | 必选 | 说明                         |
| ----------------- | ---- | ------- | ---- | ---------------------------- |
| body              | body | object  | 否   | none                         |
| » type            | body | string  | 否   | 只填入必须参数的话该值必须填 |
| » title           | body | string  | 是   | 标题                         |
| » desc            | body | string  | 是   | 内容                         |
| » picUrl          | body | string  | 是   | 图片链接                     |
| » jumpUrl         | body | string  | 是   | 跳转链接                     |
| » iconUrl         | body | string  | 否   | none                         |
| » sdkId           | body | string  | 否   | none                         |
| » appId           | body | string  | 否   | none                         |
| » scene           | body | any     | 否   | none                         |
| »» _anonymous_    | body | number  | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |
| » templateType    | body | any     | 否   | none                         |
| »» _anonymous_    | body | number  | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |
| » businessType    | body | any     | 否   | none                         |
| »» _anonymous_    | body | number  | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |
| » verType         | body | any     | 否   | none                         |
| »» _anonymous_    | body | number  | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |
| » shareType       | body | any     | 否   | none                         |
| »» _anonymous_    | body | number  | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |
| » versionId       | body | string  | 否   | none                         |
| » withShareTicket | body | any     | 否   | none                         |
| »» _anonymous_    | body | number  | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |
| » rawArkData      | body | any     | 否   | none                         |
| »» _anonymous_    | body | boolean | 否   | none                         |
| »» _anonymous_    | body | string  | 否   | none                         |

#### 枚举值

| 属性   | 值    |
| ------ | ----- |
| » type | bili  |
| » type | weibo |

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

# 消息

## POST 发送戳一戳

POST /send_poke

> Body 请求参数

```json
{
  "user_id": 0,
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » user_id      | body | any    | 是   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » group_id     | body | any    | 否   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选  | 约束 | 中文名 | 说明 |
| --------- | ----------- | ----- | ---- | ------ | ---- |
| » status  | string      | true  | none |        | none |
| » retcode | number      | true  | none |        | none |
| » data    | null        | false | none |        | none |
| » message | string      | true  | none |        | none |
| » wording | string      | true  | none |        | none |
| » echo    | string¦null | true  | none |        | none |

## POST 设置消息已读

POST /mark_msg_as_read

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 否   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » user_id      | body | any    | 否   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 撤回消息

POST /delete_msg

> Body 请求参数

```json
{
  "message_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » message_id   | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选  | 约束 | 中文名 | 说明 |
| --------- | ----------- | ----- | ---- | ------ | ---- |
| » status  | string      | true  | none |        | none |
| » retcode | number      | true  | none |        | none |
| » data    | null        | false | none |        | none |
| » message | string      | true  | none |        | none |
| » wording | string      | true  | none |        | none |
| » echo    | string¦null | true  | none |        | none |

## POST 获取群历史消息

POST /get_group_msg_history

> Body 请求参数

```json
{
  "group_id": 0,
  "message_seq": 0,
  "count": 0,
  "reverseOrder": true
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明              |
| -------------- | ---- | ------- | ---- | ----------------- |
| body           | body | object  | 否   | none              |
| » group_id     | body | any     | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » message_seq  | body | any     | 是   | none              |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » count        | body | number  | 是   | 数量              |
| » reverseOrder | body | boolean | 是   | 倒序              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message": [
      {
        "self_id": 0,
        "user_id": 0,
        "time": 0,
        "message_id": 0,
        "message_seq": 0,
        "real_id": 0,
        "message_type": "string",
        "sender": {
          "user_id": 0,
          "nickname": "string",
          "sex": "[",
          "age": 0,
          "card": "string",
          "role": "["
        },
        "raw_message": "string",
        "font": 0,
        "sub_type": "string",
        "message": [{}],
        "message_format": "string",
        "post_type": "string",
        "message_sent_type": "string",
        "group_id": 0
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称             | 类型                          | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ----------------------------- | ----- | ---- | ------ | ---- |
| » status         | string                        | true  | none |        | none |
| » retcode        | number                        | true  | none |        | none |
| » data           | object                        | true  | none |        | none |
| »» message       | [[消息详情](#schema消息详情)] | true  | none |        | none |
| »»» self_id      | number                        | false | none |        | none |
| »»» user_id      | number                        | false | none |        | none |
| »»» time         | number                        | false | none |        | none |
| »»» message_id   | number                        | false | none |        | none |
| »»» message_seq  | number                        | false | none |        | none |
| »»» real_id      | number                        | false | none |        | none |
| »»» message_type | string                        | false | none |        | none |
| »»» sender       | [sender](#schemasender)       | false | none |        | none |
| »»»» user_id     | number                        | true  | none |        | none |
| »»»» nickname    | string                        | true  | none |        | none |
| »»»» sex         | string                        | false | none |        | none |
| »»»» age         | number                        | false | none |        | none |
| »»»» card        | string                        | false | none |        | none |
| »»»» role        | string                        | false | none |        | none |
| »»» raw_message  | string                        | false | none |        | none |
| »»» font         | number                        | false | none |        | none |
| »»» sub_type     | string                        | false | none |        | none |
| »»» message      | [anyOf]                       | true  | none |        | none |

_anyOf_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» text      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [艾特消息](#schema艾特消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» qq        | any                         | true  | none |        | none |

_oneOf_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | number | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_continued_

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»» name | string | false | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» id        | number                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |
| »»»»»» summary   | string                      | false | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» id        | any                         | true  | none |        | none |

_oneOf_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | number | false | none |        | none |

_or_

| 名称             | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |
| »»»»» type       | string                       | true  | none |        | none |
| »»»»» data       | object                       | true  | none |        | none |
| »»»»»» data      | string                       | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [语音消息](#schema语音消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |
| »»»»» type       | string                               | true  | none |        | none |
| »»»»» data       | object                               | true  | none |        | none |
| »»»»»» content   | string                               | true  | none |        | none |

_continued_

| 名称                  | 类型        | 必选  | 约束 | 中文名 | 说明 |
| --------------------- | ----------- | ----- | ---- | ------ | ---- |
| »»» message_format    | string      | false | none |        | none |
| »»» post_type         | string      | false | none |        | none |
| »»» message_sent_type | string      | false | none |        | none |
| »»» group_id          | number      | false | none |        | none |
| » message             | string      | true  | none |        | none |
| » wording             | string      | true  | none |        | none |
| » echo                | string¦null | true  | none |        | none |

#### 枚举值

| 属性 | 值      |
| ---- | ------- |
| sex  | male    |
| sex  | female  |
| sex  | unknown |
| role | owner   |
| role | admin   |
| role | member  |

## POST 获取消息详情

POST /get_msg

> Body 请求参数

```json
{
  "message_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » message_id   | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取合并转发消息

POST /get_forward_msg

> Body 请求参数

```json
{
  "message_id": "string"
}
```

### 请求参数

| 名称         | 位置 | 类型   | 必选 | 说明 |
| ------------ | ---- | ------ | ---- | ---- |
| body         | body | object | 否   | none |
| » message_id | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取文件信息

POST /get_file

> Body 请求参数

```json
{
  "file_id": "string"
}
```

### 请求参数

| 名称      | 位置 | 类型   | 必选 | 说明 |
| --------- | ---- | ------ | ---- | ---- |
| body      | body | object | 否   | none |
| » file_id | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file": "string",
    "url": "string",
    "file_size": "string",
    "file_name": "string",
    "base64": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称         | 类型        | 必选 | 约束 | 中文名 | 说明       |
| ------------ | ----------- | ---- | ---- | ------ | ---------- |
| » status     | string      | true | none |        | none       |
| » retcode    | number      | true | none |        | none       |
| » data       | object      | true | none |        | none       |
| »» file      | string      | true | none |        | 路径或链接 |
| »» url       | string      | true | none |        | 路径或链接 |
| »» file_size | string      | true | none |        | 文件大小   |
| »» file_name | string      | true | none |        | 文件名     |
| »» base64    | string      | true | none |        | none       |
| » message    | string      | true | none |        | none       |
| » wording    | string      | true | none |        | none       |
| » echo       | string¦null | true | none |        | none       |

## POST 贴表情

POST /set_msg_emoji_like

> Body 请求参数

```json
{
  "message_id": 0,
  "emoji_id": 0,
  "set": true
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明 |
| -------------- | ---- | ------- | ---- | ---- |
| body           | body | object  | 否   | none |
| » message_id   | body | any     | 是   | none |
| »» _anonymous_ | body | number  | 否   | none |
| »» _anonymous_ | body | string  | 否   | none |
| » emoji_id     | body | number  | 是   | none |
| » set          | body | boolean | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置私聊已读

POST /mark_private_msg_as_read

> Body 请求参数

```json
{
  "user_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群聊已读

POST /mark_group_msg_as_read

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取好友历史消息

POST /get_friend_msg_history

> Body 请求参数

```json
{
  "user_id": 0,
  "message_seq": "0",
  "count": 0,
  "reverseOrder": false
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明     |
| -------------- | ---- | ------- | ---- | -------- |
| body           | body | object  | 否   | none     |
| » user_id      | body | any     | 是   | none     |
| »» _anonymous_ | body | number  | 否   | none     |
| »» _anonymous_ | body | string  | 否   | none     |
| » message_seq  | body | any     | 是   | 0 为最新 |
| »» _anonymous_ | body | string  | 否   | none     |
| »» _anonymous_ | body | number  | 否   | none     |
| » count        | body | number  | 是   | 数量     |
| » reverseOrder | body | boolean | 是   | 倒序     |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "messages": [
      {
        "self_id": 0,
        "user_id": 0,
        "time": 0,
        "message_id": 0,
        "message_seq": 0,
        "real_id": 0,
        "message_type": "string",
        "sender": {
          "user_id": 0,
          "nickname": "string",
          "sex": "[",
          "age": 0,
          "card": "string",
          "role": "["
        },
        "raw_message": "string",
        "font": 0,
        "sub_type": "string",
        "message": [{}],
        "message_format": "string",
        "post_type": "string",
        "message_sent_type": "string",
        "group_id": 0
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称             | 类型                          | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ----------------------------- | ----- | ---- | ------ | ---- |
| » status         | string                        | true  | none |        | none |
| » retcode        | number                        | true  | none |        | none |
| » data           | object                        | true  | none |        | none |
| »» messages      | [[消息详情](#schema消息详情)] | true  | none |        | none |
| »»» self_id      | number                        | false | none |        | none |
| »»» user_id      | number                        | false | none |        | none |
| »»» time         | number                        | false | none |        | none |
| »»» message_id   | number                        | false | none |        | none |
| »»» message_seq  | number                        | false | none |        | none |
| »»» real_id      | number                        | false | none |        | none |
| »»» message_type | string                        | false | none |        | none |
| »»» sender       | [sender](#schemasender)       | false | none |        | none |
| »»»» user_id     | number                        | true  | none |        | none |
| »»»» nickname    | string                        | true  | none |        | none |
| »»»» sex         | string                        | false | none |        | none |
| »»»» age         | number                        | false | none |        | none |
| »»»» card        | string                        | false | none |        | none |
| »»»» role        | string                        | false | none |        | none |
| »»» raw_message  | string                        | false | none |        | none |
| »»» font         | number                        | false | none |        | none |
| »»» sub_type     | string                        | false | none |        | none |
| »»» message      | [anyOf]                       | true  | none |        | none |

_anyOf_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» text      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [艾特消息](#schema艾特消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» qq        | any                         | true  | none |        | none |

_oneOf_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | number | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_continued_

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»» name | string | false | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» id        | number                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |
| »»»»»» summary   | string                      | false | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» id        | any                         | true  | none |        | none |

_oneOf_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | number | false | none |        | none |

_or_

| 名称             | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |
| »»»»» type       | string                       | true  | none |        | none |
| »»»»» data       | object                       | true  | none |        | none |
| »»»»»» data      | string                       | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [语音消息](#schema语音消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |
| »»»»» type       | string                               | true  | none |        | none |
| »»»»» data       | object                               | true  | none |        | none |
| »»»»»» content   | string                               | true  | none |        | none |

_continued_

| 名称                  | 类型        | 必选  | 约束 | 中文名 | 说明 |
| --------------------- | ----------- | ----- | ---- | ------ | ---- |
| »»» message_format    | string      | false | none |        | none |
| »»» post_type         | string      | false | none |        | none |
| »»» message_sent_type | string      | false | none |        | none |
| »»» group_id          | number      | false | none |        | none |
| » message             | string      | true  | none |        | none |
| » wording             | string      | true  | none |        | none |
| » echo                | string¦null | true  | none |        | none |

#### 枚举值

| 属性 | 值      |
| ---- | ------- |
| sex  | male    |
| sex  | female  |
| sex  | unknown |
| role | owner   |
| role | admin   |
| role | member  |

## POST 最近消息列表

POST /get_recent_contact

获取的最新消息是每个会话最新的消息

> Body 请求参数

```json
{
  "count": 10
}
```

### 请求参数

| 名称    | 位置 | 类型   | 必选 | 说明     |
| ------- | ---- | ------ | ---- | -------- |
| body    | body | object | 否   | none     |
| » count | body | number | 是   | 会话数量 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "lastestMsg": {
        "self_id": 0,
        "user_id": 0,
        "time": 0,
        "message_type": "string",
        "sender": {
          "user_id": 0,
          "nickname": "string",
          "sex": "[",
          "age": 0,
          "card": "string",
          "role": "["
        },
        "raw_message": "string",
        "font": 0,
        "sub_type": "string",
        "message": [{}],
        "message_format": "string",
        "post_type": "string",
        "group_id": 0
      },
      "peerUin": "string",
      "remark": "string",
      "msgTime": "string",
      "chatType": 0,
      "msgId": "string",
      "sendNickName": "string",
      "sendMemberName": "string",
      "peerName": "string"
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称             | 类型                    | 必选  | 约束 | 中文名 | 说明         |
| ---------------- | ----------------------- | ----- | ---- | ------ | ------------ |
| » status         | string                  | true  | none |        | none         |
| » retcode        | number                  | true  | none |        | none         |
| » data           | [object]                | true  | none |        | none         |
| »» lastestMsg    | object                  | false | none |        | 最新消息内容 |
| »»» self_id      | number                  | true  | none |        | none         |
| »»» user_id      | number                  | true  | none |        | none         |
| »»» time         | number                  | true  | none |        | none         |
| »»» message_type | string                  | true  | none |        | none         |
| »»» sender       | [sender](#schemasender) | true  | none |        | none         |
| »»»» user_id     | number                  | true  | none |        | none         |
| »»»» nickname    | string                  | true  | none |        | none         |
| »»»» sex         | string                  | false | none |        | none         |
| »»»» age         | number                  | false | none |        | none         |
| »»»» card        | string                  | false | none |        | none         |
| »»»» role        | string                  | false | none |        | none         |
| »»» raw_message  | string                  | true  | none |        | none         |
| »»» font         | number                  | true  | none |        | none         |
| »»» sub_type     | string                  | true  | none |        | none         |
| »»» message      | [anyOf]                 | true  | none |        | none         |

_anyOf_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» text      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [艾特消息](#schema艾特消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» qq        | any                         | true  | none |        | none |

_oneOf_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | number | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_continued_

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»» name | string | false | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» id        | number                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |
| »»»»»» summary   | string                      | false | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» id        | any                         | true  | none |        | none |

_oneOf_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称                | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------- | ------ | ----- | ---- | ------ | ---- |
| »»»»»»» _anonymous_ | number | false | none |        | none |

_or_

| 名称             | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |
| »»»»» type       | string                       | true  | none |        | none |
| »»»»» data       | object                       | true  | none |        | none |
| »»»»»» data      | string                       | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [语音消息](#schema语音消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |
| »»»»» type       | string                      | true  | none |        | none |
| »»»»» data       | object                      | true  | none |        | none |
| »»»»»» file      | string                      | true  | none |        | none |

_or_

| 名称             | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |
| »»»»» type       | string                               | true  | none |        | none |
| »»»»» data       | object                               | true  | none |        | none |
| »»»»»» content   | string                               | true  | none |        | none |

_continued_

| 名称               | 类型        | 必选 | 约束 | 中文名 | 说明       |
| ------------------ | ----------- | ---- | ---- | ------ | ---------- |
| »»» message_format | string      | true | none |        | none       |
| »»» post_type      | string      | true | none |        | none       |
| »»» group_id       | number      | true | none |        | none       |
| »» peerUin         | string      | true | none |        | 对方账号   |
| »» remark          | string      | true | none |        | none       |
| »» msgTime         | string      | true | none |        | 消息时间   |
| »» chatType        | number      | true | none |        | none       |
| »» msgId           | string      | true | none |        | none       |
| »» sendNickName    | string      | true | none |        | 发送人昵称 |
| »» sendMemberName  | string      | true | none |        | none       |
| »» peerName        | string      | true | none |        | 对方昵称   |
| » message          | string      | true | none |        | none       |
| » wording          | string      | true | none |        | none       |
| » echo             | string¦null | true | none |        | none       |

#### 枚举值

| 属性 | 值      |
| ---- | ------- |
| sex  | male    |
| sex  | female  |
| sex  | unknown |
| role | owner   |
| role | admin   |
| role | member  |

## POST \_设置所有消息已读

POST /\_mark_all_as_read

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取贴表情详情

POST /fetch_emoji_like

> Body 请求参数

```json
{
  "message_id": 123456,
  "emojiId": "97",
  "emojiType": "1"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » message_id   | body | any    | 是   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » emojiId      | body | string | 是   | 表情 ID           |
| » emojiType    | body | string | 是   | 表情类型          |
| » group_id     | body | any    | 否   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » user_id      | body | any    | 否   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » count        | body | number | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string",
    "emojiLikesList": [
      {
        "tinyId": "string",
        "nickName": "string",
        "headUrl": "string"
      }
    ],
    "cookie": "string",
    "isLastPage": true,
    "isFirstPage": true
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称              | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ----------------- | ----------- | ---- | ---- | ------ | ---- |
| » status          | string      | true | none |        | none |
| » retcode         | number      | true | none |        | none |
| » data            | object      | true | none |        | none |
| »» result         | number      | true | none |        | none |
| »» errMsg         | string      | true | none |        | none |
| »» emojiLikesList | [object]    | true | none |        | none |
| »»» tinyId        | string      | true | none |        | none |
| »»» nickName      | string      | true | none |        | none |
| »»» headUrl       | string      | true | none |        | none |
| »» cookie         | string      | true | none |        | none |
| »» isLastPage     | boolean     | true | none |        | none |
| »» isFirstPage    | boolean     | true | none |        | none |
| » message         | string      | true | none |        | none |
| » wording         | string      | true | none |        | none |
| » echo            | string¦null | true | none |        | none |

## POST 发送合并转发消息

POST /send_forward_msg

> Body 请求参数

```json
{
  "group_id": "1017767274",
  "messages": [
    {
      "type": "node",
      "data": {
        "user_id": 97,
        "nickname": "达艳",
        "content": [
          {
            "type": "text",
            "data": {
              "text": "test"
            }
          }
        ]
      }
    }
  ],
  "prompt": "enim est dolore et"
}
```

### 请求参数

| 名称                | 位置 | 类型                                          | 必选 | 说明              |
| ------------------- | ---- | --------------------------------------------- | ---- | ----------------- |
| body                | body | object                                        | 否   | none              |
| » group_id          | body | any                                           | 否   | 和 user_id 二选一 |
| »» _anonymous_      | body | number                                        | 否   | none              |
| »» _anonymous_      | body | string                                        | 否   | none              |
| » user_id           | body | any                                           | 否   | none              |
| »» _anonymous_      | body | number                                        | 否   | none              |
| »» _anonymous_      | body | string                                        | 否   | none              |
| » messages          | body | [[一级合并转发消息](#schema一级合并转发消息)] | 是   | none              |
| »» type             | body | string                                        | 是   | none              |
| »» data             | body | object                                        | 是   | none              |
| »»» user_id         | body | any                                           | 是   | none              |
| »»»» _anonymous_    | body | string                                        | 否   | none              |
| »»»» _anonymous_    | body | number                                        | 否   | none              |
| »»» nickname        | body | string                                        | 是   | none              |
| »»» content         | body | [anyOf]                                       | 是   | 构建              |
| »»»» _anonymous_    | body | [文本消息](#schema文本消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» text         | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [表情消息](#schema表情消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» id           | body | number                                        | 是   | none              |
| »»»» _anonymous_    | body | [图片消息](#schema图片消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» file         | body | string                                        | 是   | none              |
| »»»»»» summary      | body | string                                        | 否   | none              |
| »»»» _anonymous_    | body | [回复消息](#schema回复消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» id           | body | any                                           | 是   | none              |
| »»»»»»» _anonymous_ | body | string                                        | 否   | none              |
| »»»»»»» _anonymous_ | body | number                                        | 否   | none              |
| »»»» _anonymous_    | body | [JSON 消息](#schemajson消息)                  | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» data         | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [视频消息](#schema视频消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» file         | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [markdown 消息](#schemamarkdown消息)          | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» content      | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [发送 forward](#schema发送forward)            | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» user_id      | body | any                                           | 是   | none              |
| »»»»»»» _anonymous_ | body | number                                        | 否   | none              |
| »»»»»»» _anonymous_ | body | string                                        | 否   | none              |
| »»»»»» nickname     | body | string                                        | 是   | none              |
| »»»»»» content      | body | object                                        | 是   | none              |
| »»»»»»» type        | body | string                                        | 是   | none              |
| »»»»»»» data        | body | object                                        | 是   | none              |
| »»»»»»»» id         | body | string                                        | 是   | res_id            |
| »»»» _anonymous_    | body | [二级合并转发消息](#schema二级合并转发消息)   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» user_id      | body | any                                           | 是   | none              |
| »»»»»»» _anonymous_ | body | string                                        | 否   | none              |
| »»»»»»» _anonymous_ | body | number                                        | 否   | none              |
| »»»»»» nickname     | body | string                                        | 是   | none              |
| »»»»»» content      | body | [anyOf]                                       | 是   | 构建              |
| »»»»»»» _anonymous_ | body | [文本消息](#schema文本消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [表情消息](#schema表情消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [图片消息](#schema图片消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [回复消息](#schema回复消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [JSON 消息](#schemajson消息)                  | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [视频消息](#schema视频消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [markdown 消息](#schemamarkdown消息)          | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [发送 forward](#schema发送forward)            | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [二级合并转发消息](#schema二级合并转发消息)   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»» news         | body | [object]                                      | 否   | 外显              |
| »»»»»»» text        | body | string                                        | 是   | 内容              |
| »»»»»» prompt       | body | string                                        | 否   | 外显              |
| »»»»»» summary      | body | string                                        | 否   | 底下文本          |
| »»»»»» source       | body | string                                        | 否   | 标题              |
| » news              | body | [object]                                      | 是   | none              |
| »» text             | body | string                                        | 是   | none              |
| » prompt            | body | string                                        | 是   | 外显              |
| » summary           | body | string                                        | 是   | 底下文本          |
| » source            | body | string                                        | 是   | 内容              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取语音消息详情

POST /get_record

> Body 请求参数

```json
{
  "file_id": "000000924e61704361744f6e65426f747c4d736746696c657c327c3739303531343031397c373433313532313837383033323238303633367c373433313532313837383033323238303633357c.cd8e41763598ae7c0b7dd348d5d4804f.amr",
  "out_format": "amr"
}
```

### 请求参数

| 名称         | 位置 | 类型   | 必选 | 说明 |
| ------------ | ---- | ------ | ---- | ---- |
| body         | body | object | 否   | none |
| » file       | body | string | 是   | none |
| » out_format | body | string | 是   | none |

#### 枚举值

| 属性         | 值   |
| ------------ | ---- |
| » out_format | mp3  |
| » out_format | amr  |
| » out_format | wma  |
| » out_format | m4a  |
| » out_format | spx  |
| » out_format | ogg  |
| » out_format | wav  |
| » out_format | flac |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file": "string",
    "url": "string",
    "file_size": "string",
    "file_name": "string",
    "base64": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称         | 类型        | 必选 | 约束 | 中文名 | 说明     |
| ------------ | ----------- | ---- | ---- | ------ | -------- |
| » status     | string      | true | none |        | none     |
| » retcode    | number      | true | none |        | none     |
| » data       | object      | true | none |        | none     |
| »» file      | string      | true | none |        | 本地路径 |
| »» url       | string      | true | none |        | 网络路径 |
| »» file_size | string      | true | none |        | 文件大小 |
| »» file_name | string      | true | none |        | 文件名   |
| »» base64    | string      | true | none |        | none     |
| » message    | string      | true | none |        | none     |
| » wording    | string      | true | none |        | none     |
| » echo       | string¦null | true | none |        | none     |

## POST 获取图片消息详情

POST /get_image

> Body 请求参数

```json
{
  "file_id": "000001464e61704361744f6e65426f747c4d736746696c657c327c3739303531343031397c373433313532303534363631393630373832387c373433313532303534363631393630373832377c456851564b524a367737624c702d3739614f3554474752477050585543426a68374155675f776f6f337376687966693169514d794248427962325251674c326a41566f5161325145364b71595356456c5455716f364372676a51.CFCF5923363D36B9A27BC1224F8462A9.jpg"
}
```

### 请求参数

| 名称      | 位置 | 类型   | 必选 | 说明 |
| --------- | ---- | ------ | ---- | ---- |
| body      | body | object | 否   | none |
| » file_id | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file": "string",
    "url": "string",
    "file_size": "string",
    "file_name": "string",
    "base64": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称         | 类型        | 必选 | 约束 | 中文名 | 说明     |
| ------------ | ----------- | ---- | ---- | ------ | -------- |
| » status     | string      | true | none |        | none     |
| » retcode    | number      | true | none |        | none     |
| » data       | object      | true | none |        | none     |
| »» file      | string      | true | none |        | 本地路径 |
| »» url       | string      | true | none |        | 网络路径 |
| »» file_size | string      | true | none |        | 文件大小 |
| »» file_name | string      | true | none |        | 文件名   |
| »» base64    | string      | true | none |        | none     |
| » message    | string      | true | none |        | none     |
| » wording    | string      | true | none |        | none     |
| » echo       | string¦null | true | none |        | none     |

# 消息/发送群聊消息

## POST 发送群合并转发消息

POST /send_group_forward_msg

> Body 请求参数

```json
{
  "group_id": 0,
  "messages": [
    {
      "type": "node",
      "data": {
        "user_id": "string",
        "nickname": "string",
        "content": [{}]
      }
    }
  ],
  "news": [
    {
      "text": "string"
    }
  ],
  "prompt": "string",
  "summary": "string",
  "source": "string"
}
```

### 请求参数

| 名称                | 位置 | 类型                                          | 必选 | 说明              |
| ------------------- | ---- | --------------------------------------------- | ---- | ----------------- |
| body                | body | object                                        | 否   | none              |
| » group_id          | body | any                                           | 是   | 和 user_id 二选一 |
| »» _anonymous_      | body | number                                        | 否   | none              |
| »» _anonymous_      | body | string                                        | 否   | none              |
| » messages          | body | [[一级合并转发消息](#schema一级合并转发消息)] | 是   | none              |
| »» type             | body | string                                        | 是   | none              |
| »» data             | body | object                                        | 是   | none              |
| »»» user_id         | body | any                                           | 是   | none              |
| »»»» _anonymous_    | body | string                                        | 否   | none              |
| »»»» _anonymous_    | body | number                                        | 否   | none              |
| »»» nickname        | body | string                                        | 是   | none              |
| »»» content         | body | [anyOf]                                       | 是   | 构建              |
| »»»» _anonymous_    | body | [文本消息](#schema文本消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» text         | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [表情消息](#schema表情消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» id           | body | number                                        | 是   | none              |
| »»»» _anonymous_    | body | [图片消息](#schema图片消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» file         | body | string                                        | 是   | none              |
| »»»»»» summary      | body | string                                        | 否   | none              |
| »»»» _anonymous_    | body | [回复消息](#schema回复消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» id           | body | any                                           | 是   | none              |
| »»»»»»» _anonymous_ | body | string                                        | 否   | none              |
| »»»»»»» _anonymous_ | body | number                                        | 否   | none              |
| »»»» _anonymous_    | body | [JSON 消息](#schemajson消息)                  | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» data         | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [视频消息](#schema视频消息)                   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» file         | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [markdown 消息](#schemamarkdown消息)          | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» content      | body | string                                        | 是   | none              |
| »»»» _anonymous_    | body | [发送 forward](#schema发送forward)            | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» user_id      | body | any                                           | 是   | none              |
| »»»»»»» _anonymous_ | body | number                                        | 否   | none              |
| »»»»»»» _anonymous_ | body | string                                        | 否   | none              |
| »»»»»» nickname     | body | string                                        | 是   | none              |
| »»»»»» content      | body | object                                        | 是   | none              |
| »»»»»»» type        | body | string                                        | 是   | none              |
| »»»»»»» data        | body | object                                        | 是   | none              |
| »»»»»»»» id         | body | string                                        | 是   | res_id            |
| »»»» _anonymous_    | body | [二级合并转发消息](#schema二级合并转发消息)   | 否   | none              |
| »»»»» type          | body | string                                        | 是   | none              |
| »»»»» data          | body | object                                        | 是   | none              |
| »»»»»» user_id      | body | any                                           | 是   | none              |
| »»»»»»» _anonymous_ | body | string                                        | 否   | none              |
| »»»»»»» _anonymous_ | body | number                                        | 否   | none              |
| »»»»»» nickname     | body | string                                        | 是   | none              |
| »»»»»» content      | body | [anyOf]                                       | 是   | 构建              |
| »»»»»»» _anonymous_ | body | [文本消息](#schema文本消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [表情消息](#schema表情消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [图片消息](#schema图片消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [回复消息](#schema回复消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [JSON 消息](#schemajson消息)                  | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [视频消息](#schema视频消息)                   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [markdown 消息](#schemamarkdown消息)          | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [发送 forward](#schema发送forward)            | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»»» _anonymous_ | body | [二级合并转发消息](#schema二级合并转发消息)   | 否   | none              |
| »»»»»»»» type       | body | string                                        | 是   | none              |
| »»»»»»»» data       | body | object                                        | 是   | none              |
| »»»»»» news         | body | [object]                                      | 否   | 外显              |
| »»»»»»» text        | body | string                                        | 是   | 内容              |
| »»»»»» prompt       | body | string                                        | 否   | 外显              |
| »»»»»» summary      | body | string                                        | 否   | 底下文本          |
| »»»»»» source       | body | string                                        | 否   | 标题              |
| » news              | body | [object]                                      | 是   | none              |
| »» text             | body | string                                        | 是   | none              |
| » prompt            | body | string                                        | 是   | 外显              |
| » summary           | body | string                                        | 是   | 底下文本          |
| » source            | body | string                                        | 是   | 内容              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_id": 0,
    "res_id": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------------- | ----------- | ---- | ---- | ------ | ---- |
| » status      | string      | true | none |        | none |
| » retcode     | number      | true | none |        | none |
| » data        | object      | true | none |        | none |
| »» message_id | number      | true | none |        | none |
| »» res_id     | string      | true | none |        | none |
| » message     | string      | true | none |        | none |
| » wording     | string      | true | none |        | none |
| » echo        | string¦null | true | none |        | none |

## POST 消息转发到群

POST /forward_group_single_msg

> Body 请求参数

```json
{
  "group_id": 0,
  "message_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » message_id   | body | any    | 是   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 发送群聊戳一戳

POST /group_poke

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » user_id      | body | any    | 是   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

# 消息/发送私聊消息

## POST 发送私聊合并转发消息

POST /send_private_forward_msg

> Body 请求参数

```json
{
  "user_id": 0,
  "messages": [
    {
      "type": "node",
      "data": {
        "nickname": "string",
        "user_id": 0,
        "content": [{}]
      }
    }
  ]
}
```

### 请求参数

| 名称                | 位置 | 类型                         | 必选 | 说明 |
| ------------------- | ---- | ---------------------------- | ---- | ---- |
| body                | body | object                       | 否   | none |
| » user_id           | body | any                          | 是   | none |
| »» _anonymous_      | body | number                       | 否   | none |
| »» _anonymous_      | body | string                       | 否   | none |
| » messages          | body | [object]                     | 是   | none |
| »» type             | body | string                       | 是   | none |
| »» data             | body | object                       | 是   | none |
| »»» nickname        | body | string                       | 是   | none |
| »»» user_id         | body | any                          | 是   | none |
| »»»» _anonymous_    | body | number                       | 否   | none |
| »»»» _anonymous_    | body | string                       | 否   | none |
| »»» content         | body | [anyOf]                      | 是   | none |
| »»»» _anonymous_    | body | [文本消息](#schema文本消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» text         | body | string                       | 是   | none |
| »»»» _anonymous_    | body | [艾特消息](#schema艾特消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» qq           | body | any                          | 是   | none |
| »»»»»»» _anonymous_ | body | string                       | 否   | none |
| »»»»»»» _anonymous_ | body | number                       | 否   | none |
| »»»»»»» _anonymous_ | body | string                       | 否   | none |
| »»»»»» name         | body | string                       | 否   | none |
| »»»» _anonymous_    | body | [表情消息](#schema表情消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» id           | body | number                       | 是   | none |
| »»»» _anonymous_    | body | [图片消息](#schema图片消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» file         | body | string                       | 是   | none |
| »»»»»» summary      | body | string                       | 否   | none |
| »»»» _anonymous_    | body | [回复消息](#schema回复消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» id           | body | any                          | 是   | none |
| »»»»»»» _anonymous_ | body | string                       | 否   | none |
| »»»»»»» _anonymous_ | body | number                       | 否   | none |
| »»»» _anonymous_    | body | [JSON 消息](#schemajson消息) | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» data         | body | string                       | 是   | none |
| »»»» _anonymous_    | body | [语音消息](#schema语音消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» file         | body | string                       | 是   | none |
| »»»» _anonymous_    | body | [视频消息](#schema视频消息)  | 否   | none |
| »»»»» type          | body | string                       | 是   | none |
| »»»»» data          | body | object                       | 是   | none |
| »»»»»» file         | body | string                       | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_id": 0,
    "res_id": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------------- | ----------- | ---- | ---- | ------ | ---- |
| » status      | string      | true | none |        | none |
| » retcode     | number      | true | none |        | none |
| » data        | object      | true | none |        | none |
| »» message_id | number      | true | none |        | none |
| »» res_id     | string      | true | none |        | none |
| » message     | string      | true | none |        | none |
| » wording     | string      | true | none |        | none |
| » echo        | string¦null | true | none |        | none |

## POST 消息转发到私聊

POST /forward_friend_single_msg

> Body 请求参数

```json
{
  "user_id": 0,
  "message_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |
| » message_id   | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 发送私聊戳一戳

POST /friend_poke

> Body 请求参数

```json
{
  "user_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

# 群组

## POST 群踢人

POST /set_group_kick

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "reject_add_request": true
}
```

### 请求参数

| 名称                 | 位置 | 类型    | 必选 | 说明              |
| -------------------- | ---- | ------- | ---- | ----------------- |
| body                 | body | object  | 否   | none              |
| » group_id           | body | any     | 是   | 和 user_id 二选一 |
| »» _anonymous_       | body | number  | 否   | none              |
| »» _anonymous_       | body | string  | 否   | none              |
| » user_id            | body | any     | 是   | none              |
| »» _anonymous_       | body | number  | 否   | none              |
| »» _anonymous_       | body | string  | 否   | none              |
| » reject_add_request | body | boolean | 是   | 是否群拉黑        |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群系统消息

POST /get_group_system_msg

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "InvitedRequest": [
      {
        "request_id": "string",
        "invitor_uin": "string",
        "invitor_nick": "string",
        "group_id": "string",
        "group_name": "string",
        "checked": true,
        "actor": "string"
      }
    ],
    "join_requests": [
      {
        "request_id": "string",
        "requester_uin": "string",
        "requester_nick": "string",
        "group_id": "string",
        "group_name": "string",
        "checked": true,
        "actor": "string"
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称              | 类型     | 必选 | 约束 | 中文名 | 说明 |
| ----------------- | -------- | ---- | ---- | ------ | ---- |
| » status          | string   | true | none |        | none |
| » retcode         | number   | true | none |        | none |
| » data            | object   | true | none |        | none |
| »» InvitedRequest | [object] | true | none |        | none |
| »»» request_id    | string   | true | none |        | none |
| »»» invitor_uin   | string   | true | none |        | none |
| »»» invitor_nick  | string   | true | none |        | none |
| »»» group_id      | string   | true | none |        | none |
| »»» group_name    | string   | true | none |        | none |
| »»» checked       | boolean  | true | none |        | none |
| »»» actor         | any      | true | none |        | none |

_oneOf_

| 名称             | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称             | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | number | false | none |        | none |

_continued_

| 名称               | 类型     | 必选 | 约束 | 中文名 | 说明 |
| ------------------ | -------- | ---- | ---- | ------ | ---- |
| »» join_requests   | [object] | true | none |        | none |
| »»» request_id     | string   | true | none |        | none |
| »»» requester_uin  | string   | true | none |        | none |
| »»» requester_nick | string   | true | none |        | none |
| »»» group_id       | string   | true | none |        | none |
| »»» group_name     | string   | true | none |        | none |
| »»» checked        | boolean  | true | none |        | none |
| »»» actor          | any      | true | none |        | none |

_oneOf_

| 名称             | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称             | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | number | false | none |        | none |

_continued_

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 群禁言

POST /set_group_ban

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "duration": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » user_id      | body | any    | 是   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » duration     | body | number | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群精华消息

POST /get_essence_msg_list

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "msg_seq": 0,
      "msg_random": 0,
      "sender_id": 0,
      "sender_nick": "string",
      "operator_id": 0,
      "operator_nick": "string",
      "message_id": "string",
      "operator_time": "string",
      "content": [
        {
          "type": null,
          "data": null
        }
      ]
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称             | 类型     | 必选 | 约束 | 中文名 | 说明       |
| ---------------- | -------- | ---- | ---- | ------ | ---------- |
| » status         | string   | true | none |        | none       |
| » retcode        | number   | true | none |        | none       |
| » data           | [object] | true | none |        | none       |
| »» msg_seq       | number   | true | none |        | none       |
| »» msg_random    | number   | true | none |        | none       |
| »» sender_id     | number   | true | none |        | 发送人账号 |
| »» sender_nick   | string   | true | none |        | 发送人昵称 |
| »» operator_id   | number   | true | none |        | 设精人账号 |
| »» operator_nick | string   | true | none |        | 设精人昵称 |
| »» message_id    | string   | true | none |        | none       |
| »» operator_time | string   | true | none |        | 设精时间   |
| »» content       | [anyOf]  | true | none |        | 消息内容   |

_anyOf_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» text      | string                      | true  | none |        | none |

_or_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [艾特消息](#schema艾特消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» qq        | any                         | true  | none |        | none |

_oneOf_

| 名称               | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------ | ------ | ----- | ---- | ------ | ---- |
| »»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称               | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------ | ------ | ----- | ---- | ------ | ---- |
| »»»»»» _anonymous_ | number | false | none |        | none |

_xor_

| 名称               | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------ | ------ | ----- | ---- | ------ | ---- |
| »»»»»» _anonymous_ | string | false | none |        | none |

_continued_

| 名称       | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------- | ------ | ----- | ---- | ------ | ---- |
| »»»»» name | string | false | none |        | none |

_or_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» id        | number                      | true  | none |        | none |

_or_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» file      | string                      | true  | none |        | none |
| »»»»» summary   | string                      | false | none |        | none |

_or_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» id        | any                         | true  | none |        | none |

_oneOf_

| 名称               | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------ | ------ | ----- | ---- | ------ | ---- |
| »»»»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称               | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------------------ | ------ | ----- | ---- | ------ | ---- |
| »»»»»» _anonymous_ | number | false | none |        | none |

_or_

| 名称            | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| --------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |
| »»»» type       | string                       | true  | none |        | none |
| »»»» data       | object                       | true  | none |        | none |
| »»»»» data      | string                       | true  | none |        | none |

_or_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [语音消息](#schema语音消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» file      | string                      | true  | none |        | none |

_or_

| 名称            | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| --------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |
| »»»» type       | string                      | true  | none |        | none |
| »»»» data       | object                      | true  | none |        | none |
| »»»»» file      | string                      | true  | none |        | none |

_or_

| 名称            | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| --------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| »»» _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |
| »»»» type       | string                               | true  | none |        | none |
| »»»» data       | object                               | true  | none |        | none |
| »»»»» content   | string                               | true  | none |        | none |

_continued_

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 全体禁言

POST /set_group_whole_ban

> Body 请求参数

```json
{
  "group_id": 0,
  "enable": true
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明              |
| -------------- | ---- | ------- | ---- | ----------------- |
| body           | body | object  | 否   | none              |
| » group_id     | body | any     | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » enable       | body | boolean | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群头像

POST /set_group_portrait

> Body 请求参数

```json
"{\r\n    \"group_id\": 123456,\r\n    //网络路径\r\n    \"file\": \"http://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png\"\r\n    // 本地路径\r\n    //\"file\": \"file://D:/a.jpg\"\r\n                \r\n}"
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » file         | body | string | 是   | none              |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "success"
  },
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | string      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群管理

POST /set_group_admin

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "enable": true
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明              |
| -------------- | ---- | ------- | ---- | ----------------- |
| body           | body | object  | 否   | none              |
| » group_id     | body | any     | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » user_id      | body | any     | 是   | none              |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » enable       | body | boolean | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群成员名片

POST /set_group_card

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "card": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明               |
| -------------- | ---- | ------ | ---- | ------------------ |
| body           | body | object | 否   | none               |
| » group_id     | body | any    | 是   | 和 user_id 二选一  |
| »» _anonymous_ | body | number | 否   | none               |
| »» _anonymous_ | body | string | 否   | none               |
| » user_id      | body | any    | 是   | none               |
| »» _anonymous_ | body | number | 否   | none               |
| »» _anonymous_ | body | string | 否   | none               |
| » card         | body | string | 是   | 为空则为取消群名片 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群精华消息

POST /set_essence_msg

> Body 请求参数

```json
{
  "message_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » message_id   | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "errCode": 0,
    "errMsg": "success",
    "result": {
      "wording": "",
      "digestUin": "0",
      "digestTime": 0,
      "msg": {
        "groupCode": "0",
        "msgSeq": 0,
        "msgRandom": 0,
        "msgContent": [],
        "textSize": "0",
        "picSize": "0",
        "videoSize": "0",
        "senderUin": "0",
        "senderTime": 0,
        "addDigestUin": "0",
        "addDigestTime": 0,
        "startTime": 0,
        "latestMsgSeq": 0,
        "opType": 0
      },
      "errorCode": 0
    }
  },
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群名

POST /set_group_name

> Body 请求参数

```json
{
  "group_id": 0,
  "group_name": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » group_name   | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 删除群精华消息

POST /delete_essence_msg

> Body 请求参数

```json
{
  "message_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » message_id   | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "errCode": 0,
    "errMsg": "success",
    "result": {
      "wording": "",
      "digestUin": "0",
      "digestTime": 0,
      "msg": {
        "groupCode": "0",
        "msgSeq": 0,
        "msgRandom": 0,
        "msgContent": [],
        "textSize": "0",
        "picSize": "0",
        "videoSize": "0",
        "senderUin": "0",
        "senderTime": 0,
        "addDigestUin": "0",
        "addDigestTime": 0,
        "startTime": 0,
        "latestMsgSeq": 0,
        "opType": 0
      },
      "errorCode": 0
    }
  },
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型                |
| ------ | ------------------------------------------------------- | ---- | ----------------------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [result](#schemaresult) |

## POST 退群

POST /set_group_leave

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST \_发送群公告

POST /\_send_group_notice

> Body 请求参数

```json
{
  "group_id": 0,
  "content": "string",
  "image": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » content      | body | string | 是   | 内容              |
| » image        | body | string | 否   | 图片路径          |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群头衔

POST /set_group_special_title

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "special_title": "string"
}
```

### 请求参数

| 名称            | 位置 | 类型   | 必选 | 说明              |
| --------------- | ---- | ------ | ---- | ----------------- |
| body            | body | object | 否   | none              |
| » group_id      | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_  | body | number | 否   | none              |
| »» _anonymous_  | body | string | 否   | none              |
| » user_id       | body | any    | 是   | none              |
| »» _anonymous_  | body | number | 否   | none              |
| »» _anonymous_  | body | string | 否   | none              |
| » special_title | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST \_获取群公告

POST /\_get_group_notice

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "notice_id": "63491e2f000000004f4d1e677d2b0200",
      "sender_id": 123,
      "publish_time": 1730039119,
      "message": {
        "text": "这是一条神奇的群公告",
        "image": [
          {
            "id": "aJJBbZ6BqyLiaC1kmpvIWGBBkJerEfpRBHX5Brxbaurs",
            "height": "400",
            "width": "400"
          }
        ]
      }
    }
  ],
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称            | 类型        | 必选 | 约束 | 中文名 | 说明       |
| --------------- | ----------- | ---- | ---- | ------ | ---------- |
| » status        | string      | true | none |        | none       |
| » retcode       | number      | true | none |        | none       |
| » data          | [object]    | true | none |        | none       |
| »» notice_id    | string      | true | none |        | none       |
| »» sender_id    | number      | true | none |        | 发送人账号 |
| »» publish_time | number      | true | none |        | 发送时间   |
| »» message      | [object]    | true | none |        | none       |
| »»» id          | string      | true | none |        | none       |
| »»» height      | string      | true | none |        | none       |
| »»» width       | string      | true | none |        | none       |
| » message       | string      | true | none |        | none       |
| » wording       | string      | true | none |        | none       |
| » echo          | string¦null | true | none |        | none       |

## POST 上传群文件

POST /upload_group_file

> Body 请求参数

```json
{
  "group_id": 123456,
  "file": "E:/.../logo.png",
  "name": "logo.png",
  "folder_id": "/10b1bef8-f36c-4dea-884d-eeeed225407d"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » file         | body | string | 是   | none              |
| » name         | body | string | 是   | none              |
| » folder_id    | body | string | 是   | 文件夹 ID         |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 处理加群请求

POST /set_group_add_request

> Body 请求参数

```json
{
  "flag": "string",
  "approve": true,
  "reason": "string"
}
```

### 请求参数

| 名称      | 位置 | 类型    | 必选 | 说明     |
| --------- | ---- | ------- | ---- | -------- |
| body      | body | object  | 否   | none     |
| » flag    | body | string  | 是   | 请求 id  |
| » approve | body | boolean | 是   | 是否同意 |
| » reason  | body | string  | 否   | 拒绝理由 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 删除群文件

POST /delete_group_file

> Body 请求参数

```json
{
  "group_id": "123456",
  "file_id": "000001084e61704361744f6e65426f747c4d6f64656c496446696c657c327c3739303531343031397c373433303437343033343839323937363436357c2f64323162343062362d366133622d343438632d623737332d6166663031313530323532397c2f64323162343062362d366133622d343438632d623737332d616666303131353032353239"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » file_id      | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string",
    "transGroupFileResult": {
      "result": {
        "retCode": 0,
        "retMsg": "string",
        "clientWording": "string"
      },
      "successFileIdList": ["string"],
      "failFileIdList": ["string"]
    }
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                    | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ----------------------- | ----------- | ---- | ---- | ------ | ---- |
| » status                | string      | true | none |        | none |
| » retcode               | number      | true | none |        | none |
| » data                  | object      | true | none |        | none |
| »» result               | number      | true | none |        | none |
| »» errMsg               | string      | true | none |        | none |
| »» transGroupFileResult | object      | true | none |        | none |
| »»» result              | object      | true | none |        | none |
| »»»» retCode            | number      | true | none |        | none |
| »»»» retMsg             | string      | true | none |        | none |
| »»»» clientWording      | string      | true | none |        | none |
| »»» successFileIdList   | [string]    | true | none |        | none |
| »»» failFileIdList      | [string]    | true | none |        | none |
| » message               | string      | true | none |        | none |
| » wording               | string      | true | none |        | none |
| » echo                  | string¦null | true | none |        | none |

## POST 创建群文件文件夹

POST /create_group_file_folder

> Body 请求参数

```json
{
  "group_id": 0,
  "folder_name": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » folder_name  | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": {
      "retCode": 0,
      "retMsg": "string",
      "clientWording": "string"
    },
    "groupItem": {
      "peerId": "string",
      "type": "string",
      "folderInfo": {
        "folderId": "string",
        "parentFolderId": "string",
        "folderName": "string",
        "createTime": 0,
        "modifyTime": 0,
        "createUin": "string",
        "creatorName": "string",
        "totalFileCount": "string",
        "modifyUin": "string",
        "modifyName": "string",
        "usedSpace": "string"
      }
    }
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                | 类型        | 必选 | 约束 | 中文名 | 说明       |
| ------------------- | ----------- | ---- | ---- | ------ | ---------- |
| » status            | string      | true | none |        | none       |
| » retcode           | number      | true | none |        | none       |
| » data              | object      | true | none |        | none       |
| »» result           | object      | true | none |        | none       |
| »»» retCode         | number      | true | none |        | none       |
| »»» retMsg          | string      | true | none |        | none       |
| »»» clientWording   | string      | true | none |        | none       |
| »» groupItem        | object      | true | none |        | none       |
| »»» peerId          | string      | true | none |        | none       |
| »»» type            | string      | true | none |        | none       |
| »»» folderInfo      | object      | true | none |        | 文件夹信息 |
| »»»» folderId       | string      | true | none |        | none       |
| »»»» parentFolderId | string      | true | none |        | none       |
| »»»» folderName     | string      | true | none |        | none       |
| »»»» createTime     | number      | true | none |        | none       |
| »»»» modifyTime     | number      | true | none |        | none       |
| »»»» createUin      | string      | true | none |        | none       |
| »»»» creatorName    | string      | true | none |        | none       |
| »»»» totalFileCount | string      | true | none |        | none       |
| »»»» modifyUin      | string      | true | none |        | none       |
| »»»» modifyName     | string      | true | none |        | none       |
| »»»» usedSpace      | string      | true | none |        | none       |
| » message           | string      | true | none |        | none       |
| » wording           | string      | true | none |        | none       |
| » echo              | string¦null | true | none |        | none       |

## POST 删除群文件夹

POST /delete_group_folder

> Body 请求参数

```json
{
  "group_id": 123456,
  "folder_id": "/10b1bef8-f36c-4dea-884d-eeeed225407d"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » folder_id    | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "retCode": 0,
    "retMsg": "string",
    "clientWording": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称             | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ---------------- | ----------- | ---- | ---- | ------ | ---- |
| » status         | string      | true | none |        | none |
| » retcode        | number      | true | none |        | none |
| » data           | object      | true | none |        | none |
| »» retCode       | number      | true | none |        | none |
| »» retMsg        | string      | true | none |        | none |
| »» clientWording | string      | true | none |        | none |
| » message        | string      | true | none |        | none |
| » wording        | string      | true | none |        | none |
| » echo           | string¦null | true | none |        | none |

## POST 获取群文件系统信息

POST /get_group_file_system_info

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file_count": 0,
    "limit_count": 0,
    "used_space": 0,
    "total_space": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称           | 类型        | 必选 | 约束 | 中文名 | 说明       |
| -------------- | ----------- | ---- | ---- | ------ | ---------- |
| » status       | string      | true | none |        | none       |
| » retcode      | number      | true | none |        | none       |
| » data         | object      | true | none |        | none       |
| »» file_count  | number      | true | none |        | 文件总数   |
| »» limit_count | number      | true | none |        | 文件上限   |
| »» used_space  | number      | true | none |        | 已使用空间 |
| »» total_space | number      | true | none |        | 空间上限   |
| » message      | string      | true | none |        | none       |
| » wording      | string      | true | none |        | none       |
| » echo         | string¦null | true | none |        | none       |

## POST 获取群信息

POST /get_group_info

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群根目录文件列表

POST /get_group_root_files

> Body 请求参数

```json
{
  "group_id": "518662028"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "files": [
      {
        "group_id": 0,
        "file_id": "string",
        "file_name": "string",
        "busid": 0,
        "size": 0,
        "upload_time": 0,
        "dead_time": 0,
        "modify_time": 0,
        "download_times": 0,
        "uploader": 0,
        "uploader_name": "string"
      }
    ],
    "folders": [
      {
        "group_id": 0,
        "folder_id": "string",
        "folder": "string",
        "folder_name": "string",
        "create_time": "string",
        "creator": "string",
        "creator_name": "string",
        "total_file_count": "string"
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                 | 类型        | 必选 | 约束 | 中文名 | 说明       |
| -------------------- | ----------- | ---- | ---- | ------ | ---------- |
| » status             | string      | true | none |        | none       |
| » retcode            | number      | true | none |        | none       |
| » data               | object      | true | none |        | none       |
| »» files             | [object]    | true | none |        | 文件列表   |
| »»» group_id         | number      | true | none |        | none       |
| »»» file_id          | string      | true | none |        | none       |
| »»» file_name        | string      | true | none |        | none       |
| »»» busid            | number      | true | none |        | none       |
| »»» size             | number      | true | none |        | none       |
| »»» upload_time      | number      | true | none |        | none       |
| »»» dead_time        | number      | true | none |        | none       |
| »»» modify_time      | number      | true | none |        | none       |
| »»» download_times   | number      | true | none |        | none       |
| »»» uploader         | number      | true | none |        | none       |
| »»» uploader_name    | string      | true | none |        | none       |
| »» folders           | [object]    | true | none |        | 文件夹列表 |
| »»» group_id         | number      | true | none |        | none       |
| »»» folder_id        | string      | true | none |        | none       |
| »»» folder           | string      | true | none |        | none       |
| »»» folder_name      | string      | true | none |        | 文件夹名称 |
| »»» create_time      | string      | true | none |        | 创建时间   |
| »»» creator          | string      | true | none |        | 创建人账号 |
| »»» creator_name     | string      | true | none |        | 创建人昵称 |
| »»» total_file_count | string      | true | none |        | 文件数量   |
| » message            | string      | true | none |        | none       |
| » wording            | string      | true | none |        | none       |
| » echo               | string¦null | true | none |        | none       |

## POST 获取群列表

POST /get_group_list

> Body 请求参数

```json
{
  "no_cache": false
}
```

### 请求参数

| 名称       | 位置 | 类型    | 必选 | 说明   |
| ---------- | ---- | ------- | ---- | ------ |
| body       | body | object  | 否   | none   |
| » no_cache | body | boolean | 是   | 不缓存 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [{}],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [object]    | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群子目录文件列表

POST /get_group_files_by_folder

> Body 请求参数

```json
{
  "group_id": 123456,
  "folder_id": "/10b1bef8-f36c-4dea-884d-eeeed225407d",
  "file_count": 17
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明                 |
| -------------- | ---- | ------ | ---- | -------------------- |
| body           | body | object | 否   | none                 |
| » group_id     | body | any    | 是   | 和 user_id 二选一    |
| »» _anonymous_ | body | number | 否   | none                 |
| »» _anonymous_ | body | string | 否   | none                 |
| » folder_id    | body | string | 是   | none                 |
| » file_count   | body | number | 是   | 一次性获取的文件数量 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "files": [
      {
        "group_id": 0,
        "file_id": "string",
        "file_name": "string",
        "busid": 0,
        "size": 0,
        "upload_time": 0,
        "dead_time": 0,
        "modify_time": 0,
        "download_times": 0,
        "uploader": 0,
        "uploader_name": "string"
      }
    ],
    "folders": [
      {
        "group_id": 0,
        "folder_id": "string",
        "folder": "string",
        "folder_name": "string",
        "create_time": "string",
        "creator": "string",
        "creator_name": "string",
        "total_file_count": "string"
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                 | 类型        | 必选  | 约束 | 中文名 | 说明       |
| -------------------- | ----------- | ----- | ---- | ------ | ---------- |
| » status             | string      | true  | none |        | none       |
| » retcode            | number      | true  | none |        | none       |
| » data               | object      | true  | none |        | none       |
| »» files             | [object]    | true  | none |        | 文件列表   |
| »»» group_id         | number      | true  | none |        | none       |
| »»» file_id          | string      | true  | none |        | none       |
| »»» file_name        | string      | true  | none |        | none       |
| »»» busid            | number      | true  | none |        | none       |
| »»» size             | number      | true  | none |        | none       |
| »»» upload_time      | number      | true  | none |        | none       |
| »»» dead_time        | number      | true  | none |        | none       |
| »»» modify_time      | number      | true  | none |        | none       |
| »»» download_times   | number      | true  | none |        | none       |
| »»» uploader         | number      | true  | none |        | none       |
| »»» uploader_name    | string      | true  | none |        | none       |
| »» folders           | [object]    | false | none |        | 文件夹列表 |
| »»» group_id         | number      | true  | none |        | none       |
| »»» folder_id        | string      | true  | none |        | none       |
| »»» folder           | string      | true  | none |        | none       |
| »»» folder_name      | string      | true  | none |        | 文件夹名称 |
| »»» create_time      | string      | true  | none |        | 创建时间   |
| »»» creator          | string      | true  | none |        | 创建人账号 |
| »»» creator_name     | string      | true  | none |        | 创建人昵称 |
| »»» total_file_count | string      | true  | none |        | 文件数量   |
| » message            | string      | true  | none |        | none       |
| » wording            | string      | true  | none |        | none       |
| » echo               | string¦null | true  | none |        | none       |

## POST 获取群成员信息

POST /get_group_member_info

> Body 请求参数

```json
{
  "group_id": 0,
  "user_id": 0,
  "no_cache": true
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明              |
| -------------- | ---- | ------- | ---- | ----------------- |
| body           | body | object  | 否   | none              |
| » group_id     | body | any     | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » user_id      | body | any     | 是   | none              |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » no_cache     | body | boolean | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群文件资源链接

POST /get_group_file_url

> Body 请求参数

```json
{
  "group_id": "123456",
  "file_id": "000001084e61704361744f6e65426f747c4d6f64656c496446696c657c327c3739303531343031397c373433303436393331303833393135373435357c2f32646431303634372d623364662d346331642d396537302d6630613138303138653934307c2f32646431303634372d623364662d346331642d396537302d663061313830313865393430"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » file_id      | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "url": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» url    | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群成员列表

POST /get_group_member_list

> Body 请求参数

```json
{
  "group_id": 0,
  "no_cache": false
}
```

### 请求参数

| 名称           | 位置 | 类型    | 必选 | 说明              |
| -------------- | ---- | ------- | ---- | ----------------- |
| body           | body | object  | 否   | none              |
| » group_id     | body | any     | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number  | 否   | none              |
| »» _anonymous_ | body | string  | 否   | none              |
| » no_cache     | body | boolean | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [{}],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [object]    | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取群荣誉

POST /get_group_honor_info

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "group_id": "string",
    "current_talkative": {
      "user_id": 0,
      "avatar": "string",
      "nickname": "string",
      "day_count": 0,
      "description": "string"
    },
    "talkative_list": [
      {
        "user_id": 0,
        "avatar": "string",
        "nickname": "string",
        "day_count": 0,
        "description": "string"
      }
    ],
    "performer_list": [
      {
        "user_id": 0,
        "avatar": "string",
        "nickname": "string",
        "description": "string"
      }
    ],
    "legend_list": ["string"],
    "emotion_list": ["string"],
    "strong_newbie_list": ["string"]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                  | 类型                          | 必选  | 约束 | 中文名 | 说明         |
| --------------------- | ----------------------------- | ----- | ---- | ------ | ------------ |
| » status              | string                        | true  | none |        | none         |
| » retcode             | number                        | true  | none |        | none         |
| » data                | object                        | true  | none |        | none         |
| »» group_id           | string                        | true  | none |        | none         |
| »» current_talkative  | [龙王信息](#schema龙王信息)   | true  | none |        | 当前龙王     |
| »»» user_id           | number                        | false | none |        | none         |
| »»» avatar            | string                        | false | none |        | 头像         |
| »»» nickname          | string                        | false | none |        | none         |
| »»» day_count         | number                        | false | none |        | 连续天数     |
| »»» description       | string                        | false | none |        | 说明         |
| »» talkative_list     | [[龙王信息](#schema龙王信息)] | true  | none |        | 历史龙王列表 |
| »»» user_id           | number                        | false | none |        | none         |
| »»» avatar            | string                        | false | none |        | 头像         |
| »»» nickname          | string                        | false | none |        | none         |
| »»» day_count         | number                        | false | none |        | 连续天数     |
| »»» description       | string                        | false | none |        | 说明         |
| »» performer_list     | [object]                      | true  | none |        | 群聊之火     |
| »»» user_id           | number                        | false | none |        | none         |
| »»» avatar            | string                        | false | none |        | 头像         |
| »»» nickname          | string                        | false | none |        | none         |
| »»» description       | string                        | false | none |        | 说明         |
| »» legend_list        | [string]                      | true  | none |        | 群聊炽焰     |
| »» emotion_list       | [string]                      | true  | none |        | 快乐之源     |
| »» strong_newbie_list | [string]                      | true  | none |        | 冒尖小春笋   |
| » message             | string                        | true  | none |        | none         |
| » wording             | string                        | true  | none |        | none         |
| » echo                | string¦null                   | true  | none |        | none         |

## POST 获取群信息 ex

POST /get_group_info_ex

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "groupCode": "790514019",
    "resultCode": 0,
    "extInfo": {
      "groupInfoExtSeq": 1,
      "reserve": 0,
      "luckyWordId": "0",
      "lightCharNum": 0,
      "luckyWord": "",
      "starId": 0,
      "essentialMsgSwitch": 0,
      "todoSeq": 0,
      "blacklistExpireTime": 0,
      "isLimitGroupRtc": 0,
      "companyId": 0,
      "hasGroupCustomPortrait": 1,
      "bindGuildId": "0",
      "groupOwnerId": {
        "memberUin": "1129317309",
        "memberUid": "u_4_QA-QaFryh-Ocgsv4_8EQ",
        "memberQid": ""
      },
      "essentialMsgPrivilege": 0,
      "msgEventSeq": "0",
      "inviteRobotSwitch": 0,
      "gangUpId": "0",
      "qqMusicMedalSwitch": 0,
      "showPlayTogetherSwitch": 0,
      "groupFlagPro1": "0",
      "groupBindGuildIds": {
        "guildIds": []
      },
      "viewedMsgDisappearTime": "0",
      "groupExtFlameData": {
        "switchState": 0,
        "state": 0,
        "dayNums": [],
        "version": 0,
        "updateTime": "0",
        "isDisplayDayNum": false
      },
      "groupBindGuildSwitch": 0,
      "groupAioBindGuildId": "0",
      "groupExcludeGuildIds": {
        "guildIds": []
      },
      "fullGroupExpansionSwitch": 0,
      "fullGroupExpansionSeq": "0",
      "inviteRobotMemberSwitch": 0,
      "inviteRobotMemberExamine": 0,
      "groupSquareSwitch": 0
    }
  },
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                         | 类型     | 必选 | 约束 | 中文名 | 说明 |
| ---------------------------- | -------- | ---- | ---- | ------ | ---- |
| » status                     | string   | true | none |        | none |
| » retcode                    | number   | true | none |        | none |
| » data                       | object   | true | none |        | none |
| »» groupCode                 | string   | true | none |        | none |
| »» resultCode                | number   | true | none |        | none |
| »» extInfo                   | object   | true | none |        | none |
| »»» groupInfoExtSeq          | number   | true | none |        | none |
| »»» reserve                  | number   | true | none |        | none |
| »»» luckyWordId              | string   | true | none |        | none |
| »»» lightCharNum             | number   | true | none |        | none |
| »»» luckyWord                | string   | true | none |        | none |
| »»» starId                   | number   | true | none |        | none |
| »»» essentialMsgSwitch       | number   | true | none |        | none |
| »»» todoSeq                  | number   | true | none |        | none |
| »»» blacklistExpireTime      | number   | true | none |        | none |
| »»» isLimitGroupRtc          | number   | true | none |        | none |
| »»» companyId                | number   | true | none |        | none |
| »»» hasGroupCustomPortrait   | number   | true | none |        | none |
| »»» bindGuildId              | string   | true | none |        | none |
| »»» groupOwnerId             | object   | true | none |        | none |
| »»»» memberUin               | string   | true | none |        | none |
| »»»» memberUid               | string   | true | none |        | none |
| »»»» memberQid               | string   | true | none |        | none |
| »»» essentialMsgPrivilege    | number   | true | none |        | none |
| »»» msgEventSeq              | string   | true | none |        | none |
| »»» inviteRobotSwitch        | number   | true | none |        | none |
| »»» gangUpId                 | string   | true | none |        | none |
| »»» qqMusicMedalSwitch       | number   | true | none |        | none |
| »»» showPlayTogetherSwitch   | number   | true | none |        | none |
| »»» groupFlagPro1            | string   | true | none |        | none |
| »»» groupBindGuildIds        | object   | true | none |        | none |
| »»»» guildIds                | [string] | true | none |        | none |
| »»» viewedMsgDisappearTime   | string   | true | none |        | none |
| »»» groupExtFlameData        | object   | true | none |        | none |
| »»»» switchState             | integer  | true | none |        | none |
| »»»» state                   | integer  | true | none |        | none |
| »»»» dayNums                 | [string] | true | none |        | none |
| »»»» version                 | integer  | true | none |        | none |
| »»»» updateTime              | string   | true | none |        | none |
| »»»» isDisplayDayNum         | boolean  | true | none |        | none |
| »»» groupBindGuildSwitch     | number   | true | none |        | none |
| »»» groupAioBindGuildId      | string   | true | none |        | none |
| »»» groupExcludeGuildIds     | object   | true | none |        | none |
| »»»» guildIds                | [string] | true | none |        | none |
| »»» fullGroupExpansionSwitch | number   | true | none |        | none |
| »»» fullGroupExpansionSeq    | string   | true | none |        | none |
| »»» inviteRobotMemberSwitch  | number   | true | none |        | none |
| »»» inviteRobotMemberExamine | number   | true | none |        | none |
| »»» groupSquareSwitch        | number   | true | none |        | none |
| » message                    | string   | true | none |        | none |
| » wording                    | string   | true | none |        | none |
| » echo                       | null     | true | none |        | none |

## POST 获取群 @全体成员 剩余次数

POST /get_group_at_all_remain

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "can_at_all": true,
    "remain_at_all_count_for_group": 0,
    "remain_at_all_count_for_uin": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                             | 类型        | 必选 | 约束 | 中文名 | 说明 |
| -------------------------------- | ----------- | ---- | ---- | ------ | ---- |
| » status                         | string      | true | none |        | none |
| » retcode                        | number      | true | none |        | none |
| » data                           | object      | true | none |        | none |
| »» can_at_all                    | boolean     | true | none |        | none |
| »» remain_at_all_count_for_group | number      | true | none |        | none |
| »» remain_at_all_count_for_uin   | number      | true | none |        | none |
| » message                        | string      | true | none |        | none |
| » wording                        | string      | true | none |        | none |
| » echo                           | string¦null | true | none |        | none |

## POST 获取群过滤系统消息

POST /get_group_ignored_notifies

> Body 请求参数

```json
{
  "group_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "join_requests": [
      {
        "request_id": "string",
        "requester_uin": "string",
        "requester_nick": "string",
        "group_id": "string",
        "group_name": "string",
        "checked": true,
        "actor": "string"
      }
    ]
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称               | 类型     | 必选 | 约束 | 中文名 | 说明 |
| ------------------ | -------- | ---- | ---- | ------ | ---- |
| » status           | string   | true | none |        | none |
| » retcode          | number   | true | none |        | none |
| » data             | object   | true | none |        | none |
| »» join_requests   | [object] | true | none |        | none |
| »»» request_id     | string   | true | none |        | none |
| »»» requester_uin  | string   | true | none |        | none |
| »»» requester_nick | string   | true | none |        | none |
| »»» group_id       | string   | true | none |        | none |
| »»» group_name     | string   | true | none |        | none |
| »»» checked        | boolean  | true | none |        | none |
| »»» actor          | any      | true | none |        | none |

_oneOf_

| 名称             | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | string | false | none |        | none |

_xor_

| 名称             | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ---------------- | ------ | ----- | ---- | ------ | ---- |
| »»»» _anonymous_ | number | false | none |        | none |

_continued_

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 设置群打卡

POST /set_group_sign

> Body 请求参数

```json
{
  "group_id": 123456
}
```

### 请求参数

| 名称       | 位置 | 类型   | 必选 | 说明 |
| ---------- | ---- | ------ | ---- | ---- |
| body       | body | object | 否   | none |
| » group_id | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## POST 发送群打卡

POST /send_group_sign

> Body 请求参数

```json
{
  "group_id": 123456
}
```

### 请求参数

| 名称       | 位置 | 类型   | 必选 | 说明 |
| ---------- | ---- | ------ | ---- | ---- |
| body       | body | object | 否   | none |
| » group_id | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## POST 获取 AI 语音人物

POST /get_ai_characters

> Body 请求参数

```json
{
  "group_id": 0,
  "chat_type": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » chat_type    | body | any    | 是   | none              |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "type": "string",
      "characters": [
        {
          "character_id": "string",
          "character_name": "string",
          "preview_url": "string"
        }
      ]
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称               | 类型        | 必选 | 约束 | 中文名 | 说明     |
| ------------------ | ----------- | ---- | ---- | ------ | -------- |
| » status           | string      | true | none |        | none     |
| » retcode          | number      | true | none |        | none     |
| » data             | [object]    | true | none |        | none     |
| »» type            | string      | true | none |        | 类型     |
| »» characters      | [object]    | true | none |        | 人物列表 |
| »»» character_id   | string      | true | none |        | 人物 ID  |
| »»» character_name | string      | true | none |        | 人物名字 |
| »»» preview_url    | string      | true | none |        | 试听网址 |
| » message          | string      | true | none |        | none     |
| » wording          | string      | true | none |        | none     |
| » echo             | string¦null | true | none |        | none     |

## POST 发送群 AI 语音

POST /send_group_ai_record

> Body 请求参数

```json
{
  "group_id": 0,
  "character": "string",
  "text": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » character    | body | string | 是   | character_id      |
| » text         | body | string | 是   | 文本              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_id": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------------- | ----------- | ---- | ---- | ------ | ---- |
| » status      | string      | true | none |        | none |
| » retcode     | number      | true | none |        | none |
| » data        | object      | true | none |        | none |
| »» message_id | string      | true | none |        | none |
| » message     | string      | true | none |        | none |
| » wording     | string      | true | none |        | none |
| » echo        | string¦null | true | none |        | none |

## POST 获取 AI 语音

POST /get_ai_record

> Body 请求参数

```json
{
  "group_id": 0,
  "character": "string",
  "text": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » character    | body | string | 是   | character_id      |
| » text         | body | string | 是   | 文本              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": "string",
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | string      | true | none |        | 链接 |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

# 系统

## POST 获取 clientkey

POST /get_clientkey

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "clientkey": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称         | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------------ | ----------- | ---- | ---- | ------ | ---- |
| » status     | string      | true | none |        | none |
| » retcode    | number      | true | none |        | none |
| » data       | object      | true | none |        | none |
| »» clientkey | string      | true | none |        | none |
| » message    | string      | true | none |        | none |
| » wording    | string      | true | none |        | none |
| » echo       | string¦null | true | none |        | none |

## POST 获取当前账号在线客户端列表

POST /get_online_clients

> Body 请求参数

```json
{
  "no_cache": false
}
```

### 请求参数

| 名称       | 位置 | 类型    | 必选 | 说明 |
| ---------- | ---- | ------- | ---- | ---- |
| body       | body | object  | 否   | none |
| » no_cache | body | boolean | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "clients": {}
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称       | 类型        | 必选  | 约束 | 中文名 | 说明 |
| ---------- | ----------- | ----- | ---- | ------ | ---- |
| » status   | string      | true  | none |        | none |
| » retcode  | number      | true  | none |        | none |
| » data     | object      | true  | none |        | none |
| »» clients | object      | false | none |        | none |
| » message  | string      | true  | none |        | none |
| » wording  | string      | true  | none |        | none |
| » echo     | string¦null | true  | none |        | none |

## POST 获取机器人账号范围

POST /get_robot_uin_range

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "minUin": "3328144510",
      "maxUin": "3328144510"
    },
    {
      "minUin": "2854196301",
      "maxUin": "2854216399"
    },
    {
      "minUin": "66600000",
      "maxUin": "66600000"
    },
    {
      "minUin": "3889000000",
      "maxUin": "3889999999"
    },
    {
      "minUin": "4010000000",
      "maxUin": "4019999999"
    }
  ],
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [object]    | true | none |        | none |
| »» minUin | string      | true | none |        | none |
| »» maxUin | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST OCR 图片识别

POST /ocr_image

> Body 请求参数

```json
"{\r\n    \"image\": \"https://greasyfork.org/vite/assets/blacklogo96-CxYTSM_T.png\"\r\n    // 本地路径\r\n    //\"image\": \"file://D:/a.jpg\"\r\n}"
```

### 请求参数

| 名称    | 位置 | 类型   | 必选 | 说明 |
| ------- | ---- | ------ | ---- | ---- |
| body    | body | object | 否   | none |
| » image | body | string | 是   | none |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "text": "nU",
      "pt1": {
        "x": "25.930853",
        "y": "1.711797"
      },
      "pt2": {
        "x": "72.461205",
        "y": "2.745806"
      },
      "pt3": {
        "x": "72.193184",
        "y": "14.806514"
      },
      "pt4": {
        "x": "25.662836",
        "y": "13.772506"
      },
      "charBox": [
        {
          "charText": "nU",
          "charBox": {
            "pt1": {
              "x": "41.186707",
              "y": "2.050816"
            },
            "pt2": {
              "x": "56.442558",
              "y": "2.389835"
            },
            "pt3": {
              "x": "56.182915",
              "y": "14.073647"
            },
            "pt4": {
              "x": "40.927063",
              "y": "13.734628"
            }
          }
        }
      ],
      "score": ""
    },
    {
      "text": "yion in",
      "pt1": {
        "x": "40.310081",
        "y": "19.155090"
      },
      "pt2": {
        "x": "92.413017",
        "y": "17.004047"
      },
      "pt3": {
        "x": "93.224297",
        "y": "36.654957"
      },
      "pt4": {
        "x": "41.121365",
        "y": "38.806000"
      },
      "charBox": [
        {
          "charText": "yion",
          "charBox": {
            "pt1": {
              "x": "40.310081",
              "y": "19.155090"
            },
            "pt2": {
              "x": "66.660988",
              "y": "18.067207"
            },
            "pt3": {
              "x": "67.446922",
              "y": "37.104027"
            },
            "pt4": {
              "x": "41.096012",
              "y": "38.191910"
            }
          }
        },
        {
          "charText": " ",
          "charBox": {
            "pt1": {
              "x": "66.660988",
              "y": "18.067207"
            },
            "pt2": {
              "x": "73.847603",
              "y": "17.770512"
            },
            "pt3": {
              "x": "74.633530",
              "y": "36.807331"
            },
            "pt4": {
              "x": "67.446922",
              "y": "37.104027"
            }
          }
        },
        {
          "charText": "in",
          "charBox": {
            "pt1": {
              "x": "73.847603",
              "y": "17.770512"
            },
            "pt2": {
              "x": "85.825287",
              "y": "17.276018"
            },
            "pt3": {
              "x": "86.611214",
              "y": "36.312836"
            },
            "pt4": {
              "x": "74.633530",
              "y": "36.807331"
            }
          }
        }
      ],
      "score": ""
    },
    {
      "text": "mlHttp.",
      "pt1": {
        "x": "6.956338",
        "y": "61.610126"
      },
      "pt2": {
        "x": "72.331848",
        "y": "65.844292"
      },
      "pt3": {
        "x": "71.104248",
        "y": "84.798470"
      },
      "pt4": {
        "x": "5.728738",
        "y": "80.564301"
      },
      "charBox": [
        {
          "charText": "mlHttp",
          "charBox": {
            "pt1": {
              "x": "9.230268",
              "y": "61.757401"
            },
            "pt2": {
              "x": "61.530674",
              "y": "65.144737"
            },
            "pt3": {
              "x": "60.341438",
              "y": "83.506592"
            },
            "pt4": {
              "x": "8.041031",
              "y": "80.119255"
            }
          }
        },
        {
          "charText": ".",
          "charBox": {
            "pt1": {
              "x": "63.804607",
              "y": "65.292007"
            },
            "pt2": {
              "x": "70.626396",
              "y": "65.733833"
            },
            "pt3": {
              "x": "69.437164",
              "y": "84.095695"
            },
            "pt4": {
              "x": "62.615368",
              "y": "83.653870"
            }
          }
        }
      ],
      "score": ""
    }
  ],
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称         | 类型        | 必选 | 约束 | 中文名 | 说明         |
| ------------ | ----------- | ---- | ---- | ------ | ------------ |
| » status     | string      | true | none |        | none         |
| » retcode    | number      | true | none |        | none         |
| » data       | [object]    | true | none |        | none         |
| »» text      | string      | true | none |        | 该行文本总和 |
| »» pt1       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» pt2       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» pt3       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» pt4       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» charBox   | [object]    | true | none |        | 拆分         |
| »»» charText | string      | true | none |        | none         |
| »»» charBox  | object      | true | none |        | none         |
| »»»» pt1     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »»»» pt2     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »»»» pt3     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »»»» pt4     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »» score     | string      | true | none |        | none         |
| » message    | string      | true | none |        | none         |
| » wording    | string      | true | none |        | none         |
| » echo       | string¦null | true | none |        | none         |

## POST .OCR 图片识别

POST /.ocr_image

> Body 请求参数

```json
"{\r\n    \"image\": \"https://greasyfork.org/vite/assets/blacklogo96-CxYTSM_T.png\"\r\n    // 本地路径\r\n    //\"image\": \"file://D:/a.jpg\"\r\n}"
```

### 请求参数

| 名称    | 位置 | 类型   | 必选 | 说明 |
| ------- | ---- | ------ | ---- | ---- |
| body    | body | object | 否   | none |
| » image | body | string | 是   | none |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "text": "nU",
      "pt1": {
        "x": "25.930853",
        "y": "1.711797"
      },
      "pt2": {
        "x": "72.461205",
        "y": "2.745806"
      },
      "pt3": {
        "x": "72.193184",
        "y": "14.806514"
      },
      "pt4": {
        "x": "25.662836",
        "y": "13.772506"
      },
      "charBox": [
        {
          "charText": "nU",
          "charBox": {
            "pt1": {
              "x": "41.186707",
              "y": "2.050816"
            },
            "pt2": {
              "x": "56.442558",
              "y": "2.389835"
            },
            "pt3": {
              "x": "56.182915",
              "y": "14.073647"
            },
            "pt4": {
              "x": "40.927063",
              "y": "13.734628"
            }
          }
        }
      ],
      "score": ""
    },
    {
      "text": "yion in",
      "pt1": {
        "x": "40.310081",
        "y": "19.155090"
      },
      "pt2": {
        "x": "92.413017",
        "y": "17.004047"
      },
      "pt3": {
        "x": "93.224297",
        "y": "36.654957"
      },
      "pt4": {
        "x": "41.121365",
        "y": "38.806000"
      },
      "charBox": [
        {
          "charText": "yion",
          "charBox": {
            "pt1": {
              "x": "40.310081",
              "y": "19.155090"
            },
            "pt2": {
              "x": "66.660988",
              "y": "18.067207"
            },
            "pt3": {
              "x": "67.446922",
              "y": "37.104027"
            },
            "pt4": {
              "x": "41.096012",
              "y": "38.191910"
            }
          }
        },
        {
          "charText": " ",
          "charBox": {
            "pt1": {
              "x": "66.660988",
              "y": "18.067207"
            },
            "pt2": {
              "x": "73.847603",
              "y": "17.770512"
            },
            "pt3": {
              "x": "74.633530",
              "y": "36.807331"
            },
            "pt4": {
              "x": "67.446922",
              "y": "37.104027"
            }
          }
        },
        {
          "charText": "in",
          "charBox": {
            "pt1": {
              "x": "73.847603",
              "y": "17.770512"
            },
            "pt2": {
              "x": "85.825287",
              "y": "17.276018"
            },
            "pt3": {
              "x": "86.611214",
              "y": "36.312836"
            },
            "pt4": {
              "x": "74.633530",
              "y": "36.807331"
            }
          }
        }
      ],
      "score": ""
    },
    {
      "text": "mlHttp.",
      "pt1": {
        "x": "6.956338",
        "y": "61.610126"
      },
      "pt2": {
        "x": "72.331848",
        "y": "65.844292"
      },
      "pt3": {
        "x": "71.104248",
        "y": "84.798470"
      },
      "pt4": {
        "x": "5.728738",
        "y": "80.564301"
      },
      "charBox": [
        {
          "charText": "mlHttp",
          "charBox": {
            "pt1": {
              "x": "9.230268",
              "y": "61.757401"
            },
            "pt2": {
              "x": "61.530674",
              "y": "65.144737"
            },
            "pt3": {
              "x": "60.341438",
              "y": "83.506592"
            },
            "pt4": {
              "x": "8.041031",
              "y": "80.119255"
            }
          }
        },
        {
          "charText": ".",
          "charBox": {
            "pt1": {
              "x": "63.804607",
              "y": "65.292007"
            },
            "pt2": {
              "x": "70.626396",
              "y": "65.733833"
            },
            "pt3": {
              "x": "69.437164",
              "y": "84.095695"
            },
            "pt4": {
              "x": "62.615368",
              "y": "83.653870"
            }
          }
        }
      ],
      "score": ""
    }
  ],
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称         | 类型        | 必选 | 约束 | 中文名 | 说明         |
| ------------ | ----------- | ---- | ---- | ------ | ------------ |
| » status     | string      | true | none |        | none         |
| » retcode    | number      | true | none |        | none         |
| » data       | [object]    | true | none |        | none         |
| »» text      | string      | true | none |        | 该行文本总和 |
| »» pt1       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» pt2       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» pt3       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» pt4       | object      | true | none |        | 顶点坐标     |
| »»» x        | string      | true | none |        | none         |
| »»» y        | string      | true | none |        | none         |
| »» charBox   | [object]    | true | none |        | 拆分         |
| »»» charText | string      | true | none |        | none         |
| »»» charBox  | object      | true | none |        | none         |
| »»»» pt1     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »»»» pt2     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »»»» pt3     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »»»» pt4     | object      | true | none |        | 顶点坐标     |
| »»»»» x      | string      | true | none |        | none         |
| »»»»» y      | string      | true | none |        | none         |
| »» score     | string      | true | none |        | none         |
| » message    | string      | true | none |        | none         |
| » wording    | string      | true | none |        | none         |
| » echo       | string¦null | true | none |        | none         |

## POST 英译中

POST /translate_en2zh

> Body 请求参数

```json
{
  "words": ["word", "message", "group"]
}
```

### 请求参数

| 名称    | 位置 | 类型     | 必选 | 说明     |
| ------- | ---- | -------- | ---- | -------- |
| body    | body | object   | 否   | none     |
| » words | body | [string] | 是   | 英文数组 |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": ["单词", "讯息", "群组"],
  "message": "",
  "wording": "",
  "echo": null
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [string]    | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取登录号信息

POST /get_login_info

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "user_id": 0,
    "nickname": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称        | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ----------- | ----------- | ---- | ---- | ------ | ---- |
| » status    | string      | true | none |        | none |
| » retcode   | number      | true | none |        | none |
| » data      | object      | true | none |        | none |
| »» user_id  | number      | true | none |        | none |
| »» nickname | string      | true | none |        | none |
| » message   | string      | true | none |        | none |
| » wording   | string      | true | none |        | none |
| » echo      | string¦null | true | none |        | none |

## POST 设置输入状态

POST /set_input_status

## 状态列表

### 对方正在说话...

```json5
{ event_type: 0 }
```

### 对方正在输入...

```json5
{ event_type: 1 }
```

> Body 请求参数

```json
{
  "eventType": 0,
  "user_id": 0
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » eventType    | body | number | 是   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 下载文件到缓存目录

POST /download_file

> Body 请求参数

```json
{
  "url": "http://i0.hdslb.com/bfs/archive/c8fd97a40bf79f03e7b76cbc87236f612caef7b2.png",
  "thread_count": 5,
  "name": "bilibili.png"
}
```

### 请求参数

| 名称           | 位置 | 类型     | 必选 | 说明           |
| -------------- | ---- | -------- | ---- | -------------- |
| body           | body | object   | 否   | none           |
| » base64       | body | string   | 否   | 和 url 二选一  |
| » url          | body | string   | 否   | 下载地址       |
| » thread_count | body | number   | 是   | 下载线程数     |
| » headers      | body | any      | 是   | 请求头         |
| »» _anonymous_ | body | string   | 否   | none           |
| »» _anonymous_ | body | [string] | 否   | none           |
| » name         | body | string   | 否   | 自定义文件名称 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "file": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明         |
| --------- | ----------- | ---- | ---- | ------ | ------------ |
| » status  | string      | true | none |        | none         |
| » retcode | number      | true | none |        | none         |
| » data    | object      | true | none |        | none         |
| »» file   | string      | true | none |        | 下载后的路径 |
| » message | string      | true | none |        | none         |
| » wording | string      | true | none |        | none         |
| » echo    | string¦null | true | none |        | none         |

## POST 获取 cookies

POST /get_cookies

> Body 请求参数

```json
{
  "domain": "string"
}
```

### 请求参数

| 名称     | 位置 | 类型   | 必选 | 说明 |
| -------- | ---- | ------ | ---- | ---- |
| body     | body | object | 否   | none |
| » domain | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "cookies": "string",
    "bkn": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称       | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ---------- | ----------- | ---- | ---- | ------ | ---- |
| » status   | string      | true | none |        | none |
| » retcode  | number      | true | none |        | none |
| » data     | object      | true | none |        | none |
| »» cookies | string      | true | none |        | none |
| »» bkn     | string      | true | none |        | none |
| » message  | string      | true | none |        | none |
| » wording  | string      | true | none |        | none |
| » echo     | string¦null | true | none |        | none |

## POST .对事件执行快速操作

POST /.handle_quick_operation

相当于 http 的快速操作

> Body 请求参数

```json
{
  "context": {},
  "operation": {}
}
```

### 请求参数

| 名称        | 位置 | 类型   | 必选 | 说明         |
| ----------- | ---- | ------ | ---- | ------------ |
| body        | body | object | 否   | none         |
| » context   | body | object | 是   | 事件数据对象 |
| » operation | body | object | 是   | 快速操作对象 |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取 CSRF Token

POST /get_csrf_token

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "token": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» token  | number      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST \_删除群公告

POST /\_del_group_notice

> Body 请求参数

```json
{
  "group_id": 0,
  "notice_id": "string"
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |
| » notice_id    | body | string | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": 0,
    "errMsg": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» result | number      | true | none |        | none |
| »» errMsg | string      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取被过滤的加群请求

POST /get_group_ignore_add_request

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "request_id": 0,
      "invitor_uin": 0,
      "invitor_nick": "string",
      "group_id": 0,
      "message": "string",
      "group_name": "string",
      "checked": true,
      "actor": 0,
      "requester_nick": "string"
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称              | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ----------------- | ----------- | ---- | ---- | ------ | ---- |
| » status          | string      | true | none |        | none |
| » retcode         | number      | true | none |        | none |
| » data            | [object]    | true | none |        | none |
| »» request_id     | number      | true | none |        | none |
| »» invitor_uin    | number      | true | none |        | none |
| »» invitor_nick   | string¦null | true | none |        | none |
| »» group_id       | number¦null | true | none |        | none |
| »» message        | string¦null | true | none |        | none |
| »» group_name     | string¦null | true | none |        | none |
| »» checked        | boolean     | true | none |        | none |
| »» actor          | number      | true | none |        | none |
| »» requester_nick | string¦null | true | none |        | none |
| » message         | string      | true | none |        | none |
| » wording         | string      | true | none |        | none |
| » echo            | string¦null | true | none |        | none |

## POST 获取 QQ 相关接口凭证

POST /get_credentials

> Body 请求参数

```json
{
  "domain": "string"
}
```

### 请求参数

| 名称     | 位置 | 类型   | 必选 | 说明 |
| -------- | ---- | ------ | ---- | ---- |
| body     | body | object | 否   | none |
| » domain | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "cookies": "string",
    "token": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称       | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ---------- | ----------- | ---- | ---- | ------ | ---- |
| » status   | string      | true | none |        | none |
| » retcode  | number      | true | none |        | none |
| » data     | object      | true | none |        | none |
| »» cookies | string      | true | none |        | none |
| »» token   | number      | true | none |        | none |
| » message  | string      | true | none |        | none |
| » wording  | string      | true | none |        | none |
| » echo     | string¦null | true | none |        | none |

## POST \_获取在线机型

POST /\_get_model_show

> Body 请求参数

```json
{
  "model": "string"
}
```

### 请求参数

| 名称    | 位置 | 类型   | 必选 | 说明 |
| ------- | ---- | ------ | ---- | ---- |
| body    | body | object | 否   | none |
| » model | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "variants": {
        "model_show": "string",
        "need_pay": true
      }
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称           | 类型        | 必选 | 约束 | 中文名 | 说明 |
| -------------- | ----------- | ---- | ---- | ------ | ---- |
| » status       | string      | true | none |        | none |
| » retcode      | number      | true | none |        | none |
| » data         | [object]    | true | none |        | none |
| »» variants    | object      | true | none |        | none |
| »»» model_show | string      | true | none |        | none |
| »»» need_pay   | boolean     | true | none |        | none |
| » message      | string      | true | none |        | none |
| » wording      | string      | true | none |        | none |
| » echo         | string¦null | true | none |        | none |

## POST \_设置在线机型

POST /\_set_model_show

> Body 请求参数

```json
{
  "model": "string",
  "model_show": "string"
}
```

### 请求参数

| 名称         | 位置 | 类型   | 必选 | 说明 |
| ------------ | ---- | ------ | ---- | ---- |
| body         | body | object | 否   | none |
| » model      | body | string | 是   | none |
| » model_show | body | string | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 检查是否可以发送图片

POST /can_send_image

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "yes": true
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» yes    | boolean     | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取 packet 状态

POST /nc_get_packet_status

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": null,
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | null        | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 检查是否可以发送语音

POST /can_send_record

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "yes": true
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» yes    | boolean     | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取状态

POST /get_status

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "online": true,
    "good": true,
    "stat": {}
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | object      | true | none |        | none |
| »» online | boolean     | true | none |        | none |
| »» good   | boolean     | true | none |        | none |
| »» stat   | object      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取 rkey

POST /nc_get_rkey

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": [
    {
      "rkey": "string",
      "ttl": "string",
      "time": 0,
      "type": 0
    }
  ],
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称      | 类型        | 必选 | 约束 | 中文名 | 说明 |
| --------- | ----------- | ---- | ---- | ------ | ---- |
| » status  | string      | true | none |        | none |
| » retcode | number      | true | none |        | none |
| » data    | [object]    | true | none |        | none |
| »» rkey   | string      | true | none |        | none |
| »» ttl    | string      | true | none |        | none |
| »» time   | number      | true | none |        | none |
| »» type   | number      | true | none |        | none |
| » message | string      | true | none |        | none |
| » wording | string      | true | none |        | none |
| » echo    | string¦null | true | none |        | none |

## POST 获取版本信息

POST /get_version_info

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "app_name": "string",
    "protocol_version": "string",
    "app_version": "string"
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------------------- | ----------- | ---- | ---- | ------ | ---- |
| » status            | string      | true | none |        | none |
| » retcode           | number      | true | none |        | none |
| » data              | object      | true | none |        | none |
| »» app_name         | string      | true | none |        | none |
| »» protocol_version | string      | true | none |        | none |
| »» app_version      | string      | true | none |        | none |
| » message           | string      | true | none |        | none |
| » wording           | string      | true | none |        | none |
| » echo              | string¦null | true | none |        | none |

## POST 获取群禁言列表

POST /get_group_shut_list

> Body 请求参数

```json
{
  "group_id": 1012451981
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明              |
| -------------- | ---- | ------ | ---- | ----------------- |
| body           | body | object | 否   | none              |
| » group_id     | body | any    | 是   | 和 user_id 二选一 |
| »» _anonymous_ | body | number | 否   | none              |
| »» _anonymous_ | body | string | 否   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "uid": "string",
    "qid": "string",
    "uin": "string",
    "nick": "string",
    "remark": "string",
    "cardType": 0,
    "cardName": "string",
    "role": 0,
    "avatarPath": "string",
    "shutUpTime": 0,
    "isDelete": true,
    "isSpecialConcerned": true,
    "isSpecialShield": true,
    "isRobot": true,
    "groupHonor": {
      "0": 0,
      "1": 0,
      "2": 0,
      "3": 0
    },
    "memberRealLevel": 0,
    "memberLevel": 0,
    "globalGroupLevel": 0,
    "globalGroupPoint": 0,
    "memberTitleId": 0,
    "memberSpecialTitle": "string",
    "specialTitleExpireTime": "string",
    "userShowFlag": 0,
    "userShowFlagNew": 0,
    "richFlag": 0,
    "mssVipType": 0,
    "bigClubLevel": 0,
    "bigClubFlag": 0,
    "autoRemark": "string",
    "creditLevel": 0,
    "joinTime": 0,
    "lastSpeakTime": 0,
    "memberFlag": 0,
    "memberFlagExt": 0,
    "memberMobileFlag": 0,
    "memberFlagExt2": 0,
    "isSpecialShielded": true,
    "cardNameId": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称                      | 类型        | 必选 | 约束 | 中文名 | 说明         |
| ------------------------- | ----------- | ---- | ---- | ------ | ------------ |
| » status                  | string      | true | none |        | none         |
| » retcode                 | number      | true | none |        | none         |
| » data                    | object      | true | none |        | none         |
| »» uid                    | string      | true | none |        | none         |
| »» qid                    | string      | true | none |        | none         |
| »» uin                    | string      | true | none |        | none         |
| »» nick                   | string      | true | none |        | none         |
| »» remark                 | string      | true | none |        | none         |
| »» cardType               | number      | true | none |        | none         |
| »» cardName               | string      | true | none |        | none         |
| »» role                   | number      | true | none |        | none         |
| »» avatarPath             | string      | true | none |        | none         |
| »» shutUpTime             | number      | true | none |        | 解禁时间     |
| »» isDelete               | boolean     | true | none |        | none         |
| »» isSpecialConcerned     | boolean     | true | none |        | none         |
| »» isSpecialShield        | boolean     | true | none |        | none         |
| »» isRobot                | boolean     | true | none |        | none         |
| »» groupHonor             | object      | true | none |        | none         |
| »»» 0                     | number      | true | none |        | none         |
| »»» 1                     | number      | true | none |        | none         |
| »»» 2                     | number      | true | none |        | none         |
| »»» 3                     | number      | true | none |        | none         |
| »» memberRealLevel        | number      | true | none |        | 群聊等级     |
| »» memberLevel            | number      | true | none |        | none         |
| »» globalGroupLevel       | number      | true | none |        | none         |
| »» globalGroupPoint       | number      | true | none |        | none         |
| »» memberTitleId          | number      | true | none |        | none         |
| »» memberSpecialTitle     | string      | true | none |        | none         |
| »» specialTitleExpireTime | string      | true | none |        | none         |
| »» userShowFlag           | number      | true | none |        | none         |
| »» userShowFlagNew        | number      | true | none |        | none         |
| »» richFlag               | number      | true | none |        | none         |
| »» mssVipType             | number      | true | none |        | none         |
| »» bigClubLevel           | number      | true | none |        | none         |
| »» bigClubFlag            | number      | true | none |        | none         |
| »» autoRemark             | string      | true | none |        | none         |
| »» creditLevel            | number      | true | none |        | none         |
| »» joinTime               | number      | true | none |        | 入群时间     |
| »» lastSpeakTime          | number      | true | none |        | 最后发言时间 |
| »» memberFlag             | number      | true | none |        | none         |
| »» memberFlagExt          | number      | true | none |        | none         |
| »» memberMobileFlag       | number      | true | none |        | none         |
| »» memberFlagExt2         | number      | true | none |        | none         |
| »» isSpecialShielded      | boolean     | true | none |        | none         |
| »» cardNameId             | number      | true | none |        | none         |
| » message                 | string      | true | none |        | none         |
| » wording                 | string      | true | none |        | none         |
| » echo                    | string¦null | true | none |        | none         |

# 未定义/保留

## POST send_group_msg

POST /send_group_msg

发送群消息

> Body 请求参数

```json
{
  "group_id": 0,
  "message": [
    {
      "type": "text",
      "data": {
        "text": "string"
      }
    }
  ]
}
```

### 请求参数

| 名称              | 位置 | 类型                                 | 必选 | 说明              |
| ----------------- | ---- | ------------------------------------ | ---- | ----------------- |
| body              | body | object                               | 否   | none              |
| » group_id        | body | any                                  | 是   | 和 user_id 二选一 |
| »» _anonymous_    | body | number                               | 否   | none              |
| »» _anonymous_    | body | string                               | 否   | none              |
| » message         | body | [anyOf]                              | 是   | none              |
| »» _anonymous_    | body | [文本消息](#schema文本消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» text         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [艾特消息](#schema艾特消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» qq           | body | any                                  | 是   | none              |
| »»»»» _anonymous_ | body | string                               | 否   | none              |
| »»»»» _anonymous_ | body | number                               | 否   | none              |
| »»»»» _anonymous_ | body | string                               | 否   | none              |
| »»»» name         | body | string                               | 否   | none              |
| »» _anonymous_    | body | [表情消息](#schema表情消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» id           | body | number                               | 是   | none              |
| »» _anonymous_    | body | [图片消息](#schema图片消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» file         | body | string                               | 是   | none              |
| »»»» summary      | body | string                               | 否   | none              |
| »» _anonymous_    | body | [回复消息](#schema回复消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» id           | body | any                                  | 是   | none              |
| »»»»» _anonymous_ | body | string                               | 否   | none              |
| »»»»» _anonymous_ | body | number                               | 否   | none              |
| »» _anonymous_    | body | [JSON 消息](#schemajson消息)         | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» data         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [语音消息](#schema语音消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» file         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [视频消息](#schema视频消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» file         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [markdown 消息](#schemamarkdown消息) | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» content      | body | string                               | 是   | none              |

> 返回示例

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_id": 696124706
  },
  "message": "",
  "wording": ""
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名  | 说明    |
| ------------- | ----------- | ---- | ---- | ------- | ------- |
| » status      | string      | true | none |         | none    |
| » retcode     | number      | true | none |         | none    |
| » data        | object      | true | none |         | none    |
| »» message_id | number      | true | none | 消息 ID | 消息 ID |
| » message     | string      | true | none |         | none    |
| » wording     | string      | true | none |         | none    |
| » echo        | string¦null | true | none |         | none    |

## POST send_private_msg

POST /send_private_msg

> Body 请求参数

```json
{
  "user_id": 0,
  "message": [
    {
      "type": "text",
      "data": {
        "text": "string"
      }
    }
  ]
}
```

### 请求参数

| 名称              | 位置 | 类型                                 | 必选 | 说明 |
| ----------------- | ---- | ------------------------------------ | ---- | ---- |
| body              | body | object                               | 否   | none |
| » user_id         | body | any                                  | 是   | none |
| »» _anonymous_    | body | number                               | 否   | none |
| »» _anonymous_    | body | string                               | 否   | none |
| » message         | body | [anyOf]                              | 是   | none |
| »» _anonymous_    | body | [文本消息](#schema文本消息)          | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» text         | body | string                               | 是   | none |
| »» _anonymous_    | body | [表情消息](#schema表情消息)          | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» id           | body | number                               | 是   | none |
| »» _anonymous_    | body | [图片消息](#schema图片消息)          | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» file         | body | string                               | 是   | none |
| »»»» summary      | body | string                               | 否   | none |
| »» _anonymous_    | body | [回复消息](#schema回复消息)          | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» id           | body | any                                  | 是   | none |
| »»»»» _anonymous_ | body | string                               | 否   | none |
| »»»»» _anonymous_ | body | number                               | 否   | none |
| »» _anonymous_    | body | [JSON 消息](#schemajson消息)         | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» data         | body | string                               | 是   | none |
| »» _anonymous_    | body | [语音消息](#schema语音消息)          | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» file         | body | string                               | 是   | none |
| »» _anonymous_    | body | [视频消息](#schema视频消息)          | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» file         | body | string                               | 是   | none |
| »» _anonymous_    | body | [markdown 消息](#schemamarkdown消息) | 否   | none |
| »»» type          | body | string                               | 是   | none |
| »»» data          | body | object                               | 是   | none |
| »»»» content      | body | string                               | 是   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_id": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名  | 说明    |
| ------------- | ----------- | ---- | ---- | ------- | ------- |
| » status      | string      | true | none |         | none    |
| » retcode     | number      | true | none |         | none    |
| » data        | object      | true | none |         | none    |
| »» message_id | number      | true | none | 消息 ID | 消息 ID |
| » message     | string      | true | none |         | none    |
| » wording     | string      | true | none |         | none    |
| » echo        | string¦null | true | none |         | none    |

## POST send_msg

POST /send_msg

> Body 请求参数

```json
"{\r\n    \"message_type\": \"private\", //group | private\r\n    \"group_id\": \"480972475\",\r\n    \"user_id\": \"480972475\", // type为group时不填写\r\n    \"message\": [\r\n        {\r\n            \"type\": \"text\",\r\n            \"data\": {\r\n                \"text\": \"用面才务。定比眼表县。写单写加很研科。打王运土照。化知金步家你龙。全展标新。\"\r\n            }\r\n        }\r\n    ]\r\n}"
```

### 请求参数

| 名称              | 位置 | 类型                                 | 必选 | 说明              |
| ----------------- | ---- | ------------------------------------ | ---- | ----------------- |
| body              | body | object                               | 否   | none              |
| » message_type    | body | any                                  | 是   | none              |
| »» _anonymous_    | body | string                               | 否   | none              |
| »» _anonymous_    | body | string                               | 否   | none              |
| » group_id        | body | any                                  | 是   | 和 user_id 二选一 |
| »» _anonymous_    | body | number                               | 否   | none              |
| »» _anonymous_    | body | string                               | 否   | none              |
| » user_id         | body | any                                  | 是   | none              |
| »» _anonymous_    | body | number                               | 否   | none              |
| »» _anonymous_    | body | string                               | 否   | none              |
| » message         | body | [anyOf]                              | 是   | none              |
| »» _anonymous_    | body | [文本消息](#schema文本消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» text         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [艾特消息](#schema艾特消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» qq           | body | any                                  | 是   | none              |
| »»»»» _anonymous_ | body | string                               | 否   | none              |
| »»»»» _anonymous_ | body | number                               | 否   | none              |
| »»»»» _anonymous_ | body | string                               | 否   | none              |
| »»»» name         | body | string                               | 否   | none              |
| »» _anonymous_    | body | [表情消息](#schema表情消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» id           | body | number                               | 是   | none              |
| »» _anonymous_    | body | [图片消息](#schema图片消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» file         | body | string                               | 是   | none              |
| »»»» summary      | body | string                               | 否   | none              |
| »» _anonymous_    | body | [回复消息](#schema回复消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» id           | body | any                                  | 是   | none              |
| »»»»» _anonymous_ | body | string                               | 否   | none              |
| »»»»» _anonymous_ | body | number                               | 否   | none              |
| »» _anonymous_    | body | [JSON 消息](#schemajson消息)         | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» data         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [语音消息](#schema语音消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» file         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [视频消息](#schema视频消息)          | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» file         | body | string                               | 是   | none              |
| »» _anonymous_    | body | [markdown 消息](#schemamarkdown消息) | 否   | none              |
| »»» type          | body | string                               | 是   | none              |
| »»» data          | body | object                               | 是   | none              |
| »»»» content      | body | string                               | 是   | none              |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "message_id": 0
  },
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

状态码 **200**

| 名称          | 类型        | 必选 | 约束 | 中文名  | 说明    |
| ------------- | ----------- | ---- | ---- | ------- | ------- |
| » status      | string      | true | none |         | none    |
| » retcode     | number      | true | none |         | none    |
| » data        | object      | true | none |         | none    |
| »» message_id | number      | true | none | 消息 ID | 消息 ID |
| » message     | string      | true | none |         | none    |
| » wording     | string      | true | none |         | none    |
| » echo        | string¦null | true | none |         | none    |

# 未定义/接口

## POST send_packet

POST /send_packet

> Body 请求参数

```json
{}
```

### 请求参数

| 名称 | 位置 | 类型   | 必选 | 说明 |
| ---- | ---- | ------ | ---- | ---- |
| body | body | object | 否   | none |

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## GET unknown

GET /unknown

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## POST fetch_user_profile_like

POST /fetch_user_profile_like

> Body 请求参数

```json
{
  "qq": 1129317309
}
```

### 请求参数

| 名称           | 位置 | 类型   | 必选 | 说明 |
| -------------- | ---- | ------ | ---- | ---- |
| body           | body | object | 否   | none |
| » user_id      | body | any    | 是   | none |
| »» _anonymous_ | body | number | 否   | none |
| »» _anonymous_ | body | string | 否   | none |

> 返回示例

> 200 Response

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型                |
| ------ | ------------------------------------------------------- | ---- | ----------------------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | [result](#schemaresult) |

## GET get_guild_list

GET /get_guild_list

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## GET get_guild_service_profile

GET /get_guild_service_profile

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## POST 检查链接安全性

POST /check_url_safely

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

## POST 获取中文分词

POST /.get_word_slices

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

| 状态码 | 状态码含义                                              | 说明 | 数据模型 |
| ------ | ------------------------------------------------------- | ---- | -------- |
| 200    | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline   |

### 返回数据结构

# 数据模型

<h2 id="tocS_group_id">group_id</h2>

<a id="schemagroup_id"></a>
<a id="schema_group_id"></a>
<a id="tocSgroup_id"></a>
<a id="tocsgroup_id"></a>

```json
0
```

### 属性

oneOf

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| _anonymous_ | number | false | none |        | none |

xor

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| _anonymous_ | string | false | none |        | none |

<h2 id="tocS_user_id">user_id</h2>

<a id="schemauser_id"></a>
<a id="schema_user_id"></a>
<a id="tocSuser_id"></a>
<a id="tocsuser_id"></a>

```json
0
```

### 属性

oneOf

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| _anonymous_ | number | false | none |        | none |

xor

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| _anonymous_ | string | false | none |        | none |

<h2 id="tocS_message_id">message_id</h2>

<a id="schemamessage_id"></a>
<a id="schema_message_id"></a>
<a id="tocSmessage_id"></a>
<a id="tocsmessage_id"></a>

```json
0
```

### 属性

oneOf

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| _anonymous_ | number | false | none |        | none |

xor

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ----------- | ------ | ----- | ---- | ------ | ---- |
| _anonymous_ | string | false | none |        | none |

<h2 id="tocS_好友信息">好友信息</h2>

<a id="schema好友信息"></a>
<a id="schema_好友信息"></a>
<a id="tocS好友信息"></a>
<a id="tocs好友信息"></a>

```json
{
  "qid": "string",
  "longNick": "string",
  "birthday_year": 0,
  "birthday_month": 0,
  "birthday_day": 0,
  "age": 0,
  "sex": "string",
  "eMail": "string",
  "phoneNum": "string",
  "categoryId": 0,
  "richTime": 0,
  "richBuffer": {},
  "uid": "string",
  "uin": "string",
  "nick": "string",
  "remark": "string",
  "user_id": 0,
  "nickname": "string",
  "level": 0
}
```

### 属性

| 名称           | 类型   | 必选 | 约束 | 中文名 | 说明     |
| -------------- | ------ | ---- | ---- | ------ | -------- |
| qid            | string | true | none |        | QQID     |
| longNick       | string | true | none |        | 个性签名 |
| birthday_year  | number | true | none |        | 生日\_年 |
| birthday_month | number | true | none |        | 生日\_月 |
| birthday_day   | number | true | none |        | 生日\_日 |
| age            | number | true | none |        | 年龄     |
| sex            | string | true | none |        | 性别     |
| eMail          | string | true | none |        | 邮箱     |
| phoneNum       | string | true | none |        | 手机号   |
| categoryId     | number | true | none |        | 分类     |
| richTime       | number | true | none |        | 注册时间 |
| richBuffer     | object | true | none |        | none     |
| uid            | string | true | none |        | none     |
| uin            | string | true | none |        | none     |
| nick           | string | true | none |        | none     |
| remark         | string | true | none |        | 备注     |
| user_id        | number | true | none |        | none     |
| nickname       | string | true | none |        | none     |
| level          | number | true | none |        | 等级     |

<h2 id="tocS_群信息">群信息</h2>

<a id="schema群信息"></a>
<a id="schema_群信息"></a>
<a id="tocS群信息"></a>
<a id="tocs群信息"></a>

```json
{
  "group_id": 0,
  "group_name": "string",
  "member_count": 0,
  "max_member_count": 0
}
```

### 属性

| 名称             | 类型   | 必选 | 约束 | 中文名 | 说明           |
| ---------------- | ------ | ---- | ---- | ------ | -------------- |
| group_id         | number | true | none |        | 群号           |
| group_name       | string | true | none |        | 群名           |
| member_count     | number | true | none |        | 群成员数量     |
| max_member_count | number | true | none |        | 群最大成员数量 |

<h2 id="tocS_群成员信息">群成员信息</h2>

<a id="schema群成员信息"></a>
<a id="schema_群成员信息"></a>
<a id="tocS群成员信息"></a>
<a id="tocs群成员信息"></a>

```json
{
  "group_id": 0,
  "user_id": 0,
  "nickname": "string",
  "card": "string",
  "sex": "string",
  "age": 0,
  "area": "string",
  "level": 0,
  "qq_level": 0,
  "join_time": 0,
  "last_sent_time": 0,
  "title_expire_time": 0,
  "unfriendly": true,
  "card_changeable": true,
  "is_robot": true,
  "shut_up_timestamp": 0,
  "role": "string",
  "title": "string"
}
```

### 属性

| 名称              | 类型    | 必选 | 约束 | 中文名 | 说明         |
| ----------------- | ------- | ---- | ---- | ------ | ------------ |
| group_id          | number  | true | none |        | none         |
| user_id           | number  | true | none |        | none         |
| nickname          | string  | true | none |        | none         |
| card              | string  | true | none |        | 群昵称       |
| sex               | string  | true | none |        | 性别         |
| age               | number  | true | none |        | 年龄         |
| area              | string  | true | none |        | none         |
| level             | number  | true | none |        | 群等级       |
| qq_level          | number  | true | none |        | 账号等级     |
| join_time         | number  | true | none |        | 加群时间     |
| last_sent_time    | number  | true | none |        | 最后发言时间 |
| title_expire_time | number  | true | none |        | none         |
| unfriendly        | boolean | true | none |        | none         |
| card_changeable   | boolean | true | none |        | none         |
| is_robot          | boolean | true | none |        | 是否机器人   |
| shut_up_timestamp | number  | true | none |        | 禁言时长     |
| role              | string  | true | none |        | 权限         |
| title             | string  | true | none |        | 头衔         |

<h2 id="tocS_龙王信息">龙王信息</h2>

<a id="schema龙王信息"></a>
<a id="schema_龙王信息"></a>
<a id="tocS龙王信息"></a>
<a id="tocs龙王信息"></a>

```json
{
  "user_id": 0,
  "avatar": "string",
  "nickname": "string",
  "day_count": 0,
  "description": "string"
}
```

### 属性

| 名称        | 类型   | 必选  | 约束 | 中文名 | 说明     |
| ----------- | ------ | ----- | ---- | ------ | -------- |
| user_id     | number | false | none |        | none     |
| avatar      | string | false | none |        | 头像     |
| nickname    | string | false | none |        | none     |
| day_count   | number | false | none |        | 连续天数 |
| description | string | false | none |        | 说明     |

<h2 id="tocS_消息详情">消息详情</h2>

<a id="schema消息详情"></a>
<a id="schema_消息详情"></a>
<a id="tocS消息详情"></a>
<a id="tocs消息详情"></a>

```json
{
  "self_id": 0,
  "user_id": 0,
  "time": 0,
  "message_id": 0,
  "message_seq": 0,
  "real_id": 0,
  "message_type": "string",
  "sender": {
    "user_id": 0,
    "nickname": "string",
    "sex": "male",
    "age": 0,
    "card": "string",
    "role": "owner"
  },
  "raw_message": "string",
  "font": 0,
  "sub_type": "string",
  "message": [
    {
      "type": "text",
      "data": {
        "text": "string"
      }
    }
  ],
  "message_format": "string",
  "post_type": "string",
  "message_sent_type": "string",
  "group_id": 0
}
```

### 属性

| 名称         | 类型                    | 必选 | 约束 | 中文名 | 说明 |
| ------------ | ----------------------- | ---- | ---- | ------ | ---- |
| self_id      | number                  | true | none |        | none |
| user_id      | number                  | true | none |        | none |
| time         | number                  | true | none |        | none |
| message_id   | number                  | true | none |        | none |
| message_seq  | number                  | true | none |        | none |
| real_id      | number                  | true | none |        | none |
| message_type | string                  | true | none |        | none |
| sender       | [sender](#schemasender) | true | none |        | none |
| raw_message  | string                  | true | none |        | none |
| font         | number                  | true | none |        | none |
| sub_type     | string                  | true | none |        | none |
| message      | [anyOf]                 | true | none |        | none |

anyOf

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [艾特消息](#schema艾特消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |

or

| 名称          | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| ------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [语音消息](#schema语音消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |

or

| 名称          | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| ------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| » _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |

continued

| 名称              | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ----------------- | ------ | ---- | ---- | ------ | ---- |
| message_format    | string | true | none |        | none |
| post_type         | string | true | none |        | none |
| message_sent_type | string | true | none |        | none |
| group_id          | number | true | none |        | none |

<h2 id="tocS_文本消息">文本消息</h2>

<a id="schema文本消息"></a>
<a id="schema_文本消息"></a>
<a id="tocS文本消息"></a>
<a id="tocs文本消息"></a>

```json
{
  "type": "text",
  "data": {
    "text": "string"
  }
}
```

### 属性

| 名称   | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ------ | ------ | ---- | ---- | ------ | ---- |
| type   | string | true | none |        | none |
| data   | object | true | none |        | none |
| » text | string | true | none |        | none |

<h2 id="tocS_艾特消息">艾特消息</h2>

<a id="schema艾特消息"></a>
<a id="schema_艾特消息"></a>
<a id="tocS艾特消息"></a>
<a id="tocs艾特消息"></a>

```json
{
  "type": "at",
  "data": {
    "qq": "string",
    "name": "string"
  }
}
```

### 属性

| 名称 | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ---- | ------ | ---- | ---- | ------ | ---- |
| type | string | true | none |        | none |
| data | object | true | none |        | none |
| » qq | any    | true | none |        | none |

oneOf

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | string | false | none |        | none |

xor

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | number | false | none |        | none |

xor

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | string | false | none |        | none |

continued

| 名称   | 类型   | 必选  | 约束 | 中文名 | 说明 |
| ------ | ------ | ----- | ---- | ------ | ---- |
| » name | string | false | none |        | none |

<h2 id="tocS_表情消息">表情消息</h2>

<a id="schema表情消息"></a>
<a id="schema_表情消息"></a>
<a id="tocS表情消息"></a>
<a id="tocs表情消息"></a>

```json
{
  "type": "face",
  "data": {
    "id": 0
  }
}
```

### 属性

| 名称 | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ---- | ------ | ---- | ---- | ------ | ---- |
| type | string | true | none |        | none |
| data | object | true | none |        | none |
| » id | number | true | none |        | none |

<h2 id="tocS_图片消息">图片消息</h2>

<a id="schema图片消息"></a>
<a id="schema_图片消息"></a>
<a id="tocS图片消息"></a>
<a id="tocs图片消息"></a>

```json
{
  "type": "image",
  "data": {
    "file": "string",
    "summary": "[图片]"
  }
}
```

### 属性

| 名称      | 类型   | 必选  | 约束 | 中文名 | 说明 |
| --------- | ------ | ----- | ---- | ------ | ---- |
| type      | string | true  | none |        | none |
| data      | object | true  | none |        | none |
| » file    | string | true  | none |        | none |
| » summary | string | false | none |        | none |

<h2 id="tocS_回复消息">回复消息</h2>

<a id="schema回复消息"></a>
<a id="schema_回复消息"></a>
<a id="tocS回复消息"></a>
<a id="tocs回复消息"></a>

```json
{
  "type": "reply",
  "data": {
    "id": "string"
  }
}
```

### 属性

| 名称 | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ---- | ------ | ---- | ---- | ------ | ---- |
| type | string | true | none |        | none |
| data | object | true | none |        | none |
| » id | any    | true | none |        | none |

oneOf

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | string | false | none |        | none |

xor

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | number | false | none |        | none |

<h2 id="tocS_JSON消息">JSON消息</h2>

<a id="schemajson消息"></a>
<a id="schema_JSON消息"></a>
<a id="tocSjson消息"></a>
<a id="tocsjson消息"></a>

```json
{
  "type": "json",
  "data": {
    "data": "string"
  }
}
```

### 属性

| 名称   | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ------ | ------ | ---- | ---- | ------ | ---- |
| type   | string | true | none |        | none |
| data   | object | true | none |        | none |
| » data | string | true | none |        | none |

<h2 id="tocS_语音消息">语音消息</h2>

<a id="schema语音消息"></a>
<a id="schema_语音消息"></a>
<a id="tocS语音消息"></a>
<a id="tocs语音消息"></a>

```json
{
  "type": "record",
  "data": {
    "file": "string"
  }
}
```

### 属性

| 名称   | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ------ | ------ | ---- | ---- | ------ | ---- |
| type   | string | true | none |        | none |
| data   | object | true | none |        | none |
| » file | string | true | none |        | none |

<h2 id="tocS_视频消息">视频消息</h2>

<a id="schema视频消息"></a>
<a id="schema_视频消息"></a>
<a id="tocS视频消息"></a>
<a id="tocs视频消息"></a>

```json
{
  "type": "video",
  "data": {
    "file": "string"
  }
}
```

### 属性

| 名称   | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ------ | ------ | ---- | ---- | ------ | ---- |
| type   | string | true | none |        | none |
| data   | object | true | none |        | none |
| » file | string | true | none |        | none |

<h2 id="tocS_markdown消息">markdown消息</h2>

<a id="schemamarkdown消息"></a>
<a id="schema_markdown消息"></a>
<a id="tocSmarkdown消息"></a>
<a id="tocsmarkdown消息"></a>

```json
{
  "type": "record",
  "data": {
    "content": "string"
  }
}
```

### 属性

| 名称      | 类型   | 必选 | 约束 | 中文名 | 说明 |
| --------- | ------ | ---- | ---- | ------ | ---- |
| type      | string | true | none |        | none |
| data      | object | true | none |        | none |
| » content | string | true | none |        | none |

<h2 id="tocS_音乐卡片消息">音乐卡片消息</h2>

<a id="schema音乐卡片消息"></a>
<a id="schema_音乐卡片消息"></a>
<a id="tocS音乐卡片消息"></a>
<a id="tocs音乐卡片消息"></a>

```json
{
  "type": "music",
  "data": {
    "type": "163",
    "id": "string"
  }
}
```

### 属性

| 名称   | 类型   | 必选 | 约束 | 中文名 | 说明    |
| ------ | ------ | ---- | ---- | ------ | ------- |
| type   | string | true | none |        | none    |
| data   | object | true | none |        | none    |
| » type | string | true | none |        | none    |
| » id   | string | true | none |        | 音乐 id |

#### 枚举值

| 属性 | 值  |
| ---- | --- |
| type | 163 |
| type | qq  |

<h2 id="tocS_自定义音乐卡片消息">自定义音乐卡片消息</h2>

<a id="schema自定义音乐卡片消息"></a>
<a id="schema_自定义音乐卡片消息"></a>
<a id="tocS自定义音乐卡片消息"></a>
<a id="tocs自定义音乐卡片消息"></a>

```json
{
  "type": "music",
  "data": {
    "type": "custom",
    "url": "string",
    "audio": "string",
    "title": "string",
    "image": "string"
  }
}
```

### 属性

| 名称    | 类型   | 必选 | 约束 | 中文名 | 说明   |
| ------- | ------ | ---- | ---- | ------ | ------ |
| type    | string | true | none |        | none   |
| data    | object | true | none |        | none   |
| » type  | string | true | none |        | custom |
| » url   | string | true | none |        | 链接   |
| » audio | string | true | none |        | 音频   |
| » title | string | true | none |        | 标题   |
| » image | string | true | none |        | 图片   |

<h2 id="tocS_二级合并转发消息">二级合并转发消息</h2>

<a id="schema二级合并转发消息"></a>
<a id="schema_二级合并转发消息"></a>
<a id="tocS二级合并转发消息"></a>
<a id="tocs二级合并转发消息"></a>

```json
{
  "type": "node",
  "data": {
    "user_id": "string",
    "nickname": "string",
    "content": [
      {
        "type": "text",
        "data": {}
      }
    ],
    "news": [
      {
        "text": "string"
      }
    ],
    "prompt": "string",
    "summary": "string",
    "source": "string"
  }
}
```

### 属性

| 名称      | 类型   | 必选 | 约束 | 中文名 | 说明 |
| --------- | ------ | ---- | ---- | ------ | ---- |
| type      | string | true | none |        | none |
| data      | object | true | none |        | none |
| » user_id | any    | true | none |        | none |

oneOf

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | string | false | none |        | none |

xor

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | number | false | none |        | none |

continued

| 名称       | 类型    | 必选 | 约束 | 中文名 | 说明 |
| ---------- | ------- | ---- | ---- | ------ | ---- |
| » nickname | string  | true | none |        | none |
| » content  | [anyOf] | true | none |        | 构建 |

anyOf

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |

or

| 名称           | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |

or

| 名称           | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |

or

| 名称           | 类型                               | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ---------------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [发送 forward](#schema发送forward) | false | none |        | none |

or

| 名称           | 类型                                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------------------------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [二级合并转发消息](#schema二级合并转发消息) | false | none |        | none |

continued

| 名称      | 类型     | 必选  | 约束 | 中文名 | 说明     |
| --------- | -------- | ----- | ---- | ------ | -------- |
| » news    | [object] | false | none |        | 外显     |
| »» text   | string   | true  | none |        | 内容     |
| » prompt  | string   | false | none |        | 外显     |
| » summary | string   | false | none |        | 底下文本 |
| » source  | string   | false | none |        | 标题     |

<h2 id="tocS_发送forward">发送forward</h2>

<a id="schema发送forward"></a>
<a id="schema_发送forward"></a>
<a id="tocS发送forward"></a>
<a id="tocs发送forward"></a>

```json
{
  "type": "node",
  "data": {
    "user_id": 0,
    "nickname": "string",
    "content": {
      "type": "forward",
      "data": {
        "id": "string"
      }
    }
  }
}
```

### 属性

| 名称       | 类型                      | 必选 | 约束 | 中文名 | 说明   |
| ---------- | ------------------------- | ---- | ---- | ------ | ------ |
| type       | string                    | true | none |        | none   |
| data       | object                    | true | none |        | none   |
| » user_id  | [user_id](#schemauser_id) | true | none |        | none   |
| » nickname | string                    | true | none |        | none   |
| » content  | object                    | true | none |        | none   |
| »» type    | string                    | true | none |        | none   |
| »» data    | object                    | true | none |        | none   |
| »»» id     | string                    | true | none |        | res_id |

<h2 id="tocS_一级合并转发消息">一级合并转发消息</h2>

<a id="schema一级合并转发消息"></a>
<a id="schema_一级合并转发消息"></a>
<a id="tocS一级合并转发消息"></a>
<a id="tocs一级合并转发消息"></a>

```json
{
  "type": "node",
  "data": {
    "user_id": "string",
    "nickname": "string",
    "content": [
      {
        "type": "text",
        "data": {}
      }
    ]
  }
}
```

### 属性

| 名称      | 类型   | 必选 | 约束 | 中文名 | 说明 |
| --------- | ------ | ---- | ---- | ------ | ---- |
| type      | string | true | none |        | none |
| data      | object | true | none |        | none |
| » user_id | any    | true | none |        | none |

oneOf

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | string | false | none |        | none |

xor

| 名称           | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | number | false | none |        | none |

continued

| 名称       | 类型    | 必选 | 约束 | 中文名 | 说明 |
| ---------- | ------- | ---- | ---- | ------ | ---- |
| » nickname | string  | true | none |        | none |
| » content  | [anyOf] | true | none |        | 构建 |

anyOf

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |

or

| 名称           | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |

or

| 名称           | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | --------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |

or

| 名称           | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |

or

| 名称           | 类型                               | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ---------------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [发送 forward](#schema发送forward) | false | none |        | none |

or

| 名称           | 类型                                        | 必选  | 约束 | 中文名 | 说明 |
| -------------- | ------------------------------------------- | ----- | ---- | ------ | ---- |
| »» _anonymous_ | [二级合并转发消息](#schema二级合并转发消息) | false | none |        | none |

<h2 id="tocS_获取合并转发消息">获取合并转发消息</h2>

<a id="schema获取合并转发消息"></a>
<a id="schema_获取合并转发消息"></a>
<a id="tocS获取合并转发消息"></a>
<a id="tocs获取合并转发消息"></a>

```json
{
  "self_id": 0,
  "user_id": 0,
  "time": 0,
  "message_id": 0,
  "message_seq": 0,
  "real_id": 0,
  "message_type": "string",
  "sender": {
    "user_id": 0,
    "nickname": "string",
    "sex": "male",
    "age": 0,
    "card": "string",
    "role": "owner"
  },
  "raw_message": "string",
  "font": 0,
  "sub_type": "string",
  "message": [
    {
      "type": "text",
      "data": {
        "text": "string"
      }
    }
  ],
  "message_format": "string",
  "post_type": "string",
  "message_sent_type": "string",
  "group_id": 0
}
```

### 属性

| 名称         | 类型                    | 必选 | 约束 | 中文名 | 说明 |
| ------------ | ----------------------- | ---- | ---- | ------ | ---- |
| self_id      | number                  | true | none |        | none |
| user_id      | number                  | true | none |        | none |
| time         | number                  | true | none |        | none |
| message_id   | number                  | true | none |        | none |
| message_seq  | number                  | true | none |        | none |
| real_id      | number                  | true | none |        | none |
| message_type | string                  | true | none |        | none |
| sender       | [sender](#schemasender) | true | none |        | none |
| raw_message  | string                  | true | none |        | none |
| font         | number                  | true | none |        | none |
| sub_type     | string                  | true | none |        | none |
| message      | [anyOf]                 | true | none |        | none |

anyOf

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [文本消息](#schema文本消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [艾特消息](#schema艾特消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [表情消息](#schema表情消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [图片消息](#schema图片消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [回复消息](#schema回复消息) | false | none |        | none |

or

| 名称          | 类型                         | 必选  | 约束 | 中文名 | 说明 |
| ------------- | ---------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [JSON 消息](#schemajson消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [语音消息](#schema语音消息) | false | none |        | none |

or

| 名称          | 类型                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | --------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [视频消息](#schema视频消息) | false | none |        | none |

or

| 名称          | 类型                                 | 必选  | 约束 | 中文名 | 说明 |
| ------------- | ------------------------------------ | ----- | ---- | ------ | ---- |
| » _anonymous_ | [markdown 消息](#schemamarkdown消息) | false | none |        | none |

or

| 名称          | 类型                                        | 必选  | 约束 | 中文名 | 说明 |
| ------------- | ------------------------------------------- | ----- | ---- | ------ | ---- |
| » _anonymous_ | [获取合并转发消息](#schema获取合并转发消息) | false | none |        | none |

continued

| 名称              | 类型   | 必选 | 约束 | 中文名 | 说明 |
| ----------------- | ------ | ---- | ---- | ------ | ---- |
| message_format    | string | true | none |        | none |
| post_type         | string | true | none |        | none |
| message_sent_type | string | true | none |        | none |
| group_id          | number | true | none |        | none |

<h2 id="tocS_sender">sender</h2>

<a id="schemasender"></a>
<a id="schema_sender"></a>
<a id="tocSsender"></a>
<a id="tocssender"></a>

```json
{
  "user_id": 0,
  "nickname": "string",
  "sex": "male",
  "age": 0,
  "card": "string",
  "role": "owner"
}
```

### 属性

| 名称     | 类型   | 必选  | 约束 | 中文名 | 说明 |
| -------- | ------ | ----- | ---- | ------ | ---- |
| user_id  | number | true  | none |        | none |
| nickname | string | true  | none |        | none |
| sex      | string | false | none |        | none |
| age      | number | false | none |        | none |
| card     | string | false | none |        | none |
| role     | string | false | none |        | none |

#### 枚举值

| 属性 | 值      |
| ---- | ------- |
| sex  | male    |
| sex  | female  |
| sex  | unknown |
| role | owner   |
| role | admin   |
| role | member  |

<h2 id="tocS_result">result</h2>

<a id="schemaresult"></a>
<a id="schema_result"></a>
<a id="tocSresult"></a>
<a id="tocsresult"></a>

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {},
  "message": "string",
  "wording": "string",
  "echo": "string"
}
```

### 属性

| 名称    | 类型        | 必选 | 约束 | 中文名 | 说明 |
| ------- | ----------- | ---- | ---- | ------ | ---- |
| status  | string      | true | none |        | none |
| retcode | number      | true | none |        | none |
| data    | object      | true | none |        | none |
| message | string      | true | none |        | none |
| wording | string      | true | none |        | none |
| echo    | string¦null | true | none |        | none |
