import Vue from 'vue'

//md5
import md5 from 'blueimp-md5'

export default function(){
	Vue.prototype.setHeight = function(num){
		let height = window.innerHeight
		return (height - 60 - num)
	}
}