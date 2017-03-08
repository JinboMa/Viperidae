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

new Vue({
	el: '#app',
	router,
	template: '<App/>',
	components: { App },
	created: function(){
		created(this)
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

			data.md5 && (formData.password = md5(data.formData.password))

			data.method == "GET" ? postData.params = formData : postData.body = formData

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
					this.$message.error(res)//res.body.message.error
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