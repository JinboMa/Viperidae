<template lang="pug">
	.myHeader
		el-menu.el-menu-demo(theme="dark" default-active="1" mode="horizontal")
			el-menu-item(index="1")
				i.el-icon-menu
			el-submenu(index="2")
				template(slot="title") 生活
				el-menu-item(index="2-1") 工作列表
				el-menu-item(index="2-2") 生活列表
				el-menu-item(index="2-3") 其他列表
			el-submenu(index="3")
				template(slot="title") 社交
				el-menu-item(index="2-1") 我的朋友圈
				el-menu-item(index="2-2") 我的微博
				el-menu-item(index="2-3") 我的QQ空间
			el-menu-item(index="4") 直播
			el-menu-item(index="5") 聊天
			el-menu-item(index="6") 设置
			el-menu-item.time(index="0" style="float:right") {{time}}
</template>

<script>
export default {
	data(){
		return {
			time : ""
		}
	},
	beforeCreat : function(){
	},
	created : function(){
		this.setTime()
	},
	methods : {
		//设置右上角时间
		setTime : function(){
			var Timer = setInterval(()=>{
				var date = new Date(),
					year = date.getFullYear(),
					month = date.getMonth() + 1,
					day = date.getDate(),
					hours = date.getHours(),
					minutes = date.getMinutes(),
					seconds = date.getSeconds(),
					timeStr = `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`
				this.time = timeStr
			},1000)
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
