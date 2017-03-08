import Vue from 'vue'

//md5
import md5 from 'blueimp-md5'

export default function(that){
	//全局ajax处理
	Vue.prototype.setAjax = function(name,formData,success,fail){
		var postData = that.ajaxConfig[name];
			postData.formData = formData
			postData.success = success
			postData.fail = fail
		return postData
	}
	//全局ajax方法
	Vue.prototype.ajax = function(data){
		var postData = {
			url : that.URL+data.url,
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
				that.$message({
					message: data.successMsg,
					type: 'success'
				})
				data.success(res.body)
			}else if(data.failAlert){
				//错误提示
				that.$message.error(res.body.message.error)
			}
			that.loading = false
		},
		//失败函数
		(res)=>{
			that.$message.error(`网络错误'${res.status}',${data.failMsg}`)
			that.loading = false
			data.fail(res)
		})
	}
	Vue.prototype.setHeight = function(num){
		let height = window.innerHeight
		return (height - 60 - num)
	}
}