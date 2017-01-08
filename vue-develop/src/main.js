//初始化vue项目app模板
import Vue from 'vue'
import App from './App'

//vue路由配置引入文件
import Router from 'vue-router'
Vue.use(Router)

//vue-resource引入(发送http请求)
import VueResource from 'vue-resource'
Vue.use(VueResource)
Vue.http.options.emulateJSON = true

//elementUI引入
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(ElementUI)

//路由页面引入
import Index from './pages/Index'
import Login from './pages/Login'
import Registration from './pages/Registration'
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
