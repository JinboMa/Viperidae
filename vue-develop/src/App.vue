<template lang="jade">
	#app
		my-header(:headerIndex="headerIndex",:isLogin="isLogin",@logout="logout")
		put-top
		router-view(@login="login")
</template>

<script>
import MyHeader from './components/MyHeader'
import PutTop from './components/PutTop'

export default {
	name: 'app',
	components: {
		MyHeader,
		PutTop
	},
	data(){
		return {
			headerIndex : "/",
			isLogin : false
		}
	},
	watch:{
		'$route':function(to,from){
			this.headerIndex = to.path
		}
	},
	created(){
		localStorage.getItem('token') && (this.isLogin = true)
	},
	methods:{
		logout(){
			this.isLogin = false
			this.$router.push({path : '/Login'})
		},
		login(){
			this.isLogin = true
		}
	}
}
</script>

<style lang="stylus">
$AllWidth = 1050px
*
	margin 0
	padding 0
	outline none
	box-sizing border-box
	font-family "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑", Courier, monospace
html
body
#app
	height 100%
a
	text-decoration none
	color inherit
.content
	width 1020px
	min-height 500px
	margin 0 auto
::-webkit-scrollbar
	width 2px
	height 2px
	background none
::-webkit-scrollbar-track
	border-radius 1px
	background none
::-webkit-scrollbar-thumb
	background #324057
.hide
	display none
.left
	float left
.right
	float right
.prompt
	font-size 12px
	color red
</style>
