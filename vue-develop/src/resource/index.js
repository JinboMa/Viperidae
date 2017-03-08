import Vue from 'vue'

export default function(){
	Vue.http.options.emulateJSON = true
	//Vue.http.options.emulateHTTP = true
	//Vue.http.options.credentials = true
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
}