<template lang="pug">
	.myHeader
		el-menu.el-menu-demo(theme="dark" v-bind:default-active="String(headerIndex)" mode="horizontal")
			el-menu-item(index="1")
				router-link(to="/")
					i.el-icon-menu
			el-submenu(index="2")
				template(slot="title") 生活
				el-menu-item(index="2-1") 工作列表
				el-menu-item(index="2-2") 生活列表
				el-menu-item(index="2-3") 其他列表
			el-submenu(index="3")
				template(slot="title") 博客
				el-menu-item(index="3-1")
					router-link(to="/Blog") 新建博客
				el-menu-item(index="3-2") 我的博客
			el-menu-item(index="4") 聊天
			el-menu-item(index="5") 设置
			el-menu-item.time(index="0" style="float:right") {{time}}
			el-menu-item.time(index="-1" style="float:right")
				router-link(to="/Login") 登录/注册
</template>

<script>
export default {
	props : ["headerIndex"],
	data(){
		return {
			time : ""
		}
	},
	created : function(){
		var Timer = setInterval(this.setTime,1000)
	},
	methods : {
		//设置右上角时间
		setTime : function(){
			var date = new Date(),
				year = date.getFullYear(),
				month = date.getMonth() + 1,
				day = date.getDate(),
				hours = date.getHours(),
				minutes = date.getMinutes(),
				seconds = date.getSeconds()
				if(String(hours).length == 1){
					hours = "0" + hours
				}
				if(String(minutes).length == 1){
					minutes = "0" + minutes
				}
				if(String(seconds).length == 1){
					seconds = "0" + seconds
				}
			var	timeStr = `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`
			this.time = timeStr
		}
	}
}
</script>

<style scoped lang="stylus">
.myHeader
	width 100%
	height 60px
	position fixed
	z-index 100
.el-icon-menu
	font-size 26px
	color #E5E9F2
	text-align center
	transform translateY(5px)
</style>
