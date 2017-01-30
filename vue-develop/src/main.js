//初始化vue项目app模板
import Vue from 'vue'
import App from './App'

//vue路由配置引入文件
import Router from 'vue-router'
Vue.use(Router)

//elementUI引入
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(ElementUI)

//引入highlight css
import './assets/highlight.min.css'
//md5
import md5 from 'blueimp-md5'

//路由页面引入
import Index from './pages/Index'
import Login from './pages/Login'
import Registration from './pages/Registration'
import Blog from './pages/Blog'
import BlogList from './pages/BlogList'

//vue-resource引入(发送http请求)
import VueResource from 'vue-resource'
Vue.use(VueResource)
Vue.http.options.emulateJSON = true
Vue.http.options.emulateHTTP = true
Vue.http.options.credentials = true
Vue.http.interceptors.push((request, next) => {
		// ...
		// 请求发送前的处理逻辑
		// console.log("请求发送前",request)
		// ...
		next((response) => {
		// ...
		// 请求发送后的处理逻辑
		// console.log("请求发送后",response)
		// ...
		// 根据请求的状态，response参数会返回给successCallback或errorCallback
		return response
	})
	})

//全局变量地址
Vue.prototype.URL = "http://23.105.208.8:8088/"
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
}

new Vue({
	el: '#app',
	router: new Router({
		mode: "history",
		routes: [{
			path: "/",
			component: Index
		},{
			path: "/Login",
			component: Login
		},
		{
			path: "/Registration",
			component: Registration
		},
		{
			path: "/Blog",
			component: Blog
		},
		{
			path: "/BlogList",
			component: BlogList
		}]
	}),
	template: '<App/>',
	components: { App }
})

//全局ajax处理
Vue.prototype.setAjax = function(name,formData,success,fail){
	var postData = this.ajaxConfig[name];
		postData.formData = formData
		postData.success = success
		postData.fail = fail
	return postData
}

//全局ajax方法
Vue.prototype.ajax = function(data){
	var postData = {
		url : this.URL+data.url,
		method : data.method,
		timeout: 5000
	},
	formData = JSON.parse(JSON.stringify(data.formData))
	if(data.md5){
		formData.password = md5(data.formData.password)
	}
	if(data.method == "GET"){
		postData.params = formData
	}else if(data.method == "POST"){
		postData.body = formData
	}
	Vue.http(postData).then(
	//成功函数
	(res)=>{
		//正确提示
		if(res.body.result && data.successAlert){
			this.$message({
				message: data.successMsg,
				type: 'success'
			})
			data.success(res.body)
		}else if(data.failAlert){
			//错误提示
			this.$message.error(res.body.message.error)
		}
		this.loading = false
	},
	//失败函数
	(res)=>{
		this.$message.error(`网络错误'${res.status}',${data.failMsg}`)
		this.loading = false
		data.fail(res)
	})
}

Vue.prototype.setHeight = function(num){
	let height = window.innerHeight
	return (height - 60 - num)
}