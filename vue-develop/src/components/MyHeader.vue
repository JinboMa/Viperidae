<template lang="jade">
	.myHeader
		el-menu.el-menu-demo(theme="dark",:default-active="headerIndex",mode="horizontal",@select="select",router)
			el-menu-item(index="/")
					i.el-icon-menu
			el-submenu(index="2")
				template(slot="title") 生活
				el-menu-item(index="2-1") 工作列表
				el-menu-item(index="2-2") 生活列表
				el-menu-item(index="2-3") 其他列表
			el-submenu(index="3")
				template(slot="title") 博客
				el-menu-item(index="/Blog") 新建博客
				el-menu-item(index="/BlogList") 我的博客
			el-menu-item(index="4") 聊天
			el-menu-item(index="5") 设置
			el-menu-item(index="0",style="float:right") {{time}}
			el-submenu(index="6",style="float:right",@click="console.log(123)")
				template(slot="title") {{userName}}
				el-menu-item(index="userSetting",v-if="isLogin") 设置
				el-menu-item(index="logout",v-if="isLogin") 退出
				el-menu-item(index="/Login",v-if="!isLogin") 登录
				el-menu-item(index="/Registration",v-if="!isLogin") 注册
						

</template>

<script>
export default {
	props : ["headerIndex","isLogin"],
	data(){
		return {
			time : "",
			userName : "用户",
		}
	},
	watch:{
		'isLogin':function(value){
			value ? this.userName = localStorage.getItem('username') : this.userName = "用户"
		}
	},
	created : function(){
		var Timer = setInterval(this.setTime,1000)
		this.isLogin && (this.userName = localStorage.getItem('username'))
	},
	methods : {
		//设置右上角时间
		setTime(){
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
		},
		select(index){
			index == 'logout' && this.postLogout()
		},
		//logout
		postLogout(){
			this.$confirm('确定要退出当前账号么?', '提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
				type: 'warning'
			}).then(() => {
				this.ajax(this.setAjax("logout",{},this.success,this.fail))
			}).catch(() => {
				this.$message({
					type: 'info',
					message: '已取消退出'
				})
				this.$router.go(-1)
			})
		},
		success(res){
			this.$emit('logout')
			localStorage.removeItem('token')
			localStorage.removeItem('username')
		},
		fail(res){
			console.log('失败',res)
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
	min-width 650px
.el-icon-menu
	font-size 26px
	color #E5E9F2
	text-align center
	transform translateY(5px)
</style>
