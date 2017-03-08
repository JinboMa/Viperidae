<template lang="jade">
	#app
		my-header(:headerIndex="headerIndex")
		put-top
		router-view
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
	methods: {
		
	},
	data(){
		return {
			headerIndex : "/"
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
</style>
