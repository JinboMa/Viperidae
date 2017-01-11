----
###### URI：/login

###### 功能：登陆

###### 请求方式：POST

###### 请求参数：

* telphone 
* password

###### 返回值

* result
* message
	如果result为True，则message为{}，如果result为False，message中的error参数返回错误信息

###### 额外返回值

cookie：名为user的cookie

###### URI：/registration
###### 功能：注册
###### 请求方式：POST

###### 请求参数：
* telphone 
* password

###### 返回值
* result
* message
	如果result为True，则message为{}，如果result为False，message中的error参数返回错误信息


###### URI：/user/setting
###### 功能：设置用户信息
###### 请求方式：POST

###### 请求参数：
* name 
* nickname
* password
* email
* telphone
* id_number

###### 返回值
* result
* message
	如果result为True，则message为{}，如果result为False，message中的error参数返回错误信息
