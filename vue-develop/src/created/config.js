import Vue from 'vue'

export default function(that){
	//this.ajax(this.setAjax("login",this.formData,this.success,this.fail))
	//全局接口配置
	Vue.prototype.ajaxConfig = {
		login : {
					method : "POST",
					url : "login",
					successMsg : "登录成功",
					failMsg : "登录失败",
					successAlert : true,
					failAlert : true,
					md5 : true
		},
		registration : {
					method : "POST",
					url : "registration",
					successMsg : "注册成功",
					failMsg : "注册失败",
					successAlert : true,
					failAlert : true,
					md5 : true
		},
		userSetting : {
					method : "POST",
					url : "user/setting",
					successMsg : "设置成功",
					failMsg : "设置失败",
					successAlert : true,
					failAlert : true
		},
		blogCreate : {
					method : "POST",
					url : "blog/create",
					successMsg : "保存成功",
					failMsg : "保存失败",
					successAlert : true,
					failAlert : true
		},
		blogEdit : {
					method : "POST",
					url : "blog/edit",
					successMsg : "保存成功",
					failMsg : "保存失败",
					successAlert : true,
					failAlert : true
		},
		blogList : {
					method : "GET",
					url : "blog/list",
					successMsg : "获取成功",
					failMsg : "获取失败",
					successAlert : true,
					failAlert : true
		},
		blog : {
					method : "GET",
					url : "blog",
					successMsg : "获取成功",
					failMsg : "获取失败",
					successAlert : true,
					failAlert : true
		},
	}
}