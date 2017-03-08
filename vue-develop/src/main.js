//初始化vue项目app模板
import Vue from 'vue'
import App from './App'

//elementUI引入
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(ElementUI)

//引入highlight css
import './assets/highlight.min.css'

//引入路由配置
import router from './router'

//引入全局变量及函数
import created from 'created'

//vue-resource引入(发送http请求)
import VueResource from 'vue-resource'
Vue.use(VueResource)
import resource from 'resource'
resource()

new Vue({
	el: '#app',
	router,
	template: '<App/>',
	components: { App },
	created(){
		created(this)
	}
})