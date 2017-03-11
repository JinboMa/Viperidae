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

//md5
import md5 from 'blueimp-md5'

//引入全局变量及函数
import created from 'created'

//vue-resource引入(发送http请求)
import VueResource from 'vue-resource'
Vue.use(VueResource)
import resource from 'resource'
resource()

//给js原生对象加方法

new Vue({
	el: '#app',
	router,
	template: '<App/>',
	components: { App },
	created: function(){
		created()
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
			if(data.token && !localStorage.getItem('token')){
				this.$message.warning("还没有登录哦,请先登录")
				this.$router.push({ path : '/Login'})
				return ;
			}
			var postData = {
				url : this.URL + data.url,
				method : data.method,
				timeout: 5000
			},
			formData = JSON.parse(JSON.stringify(data.formData))

			data.md5 && (formData.password = md5(data.formData.password))

			data.token && (formData.token = localStorage.getItem('token'))

			data.method == "GET" ? postData.params = formData : postData.body = formData

			Vue.http(postData).then(
			//成功函数
			(res)=>{
				var message = res.body.message

				if(res.body.result){
					!message && (message = data.successMsg)
					data.successAlert && this.$message.success(message)
					//成功返回的参数
					data.success(res.body.data)
				}else{
					!message && (message = data.failMsg)
					console.log(message)
					data.failAlert && this.$message.error(message)
					data.fail(res.body)
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
	}
})