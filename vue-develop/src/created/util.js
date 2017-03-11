import Vue from 'vue'


export default function(){
	Vue.prototype.setHeight = function(num){
		let height = window.innerHeight
		return (height - 60 - num)
	}
}