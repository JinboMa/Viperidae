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

//路由页面引入
import Index from './pages/Index'
import Login from './pages/Login'
import Registration from './pages/Registration'

//vue-resource引入(发送http请求)
import VueResource from 'vue-resource'
Vue.use(VueResource)
Vue.http.options.emulateJSON = true
Vue.http.options.emulateHTTP = true
Vue.http.interceptors.push((request, next) => {
		// ...
		// 请求发送前的处理逻辑
		console.log("请求发送前",request)
		// ...
		next((response) => {
		// ...
		// 请求发送后的处理逻辑
		console.log("请求发送后",response)
		// ...
		// 根据请求的状态，response参数会返回给successCallback或errorCallback
		return response
	})
	})

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
		}]
	}),
	template: '<App/>',
	components: { App }
})
//全局变量地址
Vue.prototype.URL = "http://23.105.208.8:8088/"

//全局ajax方法
Vue.prototype.ajax = function(data){
	var postData = {
		url : this.URL+data.url,
		method : data.method,
		timeout: 5000
	}
	if(data.method == "GET"){
		postData.params = data.formData
	}else if(data.method == "POST"){
		postData.body = data.formData
	}
	Vue.http(postData).then(
	//成功函数
	(res)=>{
		//正确提示
		if(res.body.result){
			this.$message({
				message: data.successMsg,
				type: 'success'
			})
			data.success(res.body)
		}else{
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
