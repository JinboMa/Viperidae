import Vue from 'vue'

export default function(){
	//全局变量地址
	Vue.prototype.URL = "http://23.105.208.8:8089/"
	//token
	Vue.prototype.token = 'test token string'
}