//vue路由配置引入文件
import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
//路由页面引入
import Index from '../pages/Index'
import Login from '../pages/Login'
import Registration from '../pages/Registration'
import Blog from '../pages/Blog'
import BlogList from '../pages/BlogList'
export default new Router({
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
	})